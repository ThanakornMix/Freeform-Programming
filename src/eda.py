import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy import stats

def perform_eda(df):
    """
    Perform exploratory data analysis (EDA).
    :param df: Cleaned DataFrame.
    :return: None
    """
    # 1. Total emissions by year (trends over time)
    emissions_by_year = df.groupby('period')['value'].sum()
    print("\nEmissions by Year:")
    print(emissions_by_year)

    # Create a new figure for emissions by year
    plt.figure(figsize=(10,6), num='Emissions by Year')
    emissions_by_year.plot(kind='line', marker='o', linestyle='-', color='b')
    plt.title('Total CO2 Emissions by Year (2012-2022)')
    plt.xlabel('Year')
    plt.ylabel('CO2 Emissions')
    plt.grid(True)

    # 2. Emissions by Sector (comparison)
    emissions_by_sector = df.groupby('sector-name')['value'].sum()
    print("\nEmissions by Sector:")
    print(emissions_by_sector)

    # Create a new figure for emissions by sector
    plt.figure(2, figsize=(10,6))
    emissions_by_sector.plot(kind='bar', color='c')
    plt.title('Total CO2 Emissions by Sector (2012-2022)')
    plt.xlabel('Sector')
    plt.ylabel('CO2 Emissions')
    plt.xticks(rotation=45)

    # 3. Emissions by Fuel Type (comparison)
    emissions_by_fuel = df.groupby('fuel-name')['value'].sum()
    print("\nEmissions by Fuel Type:")
    print(emissions_by_fuel)

    # Create a new figure for emissions by fuel type
    plt.figure(3, figsize=(10,6))
    emissions_by_fuel.plot(kind='bar', color='m')
    plt.title('Total CO2 Emissions by Fuel Type (2012-2022)')
    plt.xlabel('Fuel Type')
    plt.ylabel('CO2 Emissions')
    plt.xticks(rotation=45)

    # 4. Emissions by State (distribution)
    emissions_by_state = df.groupby('state-name')['value'].sum()
    print("\nEmissions by State:")
    print(emissions_by_state)

    # Create a new figure for emissions by state
    plt.figure(4, figsize=(10,6))
    emissions_by_state.plot(kind='bar', color='g')
    plt.title('Total CO2 Emissions by State (2012-2022)')
    plt.xlabel('State')
    plt.ylabel('CO2 Emissions')
    plt.xticks(rotation=90)

def plot_distribution(df):
    """
    Plot distribution of emissions across different categories.
    :param df: Cleaned DataFrame.
    :return: None
    """
    # 1. Emissions distribution by Sector (boxplot)
    plt.figure(5, figsize=(10,6))
    sns.boxplot(x='sector-name', y='value', data=df)
    plt.title('Distribution of CO2 Emissions by Sector')
    plt.xlabel('Sector')
    plt.ylabel('CO2 Emissions')
    plt.xticks(rotation=45)

    # 2. Emissions distribution by Fuel Type (boxplot)
    plt.figure(6, figsize=(10,6))
    sns.boxplot(x='fuel-name', y='value', data=df)
    plt.title('Distribution of CO2 Emissions by Fuel Type')
    plt.xlabel('Fuel Type')
    plt.ylabel('CO2 Emissions')
    plt.xticks(rotation=45)

    # 3. Emissions distribution by State (boxplot)
    plt.figure(7, figsize=(10,6))
    sns.boxplot(x='state-name', y='value', data=df)
    plt.title('Distribution of CO2 Emissions by State')
    plt.xlabel('State')
    plt.ylabel('CO2 Emissions')
    plt.xticks(rotation=90)

def detect_outliers(df):
    """
    Detect and visualize outliers in the emissions data.
    :param df: Cleaned DataFrame.
    :return: None
    """
    # Calculate Z-score for outlier detection
    z_scores = stats.zscore(df['value'])
    abs_z_scores = np.abs(z_scores)
    outliers = (abs_z_scores > 3)

    # Plot outliers
    outlier_data = df[outliers]
    print("\nOutliers Detected:")
    print(outlier_data)

    # Create a new figure for outlier detection
    plt.figure(8, figsize=(10,6))
    sns.boxplot(x=df['value'])
    plt.title('Outlier Detection in CO2 Emissions')

# To display all plots together
def show_all_plots():
    plt.show()

