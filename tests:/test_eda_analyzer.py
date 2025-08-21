# tests/test_eda_analyzer.py
#!/usr/bin/env python
"""
Simple tests for EDA Analyzer
"""
import pytest
import pandas as pd
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from eda_analyzer import ComprehensiveEDA

def test_eda_init():
    """Test that EDA initializes correctly"""
    eda = ComprehensiveEDA()
    assert eda.df is None
    assert eda.figsize is not None

def test_data_overview():
    """Test data overview function"""
    eda = ComprehensiveEDA()
    # Create simple test data
    eda.df = pd.DataFrame({
        'A': [1, 2, 3],
        'B': ['x', 'y', 'z']
    })
    
    overview = eda.data_overview()
    assert 'shape' in overview
    assert overview['shape'] == (3, 2)

if __name__ == "__main__":
    pytest.main([__file__])