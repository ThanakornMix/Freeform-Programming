import matplotlib.pyplot as plt
import seaborn as sns

def plot_total_emissions_by_year(df):
    """
    Plot Total CO2 Emissions by Year (2012-2022).
    :param df: Cleaned DataFrame with CO2 emissions data.
    """
    total_emissions_df = df[(df["fuelId"] == "TO") & (df["sectorId"] == "TT") & (df["stateId"] == "US")]

    # Aggregate total emissions by year
    emissions_by_year = total_emissions_df.groupby("period")["value"].sum().reset_index()

    # Plot total emissions by year
    plt.figure(figsize=(10, 6), num='Emissions by Year')
    plt.plot(emissions_by_year["period"], emissions_by_year["value"], marker='o', color='b', label='Total Emissions')
    plt.title("Total CO2 Emissions by Year (2012-2022)", fontsize=14)
    plt.xlabel("Year", fontsize=12)
    plt.ylabel("Total Emissions (Million Metric Tons of CO2)", fontsize=12)
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.7)
    for i, row in emissions_by_year.iterrows():
        plt.annotate(f'{row["value"]:.2f}', (row["period"], row["value"]), fontsize=10, ha='right', color='black')
    plt.xticks(emissions_by_year["period"], rotation=45)
    plt.tight_layout()
    plt.show()

def plot_sector_emissions_by_year(df):
    """
    Plot total CO2 emissions by sector for each year, considering special cases.
    :param df: Cleaned DataFrame with CO2 emissions data.
    """
    # Filter for rows where fuelId == "TO" and stateId == "US"
    filtered_df = df[(df["fuelId"] == "TO") & (df["stateId"] == "US")]

    # Group by year (period) and sector-name, then sum emissions
    sector_emissions = filtered_df.groupby(["period", "sector-name"])["value"].sum().reset_index()

    # Pivot the data to have years as rows and sectors as columns
    pivot_data = sector_emissions.pivot(index="period", columns="sector-name", values="value")

    # Plot the data
    plt.figure(figsize=(12, 8))
    for sector in pivot_data.columns:
        plt.plot(pivot_data.index, pivot_data[sector], marker='o', label=sector)

    # Customize the plot
    plt.title("Total CO2 Emissions by Sector and Year (2012-2022)", fontsize=16)
    plt.xlabel("Year", fontsize=14)
    plt.ylabel("Total Emissions (Million Metric Tons of CO2)", fontsize=14)
    plt.xticks(pivot_data.index, rotation=45)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend(title="Sector", fontsize=12)
    plt.tight_layout()
    plt.show()