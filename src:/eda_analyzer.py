#!/usr/bin/env python
"""
Comprehensive Exploratory Data Analysis (EDA)

This script provides a complete EDA framework for analyzing datasets with
statistical summaries, correlation analysis, and professional visualizations.

Author: Poorna Venkat Neelakantam
Dependencies: pandas, seaborn, matplotlib, numpy
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from typing import Dict, List, Optional, Tuple
import warnings
import logging
from pathlib import Path

# Configure settings
warnings.filterwarnings('ignore')
plt.style.use('seaborn-v0_8')
pd.set_option('display.float_format', '{:.2f}'.format)
pd.set_option('display.max_columns', None)

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class ComprehensiveEDA:
    """
    A comprehensive Exploratory Data Analysis toolkit.
    
    This class provides methods for statistical analysis, visualization,
    and data quality assessment with professional reporting capabilities.
    """
    
    def __init__(self, figsize: Tuple[int, int] = (12, 8)):
        """
        Initialize the EDA analyzer.
        
        Args:
            figsize (Tuple[int, int]): Default figure size for plots
        """
        self.df = None
        self.figsize = figsize
        self.analysis_results = {}
        
        # Set matplotlib parameters
        plt.rcParams['figure.figsize'] = self.figsize
        plt.rcParams['font.size'] = 10
        sns.set_palette("husl")
    
    def load_data(self, filepath: str, **kwargs) -> bool:
        """
        Load data from various file formats.
        
        Args:
            filepath (str): Path to the data file
            **kwargs: Additional arguments for pandas read functions
            
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            file_path = Path(filepath)
            
            if file_path.suffix.lower() == '.csv':
                self.df = pd.read_csv(filepath, **kwargs)
            elif file_path.suffix.lower() in ['.xlsx', '.xls']:
                self.df = pd.read_excel(filepath, **kwargs)
            elif file_path.suffix.lower() == '.json':
                self.df = pd.read_json(filepath, **kwargs)
            else:
                raise ValueError(f"Unsupported file format: {file_path.suffix}")
            
            logger.info(f"Successfully loaded data: {self.df.shape[0]} rows, {self.df.shape[1]} columns")
            return True
            
        except Exception as e:
            logger.error(f"Failed to load data: {e}")
            return False
    
    def data_overview(self) -> Dict:
        """
        Generate comprehensive data overview.
        
        Returns:
            Dict: Dictionary containing overview statistics
        """
        if self.df is None:
            logger.error("No data loaded")
            return {}
        
        overview = {
            'shape': self.df.shape,
            'memory_usage_mb': self.df.memory_usage(deep=True).sum() / 1024**2,
            'column_types': self.df.dtypes.value_counts().to_dict(),
            'missing_values': self.df.isnull().sum().sum(),
            'duplicate_rows': self.df.duplicated().sum(),
            'unique_values_per_column': self.df.nunique().to_dict()
        }
        
        self.analysis_results['overview'] = overview
        
        print("="*60)
        print("DATASET OVERVIEW")
        print("="*60)
        print(f"Shape: {overview['shape'][0]} rows × {overview['shape'][1]} columns")
        print(f"Memory Usage: {overview['memory_usage_mb']:.2f} MB")
        print(f"Missing Values: {overview['missing_values']}")
        print(f"Duplicate Rows: {overview['duplicate_rows']}")
        print(f"Data Types: {overview['column_types']}")
        
        return overview
    
    def missing_value_analysis(self) -> None:
        """Analyze and visualize missing values."""
        if self.df is None:
            logger.error("No data loaded")
            return
        
        missing_stats = self.df.isnull().sum()
        missing_percent = (missing_stats / len(self.df)) * 100
        
        missing_df = pd.DataFrame({
            'Missing_Count': missing_stats,
            'Missing_Percentage': missing_percent
        }).sort_values('Missing_Count', ascending=False)
        
        # Filter columns with missing values
        missing_df = missing_df[missing_df['Missing_Count'] > 0]
        
        if len(missing_df) == 0:
            print("✅ No missing values found in the dataset!")
            return
        
        print("\nMISSING VALUES ANALYSIS")
        print("-" * 40)
        print(missing_df)
        
        # Visualize missing values
        if len(missing_df) > 0:
            fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
            
            # Bar plot of missing values
            missing_df['Missing_Count'].plot(kind='bar', ax=ax1, color='coral')
            ax1.set_title('Missing Values by Column')
            ax1.set_ylabel('Count')
            ax1.tick_params(axis='x', rotation=45)
            
            # Percentage plot
            missing_df['Missing_Percentage'].plot(kind='bar', ax=ax2, color='lightblue')
            ax2.set_title('Missing Values Percentage by Column')
            ax2.set_ylabel('Percentage (%)')
            ax2.tick_params(axis='x', rotation=45)
            
            plt.tight_layout()
            plt.show()
    
    def statistical_summary(self) -> None:
        """Generate comprehensive statistical summary."""
        if self.df is None:
            logger.error("No data loaded")
            return
        
        print("\nSTATISTICAL SUMMARY")
        print("-" * 40)
        
        # Numerical columns summary
        numeric_cols = self.df.select_dtypes(include=[np.number]).columns
        if len(numeric_cols) > 0:
            print("\nNumerical Columns:")
            print(self.df[numeric_cols].describe())
            
            # Additional statistics
            print("\nAdditional Statistics:")
            additional_stats = pd.DataFrame({
                'Skewness': self.df[numeric_cols].skew(),
                'Kurtosis': self.df[numeric_cols].kurtosis()
            })
            print(additional_stats)
        
        # Categorical columns summary
        categorical_cols = self.df.select_dtypes(include=['object', 'category']).columns
        if len(categorical_cols) > 0:
            print("\nCategorical Columns Summary:")
            for col in categorical_cols:
                print(f"\n{col}:")
                value_counts = self.df[col].value_counts().head(10)
                print(value_counts)
    
    def correlation_analysis(self) -> None:
        """Perform and visualize correlation analysis."""
        if self.df is None:
            logger.error("No data loaded")
            return
        
        numeric_cols = self.df.select_dtypes(include=[np.number]).columns
        
        if len(numeric_cols) < 2:
            print("⚠️ Need at least 2 numerical columns for correlation analysis")
            return
        
        # Calculate correlation matrix
        correlation_matrix = self.df[numeric_cols].corr()
        
        print("\nCORRELATION ANALYSIS")
        print("-" * 40)
        print(correlation_matrix)
        
        # Create correlation heatmap
        plt.figure(figsize=(12, 10))
        mask = np.triu(np.ones_like(correlation_matrix, dtype=bool))
        
        sns.heatmap(
            correlation_matrix,
            annot=True,
            cmap='RdBu_r',
            center=0,
            square=True,
            mask=mask,
            cbar_kws={"shrink": .8},
            fmt='.2f'
        )
        plt.title('Correlation Matrix Heatmap')
        plt.tight_layout()
        plt.show()
        
        # Find strong correlations
        strong_correlations = []
        for i in range(len(correlation_matrix.columns)):
            for j in range(i+1, len(correlation_matrix.columns)):
                corr_value = correlation_matrix.iloc[i, j]
                if abs(corr_value) > 0.7:  # Strong correlation threshold
                    strong_correlations.append((
                        correlation_matrix.columns[i],
                        correlation_matrix.columns[j],
                        corr_value
                    ))
        
        if strong_correlations:
            print("\nSTRONG CORRELATIONS (|r| > 0.7):")
            for col1, col2, corr in strong_correlations:
                print(f"{col1} - {col2}: {corr:.3f}")
    
    def distribution_analysis(self) -> None:
        """Analyze and visualize distributions of numerical variables."""
        if self.df is None:
            logger.error("No data loaded")
            return
        
        numeric_cols = self.df.select_dtypes(include=[np.number]).columns
        
        if len(numeric_cols) == 0:
            print("⚠️ No numerical columns found for distribution analysis")
            return
        
        n_cols = min(3, len(numeric_cols))
        n_rows = (len(numeric_cols) + n_cols - 1) // n_cols
        
        fig, axes = plt.subplots(n_rows, n_cols, figsize=(15, 5*n_rows))
        if n_rows == 1:
            axes = [axes] if n_cols == 1 else axes
        else:
            axes = axes.flatten()
        
        for i, col in enumerate(numeric_cols):
            if i < len(axes):
                # Histogram with KDE
                sns.histplot(data=self.df, x=col, kde=True, ax=axes[i])
                axes[i].set_title(f'Distribution of {col}')
                axes[i].grid(True, alpha=0.3)
        
        # Hide empty subplots
        for i in range(len(numeric_cols), len(axes)):
            axes[i].set_visible(False)
        
        plt.tight_layout()
        plt.show()
    
    def outlier_analysis(self) -> None:
        """Identify and visualize outliers using boxplots and IQR method."""
        if self.df is None:
            logger.error("No data loaded")
            return
        
        numeric_cols = self.df.select_dtypes(include=[np.number]).columns
        
        if len(numeric_cols) == 0:
            print("⚠️ No numerical columns found for outlier analysis")
            return
        
        print("\nOUTLIER ANALYSIS")
        print("-" * 40)
        
        outlier_summary = []
        
        # Box plots
        n_cols = min(3, len(numeric_cols))
        n_rows = (len(numeric_cols) + n_cols - 1) // n_cols
        
        fig, axes = plt.subplots(n_rows, n_cols, figsize=(15, 5*n_rows))
        if n_rows == 1:
            axes = [axes] if n_cols == 1 else axes
        else:
            axes = axes.flatten()
        
        for i, col in enumerate(numeric_cols):
            if i < len(axes):
                # Boxplot
                sns.boxplot(data=self.df, y=col, ax=axes[i])
                axes[i].set_title(f'Boxplot of {col}')
                axes[i].grid(True, alpha=0.3)
                
                # Calculate IQR outliers
                Q1 = self.df[col].quantile(0.25)
                Q3 = self.df[col].quantile(0.75)
                IQR = Q3 - Q1
                lower_bound = Q1 - 1.5 * IQR
                upper_bound = Q3 + 1.5 * IQR
                
                outliers = self.df[(self.df[col] < lower_bound) | (self.df[col] > upper_bound)][col]
                outlier_summary.append({
                    'Column': col,
                    'Outliers_Count': len(outliers),
                    'Outliers_Percentage': (len(outliers) / len(self.df)) * 100,
                    'Lower_Bound': lower_bound,
                    'Upper_Bound': upper_bound
                })
        
        # Hide empty subplots
        for i in range(len(numeric_cols), len(axes)):
            axes[i].set_visible(False)
        
        plt.tight_layout()
        plt.show()
        
        # Print outlier summary
        outlier_df = pd.DataFrame(outlier_summary)
        print("\nOutlier Summary (IQR Method):")
        print(outlier_df)
    
    def categorical_analysis(self) -> None:
        """Analyze categorical variables with value counts and visualizations."""
        if self.df is None:
            logger.error("No data loaded")
            return
        
        categorical_cols = self.df.select_dtypes(include=['object', 'category']).columns
        
        if len(categorical_cols) == 0:
            print("⚠️ No categorical columns found")
            return
        
        print("\nCATEGORICAL ANALYSIS")
        print("-" * 40)
        
        for col in categorical_cols[:5]:  # Limit to first 5 columns
            print(f"\n{col} - Unique Values: {self.df[col].nunique()}")
            
            value_counts = self.df[col].value_counts()
            print(value_counts.head(10))
            
            # Create visualization if reasonable number of categories
            if 2 <= self.df[col].nunique() <= 20:
                plt.figure(figsize=(10, 6))
                
                if self.df[col].nunique() <= 10:
                    # Bar plot for few categories
                    value_counts.head(10).plot(kind='bar', color='skyblue')
                    plt.title(f'Distribution of {col}')
                    plt.xticks(rotation=45)
                else:
                    # Horizontal bar plot for more categories
                    value_counts.head(10).plot(kind='barh', color='lightcoral')
                    plt.title(f'Top 10 Categories in {col}')
                
                plt.tight_layout()
                plt.show()
    
    def generate_comprehensive_report(self, save_path: Optional[str] = None) -> str:
        """
        Generate a comprehensive EDA report.
        
        Args:
            save_path (str, optional): Path to save the report
            
        Returns:
            str: Formatted report
        """
        if self.df is None:
            return "No data loaded for analysis"
        
        report = []
        report.append("="*80)
        report.append("COMPREHENSIVE EXPLORATORY DATA ANALYSIS REPORT")
        report.append("="*80)
        report.append(f"Generated on: {pd.Timestamp.now().strftime('%Y-%m-%d %H:%M:%S')}")
        report.append(f"Dataset: {self.df.shape[0]} rows × {self.df.shape[1]} columns")
        
        # Data quality summary
        report.append("\n" + "="*50)
        report.append("DATA QUALITY SUMMARY")
        report.append("="*50)
        report.append(f"Missing values: {self.df.isnull().sum().sum()}")
        report.append(f"Duplicate rows: {self.df.duplicated().sum()}")
        report.append(f"Memory usage: {self.df.memory_usage(deep=True).sum() / 1024**2:.2f} MB")
        
        # Column information
        report.append("\n" + "="*50)
        report.append("COLUMN INFORMATION")
        report.append("="*50)
        
        for col in self.df.columns:
            dtype = str(self.df[col].dtype)
            unique_count = self.df[col].nunique()
            missing_count = self.df[col].isnull().sum()
            missing_pct = (missing_count / len(self.df)) * 100
            
            report.append(f"{col}:")
            report.append(f"  - Type: {dtype}")
            report.append(f"  - Unique values: {unique_count}")
            report.append(f"  - Missing: {missing_count} ({missing_pct:.1f}%)")
        
        # Statistical insights
        numeric_cols = self.df.select_dtypes(include=[np.number]).columns
        if len(numeric_cols) > 0:
            report.append("\n" + "="*50)
            report.append("KEY STATISTICAL INSIGHTS")
            report.append("="*50)
            
            for col in numeric_cols:
                report.append(f"\n{col}:")
                report.append(f"  - Mean: {self.df[col].mean():.2f}")
                report.append(f"  - Median: {self.df[col].median():.2f}")
                report.append(f"  - Std Dev: {self.df[col].std():.2f}")
                report.append(f"  - Skewness: {self.df[col].skew():.2f}")
        
        report_text = "\n".join(report)
        
        if save_path:
            try:
                with open(save_path, 'w') as f:
                    f.write(report_text)
                logger.info(f"Report saved to: {save_path}")
            except Exception as e:
                logger.error(f"Failed to save report: {e}")
        
        return report_text
    
    def run_complete_eda(self) -> None:
        """Run the complete EDA pipeline with all analyses."""
        if self.df is None:
            logger.error("No data loaded")
            return
        
        print("🔍 Starting Comprehensive EDA Pipeline...")
        print("=" * 60)
        
        # Run all analyses
        self.data_overview()
        self.missing_value_analysis()
        self.statistical_summary()
        self.distribution_analysis()
        self.correlation_analysis()
        self.outlier_analysis()
        self.categorical_analysis()
        
        print("\n" + "="*60)
        print("✅ EDA Pipeline Completed!")
        print("="*60)


def main():
    """Main function to demonstrate the EDA toolkit."""
    # Initialize EDA analyzer
    eda = ComprehensiveEDA(figsize=(12, 8))
    
    # Example usage - replace with your data file
    data_file = "data/countries-table.csv"  # Update this path
    
    if eda.load_data(data_file):
        # Run complete EDA
        eda.run_complete_eda()
        
        # Generate and save comprehensive report
        report = eda.generate_comprehensive_report("eda_report.txt")
        print("\n📊 Analysis completed successfully!")
        print("📄 Detailed report saved as 'eda_report.txt'")
    else:
        print("❌ Failed to load data. Please check the file path.")


if __name__ == "__main__":
    main()
