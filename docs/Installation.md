# Installation Guide

This guide will help you install and set up the Data Analysis Toolkit on your system.

## Prerequisites

- Python 3.7 or higher
- pip (Python package installer)
- Git (for cloning the repository)

## Installation Methods

### Method 1: Clone from GitHub (Recommended for Development)

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/data-analysis-toolkit.git
   cd data-analysis-toolkit
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**
   - On Linux/Mac:
     ```bash
     source venv/bin/activate
     ```
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Install the package in development mode**
   ```bash
   pip install -e .
   ```

### Method 2: Direct Installation from PyPI (Future Release)

```bash
pip install data-analysis-toolkit
```

## Verify Installation

Test your installation by running:

```python
import sys
sys.path.append('src')

from webscraper import FortuneCompanyScraper
from data_cleaner import CustomerDataCleaner  
from eda_analyzer import ComprehensiveEDA

print("✅ All modules imported successfully!")
```

## Dependencies

The toolkit requires the following Python packages:

### Core Dependencies
- `pandas >= 1.3.0` - Data manipulation and analysis
- `numpy >= 1.21.0` - Numerical computing
- `requests >= 2.25.0` - HTTP library for web scraping
- `beautifulsoup4 >= 4.9.0` - HTML parsing for web scraping
- `matplotlib >= 3.4.0` - Plotting library
- `seaborn >= 0.11.0` - Statistical data visualization

### Optional Dependencies
- `jupyter >= 1.0.0` - For running notebook tutorials
- `pytest >= 6.0.0` - For running tests
- `black >= 21.0.0` - Code formatting

## Troubleshooting

### Common Issues

**Issue: ImportError when importing modules**
```
Solution: Make sure you've installed the package with `pip install -e .` and that you're in the correct directory.
```

**Issue: Missing dependencies**
```
Solution: Install all dependencies with `pip install -r requirements.txt`
```

**Issue: Permission errors on Windows**
```
Solution: Run command prompt as administrator or use `--user` flag:
pip install --user -r requirements.txt
```

**Issue: SSL certificate errors during web scraping**
```
Solution: Update certificates or use requests with verify=False (not recommended for production)
```

### System-Specific Instructions

#### Windows Users
- Use `py` instead of `python` if you have multiple Python versions
- Use `venv\Scripts\activate` to activate virtual environment
- Consider using Windows Subsystem for Linux (WSL) for better compatibility

#### macOS Users
- You may need to install Xcode command line tools: `xcode-select --install`
- Consider using Homebrew to manage Python: `brew install python`

#### Linux Users
- Install Python development headers: `sudo apt-get install python3-dev` (Ubuntu/Debian)
- For matplotlib, you may need: `sudo apt-get install python3-tk`

## Development Setup

If you plan to contribute to the project:

1. **Fork the repository** on GitHub

2. **Clone your fork**
   ```bash
   git clone https://github.com/yourusername/data-analysis-toolkit.git
   cd data-analysis-toolkit
   ```

3. **Create a development branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

4. **Install development dependencies**
   ```bash
   pip install -r requirements.txt
   pip install pytest black flake8 mypy coverage
   ```

5. **Install pre-commit hooks** (optional but recommended)
   ```bash
   pip install pre-commit
   pre-commit install
   ```

## Docker Installation (Alternative)

If you prefer using Docker:

1. **Create a Dockerfile** (not included in repository):
   ```dockerfile
   FROM python:3.9
   WORKDIR /app
   COPY requirements.txt .
   RUN pip install -r requirements.txt
   COPY . .
   RUN pip install -e .
   ```

2. **Build and run**
   ```bash
   docker build -t data-analysis-toolkit .
   docker run -it data-analysis-toolkit python
   ```

## Next Steps

After installation:

1. Check out the [Usage Guide](usage.md) for examples
2. Run the example scripts in the `examples/` directory
3. Explore the Jupyter notebooks in the `notebooks/` directory
4. Read the [API Reference](api_reference.md) for detailed documentation

## Getting Help

If you encounter any installation issues:

1. Check the [troubleshooting section](#troubleshooting) above
2. Search existing [GitHub issues](https://github.com/yourusername/data-analysis-toolkit/issues)
3. Create a new issue with:
   - Your operating system and Python version
   - Complete error messages
   - Steps you've already tried

## Uninstallation

To remove the toolkit:

```bash
pip uninstall data-analysis-toolkit
```

To completely clean up:
```bash
# Remove virtual environment
rm -rf venv

# Remove cloned repository
cd ..
rm -rf data-analysis-toolkit
```


```python

```
