# API Reference

Quick reference for all the main functions.

## Web Scraper

### FortuneCompanyScraper

**Main Methods:**
- `scrape_and_export(filename)` - Scrapes data and saves to CSV
- `display_summary()` - Shows what was scraped

**Example:**
```python
scraper = FortuneCompanyScraper()
data = scraper.scrape_and_export("companies.csv")
```

## Data Cleaner

### CustomerDataCleaner

**Main Methods:**
- `clean_all(filepath)` - Cleans the entire dataset
- `save_cleaned_data(filepath)` - Saves cleaned data
- `generate_cleaning_report()` - Shows what was cleaned

**Example:**
```python
cleaner = CustomerDataCleaner()
cleaner.clean_all("messy.csv")
cleaner.save_cleaned_data("clean.csv")
```

## EDA Analyzer

### ComprehensiveEDA

**Main Methods:**
- `load_data(filepath)` - Loads your data
- `run_complete_eda()` - Runs all analysis
- `generate_comprehensive_report()` - Creates detailed report

**Example:**
```python
eda = ComprehensiveEDA()
eda.load_data("data.csv")
eda.run_complete_eda()
```


```python

```
