import pandas as pd
from api_data_fetcher import fetch_all_data  # Import the function from your api_data_fetcher.py

def inspect_data(data):
    """
    Inspect the data types, missing values and summary statistics.
    :param data: DataFrame to inspect.
    :return: None
    """

    df = pd.DataFrame(data)
    # Display data types of each column
    print("\nData Types:")
    print(df.dtypes)
    
    # Check for missing values
    print("\nMissing Values:")
    print(df.isnull().sum())
    
    # Display summary statistics for numerical columns
    print("\nSummary Statistics:")
    print(df.describe())
