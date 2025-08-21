# Data Analysis 🔍

A comprehensive Python toolkit for web scraping, data cleaning, and exploratory data analysis (EDA). This toolkit provides professional-grade tools for the complete data analysis pipeline.

[![Python Version](https://img.shields.io/badge/python-3.7%2B-blue.svg)](https://python.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code Style: Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

## 🚀 Features

### Web Scraper
- **Fortune 500 Company Scraper**: Extract company revenue data from Wikipedia
- Robust error handling and logging
- Configurable output formats (CSV, JSON)
- User-agent rotation and request throttling

### Data Cleaner
- **Comprehensive Data Cleaning Pipeline**: Handle customer contact lists and general datasets
- Duplicate removal and data standardization
- Phone number formatting and validation
- Address parsing and business rule implementation
- Missing value handling and data type optimization

### EDA Analyzer
- **Professional Exploratory Data Analysis**: Complete statistical analysis and visualization
- Statistical summaries and correlation analysis
- Missing value analysis and outlier detection
- Distribution analysis with professional visualizations
- Comprehensive reporting capabilities

## 📋 Requirements

- Python 3.7+
- pandas
- numpy
- matplotlib
- seaborn
- requests
- beautifulsoup4
- logging

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

## 🎯 Quick Start

### Web Scraping
```python
from src.webscraper import FortuneCompanyScraper

# Initialize scraper
scraper = FortuneCompanyScraper()

# Scrape Fortune 500 data
data = scraper.scrape_and_export("fortune_500_2024.csv")

# Display summary
scraper.display_summary()
```

### Data Cleaning
```python
from src.data_cleaner import CustomerDataCleaner

# Initialize cleaner
cleaner = CustomerDataCleaner()

# Clean your data
cleaner.clean_all("raw_customer_data.csv")
cleaner.save_cleaned_data("cleaned_customer_data.csv")

# Generate cleaning report
print(cleaner.generate_cleaning_report())
```

### Exploratory Data Analysis
```python
from src.eda_analyzer import ComprehensiveEDA

# Initialize EDA analyzer
eda = ComprehensiveEDA()

# Load and analyze data
eda.load_data("your_dataset.csv")
eda.run_complete_eda()

# Generate comprehensive report
report = eda.generate_comprehensive_report("eda_report.txt")
```

## 📊 Example Use Cases

1. **E-commerce Analysis**: Scrape competitor data, clean customer lists, and analyze sales patterns
2. **Market Research**: Extract company information, standardize contact data, and perform market analysis
3. **Academic Research**: Clean survey data, perform statistical analysis, and generate research reports
4. **Business Intelligence**: Automate data collection, ensure data quality, and create analytical dashboards

## 📁 Project Structure

```
data-analysis-toolkit/
├── src/                    # Main source code
│   ├── webscraper.py      # Web scraping utilities
│   ├── data_cleaner.py    # Data cleaning pipeline
│   └── eda_analyzer.py    # EDA and visualization tools
├── examples/              # Usage examples and tutorials
├── data/                  # Data directories
│   ├── raw/              # Raw data files
│   ├── processed/        # Cleaned data files
│   └── outputs/          # Analysis outputs
├── docs/                 # Documentation
├── tests/                # Unit tests
└── notebooks/            # Jupyter notebooks with tutorials
```

## 🧪 Testing

Run the test suite:

```bash
python -m pytest tests/
```

## 📚 Documentation

Detailed documentation is available in the `docs/` directory:

- [Installation Guide](https://github.com/poornavenkatn08/Python_Pandas-Data-Analysis-Portfolio/blob/main/docs/Installation.md)
- [Usage Examples](https://github.com/poornavenkatn08/Python_Pandas-Data-Analysis-Portfolio/blob/main/docs/usage.md)
- [API Reference](https://github.com/poornavenkatn08/Python_Pandas-Data-Analysis-Portfolio/blob/main/docs/api_reference.md)


### Development Setup

1. Fork the repository
2. Create a virtual environment: `python -m venv venv`
3. Activate virtual environment: `source venv/bin/activate` (Linux/Mac) or `venv\Scripts\activate` (Windows)
4. Install dependencies: `pip install -r requirements.txt`
5. Install development dependencies: `pip install -r requirements-dev.txt`
6. Run tests: `python -m pytest tests/`

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Wikipedia for providing accessible data sources
- The Python community for excellent data analysis libraries
- Contributors and users who help improve this toolkit


## 🔄 Changelog

### v1.0.0 (Current)
- Initial release
- Web scraper for Fortune 500 companies
- Comprehensive data cleaning pipeline
- Full EDA toolkit with visualizations
- Professional logging and error handling

---

⭐ **Star this repository if you find it helpful!**

📬 Contact

Let’s connect! I'm open to collaboration and job opportunities in data analytics and visualization.

📧 pvneelakantam@gmail.com
🔗 https://www.linkedin.com/in/pneelakantam/
