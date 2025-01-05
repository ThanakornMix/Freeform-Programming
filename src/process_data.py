import pandas as pd
from api_data_fetcher import fetch_all_data 

def inspect_data(data):
    """
    Inspect the data types, missing values, and summary statistics.
    :param data: DataFrame to inspect.
    :return: None
    """
    df = pd.DataFrame(data)
    print("\nData Types:")
    print(df.dtypes)

    print("\nMissing Values:")
    print(df.isnull().sum())

    print("\nSummary Statistics:")
    print(df.describe())

def clean_missing_values(df):
    """
    Handle missing values in the dataset.
    :param df: DataFrame to clean.
    :return: DataFrame after handling missing values.
    """
    print("\nHandling Missing Values...")
    # Drop rows with missing critical 'value'
    df = df.dropna(subset=['value'])

    # Fill missing 'state-name' with a placeholder
    df['state-name'] = df['state-name'].fillna('Unknown')
    return df

def handle_duplicates(df):
    """
    Remove duplicate rows from the dataset.
    :param df: DataFrame to clean.
    :return: DataFrame without duplicates.
    """
    print("\nChecking for Duplicates...")
    duplicates_count = df.duplicated().sum()
    print(f"Number of duplicate rows: {duplicates_count}")
    df = df.drop_duplicates()
    return df

def validate_data_types(df):
    """
    Validate and correct data types for consistency.
    :param df: DataFrame to validate.
    :return: DataFrame with correct data types.
    """
    print("\nValidating Data Types...")
    # Ensure 'value' is numeric
    df['value'] = pd.to_numeric(df['value'], errors='coerce')

    # Ensure categorical columns are strings
    for col in ['sector-name', 'fuel-name', 'state-name']:
        df[col] = df[col].astype(str)
    return df

def standardize_categorical_data(df):
    """
    Standardize formatting for categorical columns.
    :param df: DataFrame to clean.
    :return: DataFrame with standardized categories.
    """
    print("\nStandardizing Categorical Data...")
    for col in ['sector-name', 'fuel-name', 'state-name']:
        df[col] = df[col].str.strip().str.title()  # Remove extra spaces and capitalize each word
    return df

def filter_invalid_data(df):
    """
    Remove rows with invalid or nonsensical values.
    :param df: DataFrame to clean.
    :return: DataFrame after filtering invalid data.
    """
    print("\nFiltering Invalid Data...")
    # Remove rows with negative values in 'value'
    invalid_count = (df['value'] < 0).sum()
    print(f"Number of rows with negative 'value': {invalid_count}")
    df = df[df['value'] >= 0]
    return df


def process_api_data(data, start_year, end_year):
    """
    Process and clean the API data.
    :param data: The raw data fetched from the API.
    :param start_year: Starting year of the data range.
    :param end_year: Ending year of the data range.
    :return: Cleaned DataFrame.
    """
    print("\n--- Data Inspection ---")
    inspect_data(data)

    print("\n--- Cleaning Data ---")
    df = pd.DataFrame(data)

    # Step 1: Handle Missing Values
    df = clean_missing_values(df)

    # Step 2: Remove Duplicates
    df = handle_duplicates(df)

    # Step 3: Validate Data Types
    df = validate_data_types(df)

    # Step 4: Standardize Categorical Data
    df = standardize_categorical_data(df)

    # Step 5: Filter Out Invalid Data
    df = filter_invalid_data(df)

    print(f"\nData successfully cleaned and processed for the period {start_year}-{end_year}.")
    
    return df
