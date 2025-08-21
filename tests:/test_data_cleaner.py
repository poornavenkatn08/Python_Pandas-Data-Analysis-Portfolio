#!/usr/bin/env python
"""
tests/test_data_cleaner.py
Simple tests for DataCleaner
"""
import pytest
import pandas as pd
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from data_cleaner import CustomerDataCleaner

def test_cleaner_init():
    """Test that cleaner initializes correctly"""
    cleaner = CustomerDataCleaner()
    assert cleaner.df is None
    assert cleaner.cleaning_report is not None

def test_remove_duplicates():
    """Test duplicate removal"""
    cleaner = CustomerDataCleaner()
    # Create test data with duplicates
    test_data = pd.DataFrame({
        'Name': ['John', 'Jane', 'John'],
        'Phone': ['123', '456', '123']
    })
    cleaner.df = test_data
    cleaner.remove_duplicates()
    
    assert len(cleaner.df) == 2  # Should remove 1 duplicate

if __name__ == "__main__":
    pytest.main([__file__])