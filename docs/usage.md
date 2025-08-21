# Usage Guide

This guide provides comprehensive examples and best practices for using the Data Analysis Toolkit.

## 📖 Table of Contents

1. [Quick Start](#quick-start)
2. [Web Scraper Usage](#web-scraper-usage)
3. [Data Cleaner Usage](#data-cleaner-usage)
4. [EDA Analyzer Usage](#eda-analyzer-usage)
5. [Complete Workflow Examples](#complete-workflow-examples)
6. [Best Practices](#best-practices)
7. [Advanced Usage](#advanced-usage)
8. [Troubleshooting](#troubleshooting)

## 🚀 Quick Start

### Basic Import and Setup

```python
# Import all components
from src.webscraper import FortuneCompanyScraper
from src.data_cleaner import CustomerDataCleaner
from src.eda_analyzer import ComprehensiveEDA

# Or import the entire package
import src as dat
```

### Run Complete Demo

```python
# Generate sample data and run all demonstrations
python examples/basic_usage.py
```

## 🕸️ Web Scraper Usage

### Basic Fortune 500 Scraping

```python
from src.webscraper import FortuneCompanyScraper

# Initialize scraper
scraper = FortuneCompanyScraper()

# Simple scrape and export
data = scraper.scrape_and_export("fortune_companies.csv")

if data is not None:
    print(f"Scraped {len(data)} companies successfully!")
    scraper.display_summary()
else:
    print("Scraping failed - check logs")
```

### Advanced Scraping Configuration

```python
# Custom configuration
scraper = FortuneCompanyScraper()

# Modify headers for different user agent
scraper.headers['User-Agent'] = 'Your Custom User Agent'

# Scrape with custom filename
data = scraper.scrape_and_export("companies_2024.csv")

# Access raw data for further processing
if scraper.df is not None:
    # Filter top 100 companies
    top_100 = scraper.df.head(100)
    
    # Save filtered data
    scraper.save_


```python

```
