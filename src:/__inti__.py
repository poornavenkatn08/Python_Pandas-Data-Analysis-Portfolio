#!/usr/bin/env python
# coding: utf-8

# In[3]:


"""
Data Analysis Toolkit

A comprehensive Python toolkit for web scraping, data cleaning, 
and exploratory data analysis.
"""

__version__ = "1.0.0"
__author__ = "Poorna Venkat Neelakantam"
__email__ = "pvneelakantam@gmail.com"

from .webscraper import FortuneCompanyScraper
from .data_cleaner import CustomerDataCleaner
from .eda_analyzer import ComprehensiveEDA

__all__ = [
    "FortuneCompanyScraper",
    "CustomerDataCleaner", 
    "ComprehensiveEDA"
]


# 
