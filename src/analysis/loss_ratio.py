import pandas as pd
import numpy as np

def load_and_clean_data(file_path):
    """
    Load and clean the insurance data.
    
    Args:
        file_path (str): Path to the data file
        
    Returns:
        pd.DataFrame: Cleaned dataframe
    """
    # Read the data
    df = pd.read_csv(file_path)
    
    # Basic cleaning
    # Remove any duplicate rows
    df = df.drop_duplicates()
    
    # Handle missing values
    numeric_columns = df.select_dtypes(include=[np.number]).columns
    df[numeric_columns] = df[numeric_columns].fillna(df[numeric_columns].mean())
    
    categorical_columns = df.select_dtypes(include=['object']).columns
    df[categorical_columns] = df[categorical_columns].fillna(df[categorical_columns].mode().iloc[0])
    
    return df

def calculate_loss_ratio_by_group(df, group_column):
    """
    Calculate loss ratio for different groups.
    
    Args:
        df (pd.DataFrame): Input dataframe
        group_column (str): Column to group by
        
    Returns:
        pd.Series: Loss ratio by group
    """
    grouped = df.groupby(group_column).agg({
        'TotalClaims': 'sum',
        'TotalPremium': 'sum'
    })
    
    return grouped['TotalClaims'] / grouped['TotalPremium']

def plot_loss_ratio(loss_ratios, title, overall_ratio=None):
    """
    Plot loss ratios with optional overall ratio line.
    
    Args:
        loss_ratios (pd.Series): Loss ratios to plot
        title (str): Plot title
        overall_ratio (float, optional): Overall portfolio ratio
    """
    import matplotlib.pyplot as plt
    
    plt.figure(figsize=(10, 6))
    loss_ratios.sort_values().plot(kind='bar')
    plt.title(title)
    plt.ylabel('Loss Ratio')
    
    if overall_ratio is not None:
        plt.axhline(y=overall_ratio, color='r', linestyle='--', label='Portfolio Average')
        plt.legend()
    
    plt.tight_layout()
    plt.show() 