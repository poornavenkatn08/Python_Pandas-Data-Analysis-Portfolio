#!/usr/bin/env python
"""
Setup script for Data Analysis Toolkit
"""

from setuptools import setup, find_packages
import pathlib

# Read the contents of README file
this_directory = pathlib.Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding='utf-8')

# Read requirements
requirements = []
with open('requirements.txt', 'r') as f:
    requirements = [line.strip() for line in f if line.strip() and not line.startswith('#')]

setup(
    name="data-analysis-toolkit",
    version="1.0.0",
    author="Poorna Venkat Neelakantam",
    author_email="pvneelakantam@gmail.com",
    description="A comprehensive Python toolkit for web scraping, data cleaning, and exploratory data analysis",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/poornavenkatn08/data-analysis-toolkit",
    project_urls={
        "Bug Tracker": "https://github.com/poornavenkatn08/data-analysis-toolkit/issues",
        "Documentation": "https://github.com/poornavenkatn08/data-analysis-toolkit/docs",
        "Source Code": "https://github.com/poornavenkatn08/data-analysis-toolkit",
    },
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Internet :: WWW/HTTP :: Indexing/Search",
        "Topic :: Office/Business :: Financial :: Spreadsheet",
    ],
    python_requires=">=3.7",
    install_requires=requirements,
    extras_require={
        "dev": [
            "pytest>=6.0.0",
            "black>=21.0.0",
            "flake8>=3.9.0",
            "mypy>=0.910",
            "coverage>=5.5",
        ],
        "jupyter": [
            "jupyter>=1.0.0",
            "jupyterlab>=3.0.0",
            "ipywidgets>=7.6.0",
        ],
    },
    include_package_data=True,
    zip_safe=False,
    keywords="data analysis, web scraping, data cleaning, eda, exploratory data analysis, pandas, visualization",
)
