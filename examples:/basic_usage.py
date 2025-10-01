#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#!/usr/bin/env python
"""
Basic Usage Examples for Data Analysis Toolkit

This script demonstrates how to use the three main components:
1. Web Scraper - Fortune 500 Companies
2. Data Cleaner - Customer Data Cleaning
3. EDA Analyzer - Exploratory Data Analysis

Author: Poorna Venkat Neelakntam
"""

import sys
import os
import pandas as pd

# Add src directory to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from webscraper import FortuneCompanyScraper
from data_cleaner import CustomerDataCleaner
from eda_analyzer import ComprehensiveEDA


def demonstrate_web_scraper():
    """Demonstrate web scraping functionality."""
    print("="*60)
    print("🕸️  WEB SCRAPING DEMONSTRATION")
    print("="*60)
    
    # Initialize the scraper
    scraper = FortuneCompanyScraper()
    
    # Scrape Fortune 500 data
    print("Scraping Fortune 500 companies data...")
    data = scraper.scrape_and_export("examples/sample_data/fortune_500_demo.csv")
    
    if data is not None:
        print("Web scraping completed successfully!")
        scraper.display_summary()
        
        # Save a small sample for demonstration
        sample_data = data.head(20)  # First 20 companies
        sample_data.to_csv("examples/sample_data/fortune_sample.csv", index=False)
        print("📁 Sample data saved for cleaning demonstration")
        
        return sample_data
    else:
        print(" Web scraping failed")
        return None


def demonstrate_data_cleaning():
    """Demonstrate data cleaning functionality."""
    print("\n" + "="*60)
    print("DATA CLEANING DEMONSTRATION")
    print("="*60)
    
    # Create sample messy customer data for demonstration
    sample_customer_data = pd.DataFrame({
        'First_Name': ['John123', 'JANE', 'bob--', 'Alice', 'Charlie'],
        'Last_Name': ['Smith/_', 'DOE', 'johnson', 'Brown', 'Wilson'],
        'Phone_Number': ['5551234567', '555-123-4567', 'Na--', '555.123.4567', '555-456-7890'],
        'Address': ['123 Main St, NY, 10001', '456 Oak Ave, CA, 90210', 
                   '789 Pine Rd, TX, 75001', '321 Elm St, FL, 33101', '654 Maple Dr, WA, 98001'],
        'Do_Not_Contact': ['No', 'Yes', 'FALSE', 'N', 'TRUE'],
        'Paying_Customer': ['Yes', 'No', 'TRUE', 'Y', 'FALSE']
    })
    
    # Add some duplicates and missing values
    sample_customer_data = pd.concat([sample_customer_data, sample_customer_data.iloc[:2]], ignore_index=True)
    sample_customer_data.loc[5, 'Phone_Number'] = 'N/A'
    sample_customer_data.loc[6, 'First_Name'] = None
    
    # Save sample data
    os.makedirs("examples/sample_data", exist_ok=True)
    sample_customer_data.to_csv("examples/sample_data/messy_customer_data.csv", index=False)
    
    # Initialize cleaner
    cleaner = CustomerDataCleaner()
    
    # Clean the data
    print("Cleaning customer data...")
    if cleaner.clean_all("examples/sample_data/messy_customer_data.csv"):
        cleaner.save_cleaned_data("examples/sample_data/cleaned_customer_data.csv")
        print(" Data cleaning completed successfully!")
        print(cleaner.generate_cleaning_report())
        
        print("\nCleaned Data Preview:")
        print(cleaner.df.head())
        
        return cleaner.df
    else:
        print("Data cleaning failed")
        return None


def demonstrate_eda():
    """Demonstrate EDA functionality."""
    print("\n" + "="*60)
    print("EXPLORATORY DATA ANALYSIS DEMONSTRATION")
    print("="*60)
    
    # Create sample dataset for EDA demonstration
    import numpy as np
    np.random.seed(42)  # For reproducible results
    
    # Generate sample sales data
    n_samples = 1000
    sample_eda_data = pd.DataFrame({
        'Product_Category': np.random.choice(['Electronics', 'Clothing', 'Books', 'Home', 'Sports'], n_samples),
        'Sales_Amount': np.random.lognormal(4, 1, n_samples),
        'Customer_Age': np.random.normal(35, 12, n_samples),
        'Customer_Satisfaction': np.random.normal(4.2, 0.8, n_samples),
        'Region': np.random.choice(['North', 'South', 'East', 'West'], n_samples),
        'Marketing_Spend': np.random.exponential(100, n_samples),
        'Units_Sold': np.random.poisson(5, n_samples)
    })
    
    # Add some correlations
    sample_eda_data['Revenue'] = sample_eda_data['Sales_Amount'] * sample_eda_data['Units_Sold']
    sample_eda_data['Profit_Margin'] = np.random.normal(0.15, 0.05, n_samples)
    
    # Add some missing values
    missing_indices = np.random.choice(n_samples, size=50, replace=False)
    sample_eda_data.loc[missing_indices, 'Customer_Satisfaction'] = np.nan
    
    # Save sample data
    sample_eda_data.to_csv("examples/sample_data/sales_data_demo.csv", index=False)
    
    # Initialize EDA analyzer
    eda = ComprehensiveEDA(figsize=(10, 6))
    
    # Load and analyze data
    print("Loading sample sales data for EDA...")
    if eda.load_data("examples/sample_data/sales_data_demo.csv"):
        print(" Data loaded successfully!")
        
        # Run comprehensive EDA
        print("\nRunning comprehensive EDA analysis...")
        eda.run_complete_eda()
        
        # Generate detailed report
        report = eda.generate_comprehensive_report("examples/sample_data/eda_report_demo.txt")
        print("Comprehensive EDA report generated!")
        
        return sample_eda_data
    else:
        print("EDA analysis failed")
        return None


def create_sample_notebooks():
    """Create sample Jupyter notebook content."""
    print("\n" + "="*60)
    print("CREATING SAMPLE NOTEBOOKS")
    print("="*60)
    
    # Create notebooks directory
    os.makedirs("notebooks", exist_ok=True)
    
    # Basic notebook content (as markdown for demonstration)
    notebook_content = """
# Data Analysis Toolkit Tutorial

## Introduction
This notebook demonstrates the complete data analysis workflow using our toolkit.

## 1. Web Scraping
```python
from src.webscraper import FortuneCompanyScraper

scraper = FortuneCompanyScraper()
data = scraper.scrape_and_export("fortune_data.csv")
scraper.display_summary()
```

## 2. Data Cleaning
```python
from src.data_cleaner import CustomerDataCleaner

cleaner = CustomerDataCleaner()
cleaner.clean_all("raw_data.csv")
cleaner.save_cleaned_data("cleaned_data.csv")
print(cleaner.generate_cleaning_report())
```

## 3. Exploratory Data Analysis
```python
from src.eda_analyzer import ComprehensiveEDA

eda = ComprehensiveEDA()
eda.load_data("cleaned_data.csv")
eda.run_complete_eda()
```
"""
    
    # Save as markdown (you can convert to .ipynb format later)
    with open("notebooks/01_complete_tutorial.md", "w") as f:
        f.write(notebook_content)
    
    print(" Sample notebook templates created!")


def main():
    """Run all demonstrations."""
    print(" STARTING DATA ANALYSIS TOOLKIT DEMONSTRATIONS")
    print("="*80)
    
    try:
        # Demonstrate web scraping
        scraped_data = demonstrate_web_scraper()
        
        # Demonstrate data cleaning
        cleaned_data = demonstrate_data_cleaning()
        
        # Demonstrate EDA
        eda_data = demonstrate_eda()
        
        # Create sample notebooks
        create_sample_notebooks()
        
        print("\n" + "="*80)
        print(" ALL DEMONSTRATIONS COMPLETED SUCCESSFULLY!")
        print("="*80)
        
        print("\n📁 Files created:")
        print("- examples/sample_data/fortune_500_demo.csv")
        print("- examples/sample_data/fortune_sample.csv") 
        print("- examples/sample_data/messy_customer_data.csv")
        print("- examples/sample_data/cleaned_customer_data.csv")
        print("- examples/sample_data/sales_data_demo.csv")
        print("- examples/sample_data/eda_report_demo.txt")
        print("- notebooks/01_complete_tutorial.md")
        
        print("\n Next Steps:")
        print("1. Review the generated sample data and reports")
        print("2. Modify the code for your specific use cases")
        print("3. Run individual components as needed")
        print("4. Check the documentation in docs/ folder")
        
    except Exception as e:
        print(f"\n Error during demonstration: {e}")
        print("Please check the error logs and ensure all dependencies are installed.")


if __name__ == "__main__":
    main()

