#!/usr/bin/env python
# coding: utf-8

# In[2]:


#!/usr/bin/env python
"""
Unit tests for the WebScraper module.
"""

import pytest
import pandas as pd
from unittest.mock import Mock, patch, MagicMock
from bs4 import BeautifulSoup
import requests
import sys
import os

# Add src directory to Python path for testing
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from webscraper import FortuneCompanyScraper


class TestFortuneCompanyScraper:
    """Test cases for FortuneCompanyScraper class."""
    
    def setup_method(self):
        """Set up test fixtures before each test method."""
        self.scraper = FortuneCompanyScraper()
    
    def test_init_creates_correct_attributes(self):
        """Test that initialization creates the correct attributes."""
        assert self.scraper.url is not None
        assert "wikipedia.org" in self.scraper.url
        assert self.scraper.headers is not None
        assert "User-Agent" in self.scraper.headers
        assert self.scraper.df is None
    
    def test_init_sets_correct_url(self):
        """Test that the correct Wikipedia URL is set."""
        expected_url = "https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue"
        assert self.scraper.url == expected_url
    
    @patch('requests.get')
    def test_fetch_webpage_success(self, mock_get):
        """Test successful webpage fetching."""
        # Mock successful response
        mock_response = Mock()
        mock_response.text = "<html><body><h1>Test</h1></body></html>"
        mock_response.raise_for_status.return_value = None
        mock_get.return_value = mock_response
        
        result = self.scraper.fetch_webpage()
        
        assert result is not None
        assert isinstance(result, BeautifulSoup)
        mock_get.assert_called_once_with(
            self.scraper.url, 
            headers=self.scraper.headers, 
            timeout=10
        )
    
    @patch('requests.get')
    def test_fetch_webpage_request_exception(self, mock_get):
        """Test webpage fetching with request exception."""
        mock_get.side_effect = requests.RequestException("Network error")
        
        result = self.scraper.fetch_webpage()
        
        assert result is None
    
    @patch('requests.get')
    def test_fetch_webpage_http_error(self, mock_get):
        """Test webpage fetching with HTTP error."""
        mock_response = Mock()
        mock_response.raise_for_status.side_effect = requests.HTTPError("404 Not Found")
        mock_get.return_value = mock_response
        
        result = self.scraper.fetch_webpage()
        
        assert result is None
    
    def test_extract_table_data_no_tables(self):
        """Test table extraction when no tables are found."""
        soup = BeautifulSoup("<html><body><p>No tables here</p></body></html>", 'html.parser')
        
        result = self.scraper.extract_table_data(soup)
        
        assert result is None
    
    def test_extract_table_data_success(self):
        """Test successful table extraction."""
        html_content = """
        <html>
            <body>
                <table class="wikitable">
                    <tr>
                        <th>Company</th>
                        <th>Revenue</th>
                        <th>Industry</th>
                    </tr>
                    <tr>
                        <td>Apple Inc.</td>
                        <td>$365,817</td>
                        <td>Technology</td>
                    </tr>
                    <tr>
                        <td>Microsoft</td>
                        <td>$198,270</td>
                        <td>Technology</td>
                    </tr>
                </table>
            </body>
        </html>
        """
        soup = BeautifulSoup(html_content, 'html.parser')
        
        result = self.scraper.extract_table_data(soup)
        
        assert result is not None
        assert isinstance(result, pd.DataFrame)
        assert len(result) == 2
        assert list(result.columns) == ['Company', 'Revenue', 'Industry']
        assert result.iloc[0]['Company'] == 'Apple Inc.'
        assert result.iloc[1]['Company'] == 'Microsoft'
    
    def test_clean_data_basic_cleaning(self):
        """Test basic data cleaning functionality."""
        # Create sample DataFrame with dirty data
        dirty_data = pd.DataFrame({
            'Company': ['Apple Inc.', 'Microsoft', None],
            'Revenue': ['$365,817', '$198,270', '$150,000'],
            'Industry': ['Technology', 'Technology', 'Finance']
        })
        
        result = self.scraper.clean_data(dirty_data)
        
        assert isinstance(result, pd.DataFrame)
        assert len(result) == 2  # NaN row should be removed
        # Revenue column should be cleaned ($ and commas removed)
        # Note: The actual cleaning logic depends on implementation
    
    def test_clean_data_empty_dataframe(self):
        """Test cleaning an empty DataFrame."""
        empty_df = pd.DataFrame()
        
        result = self.scraper.clean_data(empty_df)
        
        assert isinstance(result, pd.DataFrame)
        assert len(result) == 0
    
    @patch('os.makedirs')
    @patch('pandas.DataFrame.to_csv')
    def test_save_to_csv_success(self, mock_to_csv, mock_makedirs):
        """Test successful CSV saving."""
        df = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
        filename = "test.csv"
        
        result = self.scraper.save_to_csv(df, filename)
        
        assert result is True
        mock_makedirs.assert_called_once()
        mock_to_csv.assert_called_once()
    
    @patch('os.makedirs')
    @patch('pandas.DataFrame.to_csv')
    def test_save_to_csv_failure(self, mock_to_csv, mock_makedirs):
        """Test CSV saving failure."""
        df = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
        filename = "test.csv"
        mock_to_csv.side_effect = Exception("Write error")
        
        result = self.scraper.save_to_csv(df, filename)
        
        assert result is False
    
    def test_display_summary_no_data(self):
        """Test display summary with no data."""
        # This should not raise an exception
        self.scraper.display_summary()
        # Just verify it doesn't crash
        assert self.scraper.df is None
    
    def test_display_summary_with_data(self):
        """Test display summary with data."""
        self.scraper.df = pd.DataFrame({
            'Company': ['Apple', 'Microsoft'],
            'Revenue': [365817, 198270]
        })
        
        # This should not raise an exception
        self.scraper.display_summary()
        # Just verify it doesn't crash
        assert self.scraper.df is not None
    
    @patch.object(FortuneCompanyScraper, 'fetch_webpage')
    @patch.object(FortuneCompanyScraper, 'extract_table_data')
    @patch.object(FortuneCompanyScraper, 'clean_data')
    @patch.object(FortuneCompanyScraper, 'save_to_csv')
    def test_scrape_and_export_success(self, mock_save, mock_clean, mock_extract, mock_fetch):
        """Test complete scraping and export process."""
        # Set up mocks
        mock_soup = Mock()
        mock_fetch.return_value = mock_soup
        
        mock_df = pd.DataFrame({'Company': ['Apple'], 'Revenue': [365817]})
        mock_extract.return_value = mock_df
        mock_clean.return_value = mock_df
        mock_save.return_value = True
        
        result = self.scraper.scrape_and_export("test.csv")
        
        assert result is not None
        assert isinstance(result, pd.DataFrame)
        mock_fetch.assert_called_once()
        mock_extract.assert_called_once_with(mock_soup)
        mock_clean.assert_called_once_with(mock_df)
        mock_save.assert_called_once_with(mock_df, "test.csv")
    
    @patch.object(FortuneCompanyScraper, 'fetch_webpage')
    def test_scrape_and_export_fetch_failure(self, mock_fetch):
        """Test scraping when webpage fetch fails."""
        mock_fetch.return_value = None
        
        result = self.scraper.scrape_and_export("test.csv")
        
        assert result is None
    
    @patch.object(FortuneCompanyScraper, 'fetch_webpage')
    @patch.object(FortuneCompanyScraper, 'extract_table_data')
    def test_scrape_and_export_extract_failure(self, mock_extract, mock_fetch):
        """Test scraping when table extraction fails."""
        mock_fetch.return_value = Mock()
        mock_extract.return_value = None
        
        result = self.scraper.scrape_and_export("test.csv")
        
        assert result is None


if __name__ == "__main__":
    pytest.main([__file__])


# 
