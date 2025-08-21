# Data Analysis Toolkit 🔍

A comprehensive Python toolkit for web scraping, data cleaning, and exploratory data analysis (EDA).  
This toolkit provides professional-grade tools for the complete data analysis pipeline with real-world tested capabilities and proven performance metrics.

[![Python Version](https://img.shields.io/badge/python-3.7%2B-blue.svg)](https://python.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code Style: Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

---

## 🚀 Features

### Web Scraper
- **Multi-Source Data Scraper**: Extract data from various web sources including Wikipedia and other structured sites  
- **Fortune 500 Company Scraper**: Extract company revenue and financial data  
- **Global Demographics Scraper**: Collect population and country statistics  
- Robust error handling and comprehensive logging  
- Configurable output formats (CSV, JSON)  
- User-agent rotation and request throttling for reliable scraping  

### Data Cleaner
- **Advanced Data Cleaning Pipeline**: Handle diverse datasets including demographic, financial, and contact data  
- **99.8% Data Retention Rate**: Proven efficient cleaning with minimal data loss  
- Intelligent duplicate detection and removal  
- Phone number formatting and validation  
- Address parsing and standardization  
- Missing value handling with multiple imputation strategies  
- Data type optimization and memory usage reduction  
- Business rule implementation and validation  

### EDA Analyzer
- **Comprehensive Statistical Analysis**: Complete exploratory data analysis with professional reporting  
- **Multi-Dimensional Analysis**: Handle datasets with 19+ columns and complex relationships  
- Advanced correlation analysis with strong correlation detection (|r| > 0.7)  
- Outlier detection using IQR method with detailed reporting  
- Missing value analysis and visualization  
- Distribution analysis with skewness and kurtosis calculations  
- Professional statistical summaries and categorical analysis  
- Memory-efficient processing for large datasets  

---

## 📊 Real Performance Metrics

### Data Cleaning Performance
```
✅ Layoffs Dataset (2,361 records)
- Duplicates removed: 5
- Data retention rate: 99.8%
- Processing time: < 1 second
- Final dataset: 2,356 rows × 9 columns
```

### EDA Analysis Capabilities
```
✅ Demographics Dataset (234 countries)
- Dataset size: 234 rows × 19 columns
- Memory usage: 0.07 MB
- Missing values handled: 15 across 3 columns
- Strong correlations identified: 31 pairs
- Outliers detected: Up to 35 per column
- Processing time: < 2 seconds
```

---

## 📋 Requirements

- Python 3.7+  
- pandas  
- numpy  
- matplotlib  
- seaborn  
- requests  
- beautifulsoup4  
- scipy (for advanced statistics)  
- logging  

---

## 🛠️ Installation

### Option 1: Clone Repository
```bash
git clone https://github.com/yourusername/data-analysis-toolkit.git
cd data-analysis-toolkit
pip install -r requirements.txt
```

### Option 2: Install from PyPI (Future Release)
```bash
pip install data-analysis-toolkit
```

---

## 🎯 Quick Start

### Web Scraping
```python
from src.webscraper import DataScraper

# Initialize scraper
scraper = DataScraper()

# Scrape Fortune 500 data
fortune_data = scraper.scrape_fortune_500("fortune_500_2024.csv")

# Scrape demographic data
demo_data = scraper.scrape_demographics("world_population_2024.csv")

# Display summary
scraper.display_summary()
```

### Data Cleaning
```python
from src.data_cleaner import AdvancedDataCleaner

# Initialize cleaner
cleaner = AdvancedDataCleaner()

# Clean your data with high retention rate
cleaner.clean_all("raw_data.csv")
cleaner.save_cleaned_data("cleaned_data.csv")

# Generate detailed cleaning report
report = cleaner.generate_cleaning_report()
print(f"Data retention rate: {report['retention_rate']}%")
```

### Exploratory Data Analysis
```python
from src.eda_analyzer import ComprehensiveEDA

# Initialize EDA analyzer
eda = ComprehensiveEDA()

# Load and analyze data
eda.load_data("your_dataset.csv")
eda.run_complete_eda()

# Generate comprehensive report with statistics
report = eda.generate_comprehensive_report("eda_report.txt")

# Access specific analysis results
correlations = eda.get_strong_correlations(threshold=0.7)
outliers = eda.detect_outliers_iqr()
missing_analysis = eda.analyze_missing_values()
```

---

## 📈 Analysis Capabilities

### Statistical Analysis
- **Descriptive Statistics**: Mean, median, std, skewness, kurtosis  
- **Correlation Analysis**: Pearson correlation with strong correlation detection  
- **Distribution Analysis**: Shape analysis and normality testing  
- **Outlier Detection**: IQR method with reporting and percentages  

### Data Quality Assessment
- **Missing Value Analysis**: Breakdown by column with percentages  
- **Duplicate Detection**: Efficient identification and removal  
- **Data Type Optimization**: Automatic type inference & memory optimization  
- **Categorical Analysis**: Unique values and distributions  

### Advanced Features
- **Memory Efficient**: Minimal footprint for large datasets  
- **Batch Processing**: Handle multiple files simultaneously  
- **Custom Business Rules**: Domain-specific validation logic  
- **Export Flexibility**: Multiple formats & custom reports  

---

## 📊 Example Use Cases

1. **Global Demographics Analysis**: Population data, growth trends, outliers  
2. **Corporate Layoffs Analysis**: Employment data, industry trends, time patterns  
3. **Market Research**: Competitor scraping, contact standardization, analysis  
4. **Academic Research**: Clean survey data, statistical analysis, publishable reports  
5. **Business Intelligence**: Automate collection, ensure quality, dashboards  

---

## 📁 Project Structure

```
data-analysis-toolkit/
├── src/                    # Main source code
│   ├── webscraper.py       # Web scraping utilities
│   ├── data_cleaner.py     # Advanced data cleaning pipeline
│   └── eda_analyzer.py     # Comprehensive EDA & visualization
├── examples/               # Real usage examples & tutorials
├── data/                   
│   ├── raw/                # Raw scraped data
│   ├── processed/          # Cleaned data (99.8% retention)
│   └── outputs/            # Reports & visualizations
├── docs/                   # Documentation
├── tests/                  # Unit tests with real scenarios
└── notebooks/              # Jupyter notebooks
```

---

## 🔍 Sample Output

### Data Cleaning Report
```
============================================================
DATA CLEANING REPORT
============================================================
Original rows: 2361
Duplicates removed: 5
Do not contact removed: 0
Invalid phones removed: 0
Final rows: 2356
Data retention rate: 99.8%
============================================================
```

### EDA Analysis Summary
```
============================================================
DATASET OVERVIEW
============================================================
Shape: 234 rows × 19 columns
Memory Usage: 0.07 MB
Missing Values: 15
Duplicate Rows: 0
Strong Correlations Found: 31 pairs (|r| > 0.7)
Outliers Detected: 19-35 per column (IQR method)
============================================================
```

---

## 🧪 Testing

Run the comprehensive test suite:
```bash
python -m pytest tests/ -v
```

Run performance benchmarks:
```bash
python tests/benchmark_performance.py
```

---

## 📚 Documentation

- [Installation Guide](https://github.com/poornavenkatn08/Python_Pandas-Data-Analysis-Portfolio/blob/main/docs/Installation.md)  
- [Usage Examples with Real Data](https://github.com/poornavenkatn08/Python_Pandas-Data-Analysis-Portfolio/blob/main/docs/usage.md)  
- [API Reference](https://github.com/poornavenkatn08/Python_Pandas-Data-Analysis-Portfolio/blob/main/docs/api_reference.md)  

---

## Development Setup

1. Fork the repository  
2. Create a virtual environment: `python -m venv venv`  
3. Activate venv: `source venv/bin/activate` (Linux/Mac) or `venv\Scriptsctivate` (Windows)  
4. Install dependencies: `pip install -r requirements.txt`  
5. Install dev dependencies: `pip install -r requirements-dev.txt`  
6. Run tests: `python -m pytest tests/`  
7. Run benchmarks: `python tests/benchmark_performance.py`  

---

## 🎯 Performance Guarantees

- **Data Cleaning**: 99%+ retention rate on real datasets  
- **EDA Processing**: < 2 seconds for datasets up to 500 rows × 20 columns  
- **Memory Usage**: < 100MB for typical datasets  
- **Accuracy**: scipy-backed statistical analysis  

---

## 📜 License

This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- Wikipedia and open data sources  
- Python community (pandas, numpy, scipy)  
- Contributors and testers  
- Open data initiatives  

---

## 🔄 Changelog

### v1.0.0 (Current)
- ✅ Proven data cleaning with 99.8% retention  
- ✅ Comprehensive EDA for multi-dimensional datasets  
- ✅ Advanced statistical analysis with correlation detection  
- ✅ Efficient outlier detection (IQR method)  
- ✅ Memory-optimized processing  
- ✅ Professional logging & error handling  
- ✅ Real-world tested on demographics & employment data  
## 📬 Contact

Let’s connect! I'm open to collaboration and job opportunities in data analytics and visualization.

📧 pvneelakantam@gmail.com
🔗 https://www.linkedin.com/in/pneelakantam/
