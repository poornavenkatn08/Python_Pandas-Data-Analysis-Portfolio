#!/usr/bin/env python
"""
Fortune 500 Companies Web Scraper

This script scrapes the list of largest companies in the United States by revenue
from Wikipedia and exports the data to a CSV file.

Author: Poorna Venkat Neelakantam
Dependencies: requests, beautifulsoup4, pandas
"""

import pandas as pd
import requests
from bs4 import BeautifulSoup
import logging
from typing import List, Optional
import os

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class FortuneCompanyScraper:
    """
    A web scraper for extracting Fortune 500 company data from Wikipedia.
    
    This class handles the complete process of scraping, parsing, and exporting
    company revenue data from Wikipedia's largest companies list.
    """
    
    def __init__(self):
        self.url = "https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue"
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        self.df = None
    
    def fetch_webpage(self) -> Optional[BeautifulSoup]:
        """
        Fetches the webpage and returns a BeautifulSoup object.
        
        Returns:
            BeautifulSoup: Parsed HTML content or None if failed
        """
        try:
            logger.info(f"Fetching data from: {self.url}")
            response = requests.get(self.url, headers=self.headers, timeout=10)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.text, 'html.parser')
            logger.info("Successfully fetched and parsed webpage")
            return soup
            
        except requests.RequestException as e:
            logger.error(f"Failed to fetch webpage: {e}")
            return None
    
    def extract_table_data(self, soup: BeautifulSoup) -> Optional[pd.DataFrame]:
        """
        Extracts table data from the BeautifulSoup object.
        
        Args:
            soup (BeautifulSoup): Parsed HTML content
            
        Returns:
            pd.DataFrame: Extracted company data or None if failed
        """
        try:
            # Find the main table (usually the first one)
            tables = soup.find_all('table', class_='wikitable')
            if not tables:
                logger.error("No tables found on the webpage")
                return None
            
            table = tables[0]  # Get the first table
            logger.info("Found data table")
            
            # Extract headers
            headers = table.find_all('th')
            column_names = [header.text.strip() for header in headers]
            logger.info(f"Extracted columns: {column_names}")
            
            # Create DataFrame with extracted columns
            df = pd.DataFrame(columns=column_names)
            
            # Extract row data
            rows = table.find_all('tr')[1:]  # Skip header row
            
            for i, row in enumerate(rows):
                cells = row.find_all('td')
                if len(cells) == len(column_names):
                    row_data = [cell.text.strip() for cell in cells]
                    df.loc[len(df)] = row_data
                    
            logger.info(f"Successfully extracted {len(df)} companies")
            return df
            
        except Exception as e:
            logger.error(f"Failed to extract table data: {e}")
            return None
    
    def clean_data(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Cleans the extracted data for better usability.
        
        Args:
            df (pd.DataFrame): Raw extracted data
            
        Returns:
            pd.DataFrame: Cleaned data
        """
        try:
            # Make a copy to avoid modifying original
            cleaned_df = df.copy()
            
            # Remove any rows with all NaN values
            cleaned_df = cleaned_df.dropna(how='all')
            
            # Clean revenue column if it exists (remove $ and convert to numeric)
            revenue_columns = [col for col in cleaned_df.columns if 'revenue' in col.lower()]
            for col in revenue_columns:
                if col in cleaned_df.columns:
                    # Remove currency symbols and commas, then convert to numeric
                    cleaned_df[col] = cleaned_df[col].str.replace(r'[\$,]', '', regex=True)
                    cleaned_df[col] = pd.to_numeric(cleaned_df[col], errors='coerce')
            
            # Reset index
            cleaned_df = cleaned_df.reset_index(drop=True)
            
            logger.info("Data cleaning completed")
            return cleaned_df
            
        except Exception as e:
            logger.error(f"Data cleaning failed: {e}")
            return df
    
    def save_to_csv(self, df: pd.DataFrame, filename: str = "fortune_companies.csv") -> bool:
        """
        Saves the DataFrame to a CSV file.
        
        Args:
            df (pd.DataFrame): Data to save
            filename (str): Output filename
            
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            # Create output directory if it doesn't exist
            output_dir = "data/processed"
            os.makedirs(output_dir, exist_ok=True)
            
            filepath = os.path.join(output_dir, filename)
            df.to_csv(filepath, index=False, encoding='utf-8')
            
            logger.info(f"Data saved successfully to: {filepath}")
            return True
            
        except Exception as e:
            logger.error(f"Failed to save CSV: {e}")
            return False
    
    def scrape_and_export(self, output_filename: str = "fortune_companies.csv") -> Optional[pd.DataFrame]:
        """
        Main method to execute the complete scraping and export process.
        
        Args:
            output_filename (str): Name of the output CSV file
            
        Returns:
            pd.DataFrame: Scraped data or None if failed
        """
        # Fetch webpage
        soup = self.fetch_webpage()
        if soup is None:
            return None
        
        # Extract table data
        df = self.extract_table_data(soup)
        if df is None:
            return None
        
        # Clean data
        df = self.clean_data(df)
        
        # Save to CSV
        if self.save_to_csv(df, output_filename):
            self.df = df
            return df
        
        return None
    
    def display_summary(self) -> None:
        """Displays a summary of the scraped data."""
        if self.df is not None:
            print("\n" + "="*50)
            print("SCRAPING SUMMARY")
            print("="*50)
            print(f"Total companies scraped: {len(self.df)}")
            print(f"Columns: {list(self.df.columns)}")
            print(f"Data shape: {self.df.shape}")
            print("\nFirst 5 rows:")
            print(self.df.head())
        else:
            print("No data available. Please run scrape_and_export() first.")


def main():
    """Main function to demonstrate the scraper."""
    scraper = FortuneCompanyScraper()
    
    # Scrape data and export to CSV
    data = scraper.scrape_and_export("largest_us_companies_2024.csv")
    
    if data is not None:
        scraper.display_summary()
        print("\n✅ Scraping completed successfully!")
    else:
        print("\n❌ Scraping failed. Check logs for details.")


if __name__ == "__main__":
    main()
