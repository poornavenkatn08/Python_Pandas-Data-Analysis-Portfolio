#!/usr/bin/env python
"""
Customer Data Cleaning Pipeline

This script provides a comprehensive data cleaning solution for customer contact lists,
including deduplication, data validation, standardization, and business rule implementation.

Author: Poorna Venkat Neelakantam

Dependencies: pandas, re
"""

import pandas as pd
import re
import logging
from typing import Dict, List, Optional, Tuple
import os

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class CustomerDataCleaner:
    """
    A comprehensive data cleaning pipeline for customer contact information.
    
    This class handles various data quality issues including:
    - Duplicate removal
    - Data standardization
    - Missing value handling
    - Business rule implementation
    """
    
    def __init__(self):
        self.df = None
        self.cleaning_report = {
            'original_rows': 0,
            'duplicates_removed': 0,
            'invalid_phones_removed': 0,
            'do_not_contact_removed': 0,
            'final_rows': 0
        }
    
    def load_data(self, filepath: str) -> bool:
        """
        Loads customer data from Excel or CSV file.
        
        Args:
            filepath (str): Path to the data file
            
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            file_extension = os.path.splitext(filepath)[1].lower()
            
            if file_extension == '.xlsx':
                self.df = pd.read_excel(filepath)
            elif file_extension == '.csv':
                self.df = pd.read_csv(filepath)
            else:
                raise ValueError(f"Unsupported file format: {file_extension}")
            
            self.cleaning_report['original_rows'] = len(self.df)
            logger.info(f"Successfully loaded {len(self.df)} rows from {filepath}")
            return True
            
        except Exception as e:
            logger.error(f"Failed to load data: {e}")
            return False
    
    def remove_duplicates(self) -> None:
        """Removes duplicate rows from the dataset."""
        if self.df is None:
            logger.error("No data loaded")
            return
        
        initial_count = len(self.df)
        self.df = self.df.drop_duplicates()
        
        duplicates_removed = initial_count - len(self.df)
        self.cleaning_report['duplicates_removed'] = duplicates_removed
        
        if duplicates_removed > 0:
            logger.info(f"Removed {duplicates_removed} duplicate rows")
        else:
            logger.info("No duplicate rows found")
    
    def remove_unnecessary_columns(self, columns_to_remove: List[str] = None) -> None:
        """
        Removes unnecessary columns from the dataset.
        
        Args:
            columns_to_remove (List[str]): List of column names to remove
        """
        if self.df is None:
            logger.error("No data loaded")
            return
        
        if columns_to_remove is None:
            # Default columns to remove based on common patterns
            columns_to_remove = [col for col in self.df.columns 
                               if 'not_useful' in col.lower() or 'unused' in col.lower()]
        
        existing_columns = [col for col in columns_to_remove if col in self.df.columns]
        
        if existing_columns:
            self.df = self.df.drop(columns=existing_columns)
            logger.info(f"Removed columns: {existing_columns}")
        else:
            logger.info("No unnecessary columns found to remove")
    
    def clean_names(self) -> None:
        """Cleans first and last name fields."""
        if self.df is None:
            logger.error("No data loaded")
            return
        
        name_columns = ['First_Name', 'Last_Name', 'first_name', 'last_name']
        existing_name_columns = [col for col in name_columns if col in self.df.columns]
        
        for col in existing_name_columns:
            # Remove special characters and digits from names
            self.df[col] = self.df[col].astype(str).str.strip("123./_-")
            self.df[col] = self.df[col].str.title()  # Proper case
            
        logger.info(f"Cleaned name columns: {existing_name_columns}")
    
    def standardize_phone_numbers(self) -> None:
        """
        Standardizes phone number formats to XXX-XXX-XXXX pattern.
        Removes invalid phone numbers.
        """
        if self.df is None:
            logger.error("No data loaded")
            return
        
        phone_columns = ['Phone_Number', 'phone_number', 'Phone', 'phone']
        existing_phone_columns = [col for col in phone_columns if col in self.df.columns]
        
        for col in existing_phone_columns:
            # Convert to string and handle NaN values
            self.df[col] = self.df[col].astype(str)
            
            # Remove common invalid patterns
            self.df[col] = self.df[col].str.replace('Na--', '', regex=False)
            self.df[col] = self.df[col].str.replace('nan--', '', regex=False)
            
            # Extract only digits
            self.df[col] = self.df[col].str.replace(r'[^0-9]', '', regex=True)
            
            # Format valid 10-digit numbers
            mask = self.df[col].str.len() == 10
            self.df.loc[mask, col] = (self.df.loc[mask, col].str[:3] + '-' + 
                                      self.df.loc[mask, col].str[3:6] + '-' + 
                                      self.df.loc[mask, col].str[6:10])
            
            # Mark invalid phone numbers for removal
            invalid_mask = (~mask) & (self.df[col] != '')
            self.df.loc[invalid_mask, col] = ''
            
        logger.info(f"Standardized phone number columns: {existing_phone_columns}")
    
    def parse_addresses(self) -> None:
        """Parses address into separate components (street, state, zip)."""
        if self.df is None:
            logger.error("No data loaded")
            return
        
        address_column = None
        for col in ['Address', 'address', 'Full_Address']:
            if col in self.df.columns:
                address_column = col
                break
        
        if address_column is None:
            logger.info("No address column found to parse")
            return
        
        # Split address by comma
        try:
            address_parts = self.df[address_column].str.split(',', n=2, expand=True)
            
            if len(address_parts.columns) >= 2:
                self.df['Street_Address'] = address_parts[0].str.strip()
                self.df['State'] = address_parts[1].str.strip() if len(address_parts.columns) > 1 else ''
                self.df['Zip_Code'] = address_parts[2].str.strip() if len(address_parts.columns) > 2 else ''
                
                logger.info("Successfully parsed address into components")
            
        except Exception as e:
            logger.error(f"Failed to parse addresses: {e}")
    
    def standardize_boolean_fields(self) -> None:
        """Standardizes boolean fields to Y/N format."""
        if self.df is None:
            logger.error("No data loaded")
            return
        
        boolean_columns = [col for col in self.df.columns 
                          if any(keyword in col.lower() for keyword in ['do_not_contact', 'paying_customer', 'active'])]
        
        for col in boolean_columns:
            # Standardize Yes/No to Y/N
            self.df[col] = self.df[col].astype(str)
            self.df[col] = self.df[col].str.replace('Yes', 'Y', regex=False)
            self.df[col] = self.df[col].str.replace('No', 'N', regex=False)
            self.df[col] = self.df[col].str.replace('TRUE', 'Y', regex=False)
            self.df[col] = self.df[col].str.replace('FALSE', 'N', regex=False)
            
        logger.info(f"Standardized boolean fields: {boolean_columns}")
    
    def handle_missing_values(self) -> None:
        """Handles missing values appropriately."""
        if self.df is None:
            logger.error("No data loaded")
            return
        
        # Fill NaN values with empty strings for most columns
        self.df = self.df.fillna('')
        
        # Replace various representations of missing data
        missing_patterns = ['N/a', 'N/A', 'null', 'NULL', 'None', 'NONE']
        for pattern in missing_patterns:
            self.df = self.df.replace(pattern, '')
        
        logger.info("Handled missing values")
    
    def apply_business_rules(self) -> None:
        """
        Applies business rules to filter out unwanted records.
        
        Rules applied:
        1. Remove records marked as "Do Not Contact"
        2. Remove records without valid phone numbers
        """
        if self.df is None:
            logger.error("No data loaded")
            return
        
        initial_count = len(self.df)
        
        # Rule 1: Remove "Do Not Contact" records
        do_not_contact_cols = [col for col in self.df.columns if 'do_not_contact' in col.lower()]
        for col in do_not_contact_cols:
            before_count = len(self.df)
            self.df = self.df[self.df[col] != 'Y']
            removed = before_count - len(self.df)
            self.cleaning_report['do_not_contact_removed'] += removed
            
        # Rule 2: Remove records without valid phone numbers
        phone_cols = [col for col in self.df.columns if 'phone' in col.lower()]
        for col in phone_cols:
            before_count = len(self.df)
            self.df = self.df[self.df[col] != '']
            removed = before_count - len(self.df)
            self.cleaning_report['invalid_phones_removed'] += removed
        
        total_removed = initial_count - len(self.df)
        logger.info(f"Applied business rules, removed {total_removed} records")
    
    def cleanup_columns(self) -> None:
        """Removes temporary and unnecessary columns."""
        if self.df is None:
            logger.error("No data loaded")
            return
        
        columns_to_remove = []
        
        # Remove original address column if we've parsed it
        if 'Street_Address' in self.df.columns and 'Address' in self.df.columns:
            columns_to_remove.append('Address')
            
        # Remove zip code if it's mostly empty
        if 'Zip_Code' in self.df.columns:
            if self.df['Zip_Code'].str.strip().eq('').sum() > len(self.df) * 0.8:
                columns_to_remove.append('Zip_Code')
        
        if columns_to_remove:
            self.df = self.df.drop(columns=columns_to_remove)
            logger.info(f"Removed unnecessary columns: {columns_to_remove}")
    
    def finalize_data(self) -> None:
        """Final data preparation steps."""
        if self.df is None:
            logger.error("No data loaded")
            return
        
        # Reset index
        self.df = self.df.reset_index(drop=True)
        
        # Update final count
        self.cleaning_report['final_rows'] = len(self.df)
        
        logger.info("Data finalization completed")
    
    def clean_all(self, filepath: str) -> bool:
        """
        Executes the complete data cleaning pipeline.
        
        Args:
            filepath (str): Path to the input data file
            
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            # Load data
            if not self.load_data(filepath):
                return False
            
            # Execute cleaning steps
            logger.info("Starting data cleaning pipeline...")
            
            self.remove_duplicates()
            self.remove_unnecessary_columns()
            self.clean_names()
            self.standardize_phone_numbers()
            self.parse_addresses()
            self.standardize_boolean_fields()
            self.handle_missing_values()
            self.apply_business_rules()
            self.cleanup_columns()
            self.finalize_data()
            
            logger.info("Data cleaning pipeline completed successfully")
            return True
            
        except Exception as e:
            logger.error(f"Data cleaning pipeline failed: {e}")
            return False
    
    def save_cleaned_data(self, output_filepath: str) -> bool:
        """
        Saves the cleaned data to a CSV file.
        
        Args:
            output_filepath (str): Path for the output file
            
        Returns:
            bool: True if successful, False otherwise
        """
        if self.df is None:
            logger.error("No cleaned data to save")
            return False
        
        try:
            # Create output directory if it doesn't exist
            os.makedirs(os.path.dirname(output_filepath), exist_ok=True)
            
            self.df.to_csv(output_filepath, index=False)
            logger.info(f"Cleaned data saved to: {output_filepath}")
            return True
            
        except Exception as e:
            logger.error(f"Failed to save cleaned data: {e}")
            return False
    
    def generate_cleaning_report(self) -> str:
        """
        Generates a summary report of the cleaning process.
        
        Returns:
            str: Formatted cleaning report
        """
        report = "\n" + "="*60
        report += "\nDATA CLEANING REPORT"
        report += "\n" + "="*60
        report += f"\nOriginal rows: {self.cleaning_report['original_rows']}"
        report += f"\nDuplicates removed: {self.cleaning_report['duplicates_removed']}"
        report += f"\nDo not contact removed: {self.cleaning_report['do_not_contact_removed']}"
        report += f"\nInvalid phones removed: {self.cleaning_report['invalid_phones_removed']}"
        report += f"\nFinal rows: {self.cleaning_report['final_rows']}"
        
        if self.cleaning_report['original_rows'] > 0:
            retention_rate = (self.cleaning_report['final_rows'] / self.cleaning_report['original_rows']) * 100
            report += f"\nData retention rate: {retention_rate:.1f}%"
        
        report += "\n" + "="*60
        
        if self.df is not None:
            report += f"\n\nFinal dataset shape: {self.df.shape}"
            report += f"\nColumns: {list(self.df.columns)}"
        
        return report


def main():
    """Main function to demonstrate the data cleaning pipeline."""
    # Example usage
    cleaner = CustomerDataCleaner()
    
    # Replace with your actual file path
    input_file = "/Users/poornavenkat/Documents/GitHub/SQL-Projects/01_tech_layoffs_analysis:/Data/Raw/layoffs_Raw.csv"
    output_file = "d'/Users/poornavenkat/Documents/GitHub/SQL-Projects/01_tech_layoffs_analysis:/Data/Raw/layoffs_Cleaned.csv'"
    
    if cleaner.clean_all(input_file):
        cleaner.save_cleaned_data(output_file)
        print(cleaner.generate_cleaning_report())
        print("\n✅ Data cleaning completed successfully!")
        
        # Display sample of cleaned data
        print("\nSample of cleaned data:")
        print(cleaner.df.head())
    else:
        print("\n❌ Data cleaning failed. Check logs for details.")


if __name__ == "__main__":
    main()
