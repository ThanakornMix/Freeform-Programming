import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

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
    # Filter for rows 
    filtered_df = df[(df["fuelId"] == "TO") & (df["stateId"] == "US") & (df["sectorId"] != "TT")]

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
    plt.legend(title="Sector", fontsize=12, bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
    plt.tight_layout()
    plt.show()

def plot_fuel_emissions(df):
    """
    Plot a pie chart showing the average percentage of total CO2 emissions by fuel type over the entire decade (2012-2022).
    :param df: Cleaned DataFrame with CO2 emissions data.
    """
    # Filter data for total emissions 
    filtered_df = df[(df["stateId"] == "US") & (df["sectorId"] == "TT") & (df["fuelId"] != "TO")]

    # Group by fuel-name and sum emissions over the decade
    fuel_emissions = filtered_df.groupby("fuel-name")["value"].sum()

    # Calculate the percentage contribution of each fuel type
    fuel_emissions_percentage = (fuel_emissions / fuel_emissions.sum()) * 100

    # Plot the pie chart
    plt.figure(figsize=(8, 8))
    plt.pie(fuel_emissions_percentage, labels=fuel_emissions_percentage.index, 
            autopct='%1.1f%%', startangle=140, colors=sns.color_palette('pastel'))
    plt.title("Average Percentage of CO2 Emissions by Fuel Type (2012-2022)", fontsize=16)
    plt.show()

def plot_stacked_bar_emissions_by_sector_and_fuel(df):
    """
    Plot a stacked bar chart showing CO2 emissions by sector and fuel type for each year.
    :param df: Cleaned DataFrame with CO2 emissions data.
    """
    # Filter data for total emissions across all states 
    filtered_df = df[(df["stateId"] == "US") & (df["sectorId"] != "TT") & (df["fuelId"] != "TO")]

    # Group by year, sector, and fuel, then sum emissions
    grouped = filtered_df.groupby(["period", "sector-name", "fuel-name"])["value"].sum().reset_index()

    # Pivot to create a matrix with years as rows and (sector, fuel) as columns
    pivot_data = grouped.pivot_table(index="period", columns=["sector-name", "fuel-name"], values="value", aggfunc='sum', fill_value=0)

    # Plot stacked bar chart
    plt.figure(figsize=(14, 8))
    bottom = None
    for (sector, fuel), values in pivot_data.items():
        if bottom is None:
            bottom = values
            plt.bar(pivot_data.index, values, label=f"{sector} - {fuel}")
        else:
            plt.bar(pivot_data.index, values, bottom=bottom, label=f"{sector} - {fuel}")
            bottom += values

    # Customize the plot
    plt.title("Stacked Bar Chart of CO2 Emissions by Sector and Fuel Type (2012-2022)", fontsize=16)
    plt.xlabel("Year", fontsize=14)
    plt.ylabel("CO2 Emissions (Million Metric Tons)", fontsize=14)
    plt.xticks(pivot_data.index, rotation=45)
    plt.legend(title="Sector - Fuel", bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()

def plot_emissions_stripplot(df):
    """
    Create a strip plot with CO2 emissions (value) on the y-axis and year (period) on the x-axis.
    :param df: Cleaned DataFrame with CO2 emissions data.
    """
    # Filter the data 
    filtered_df = df[(df["stateId"] != "US") & (df["sectorId"] != "TT") & (df["fuelId"] != "TO")]

    # Sort the data by period (year) in ascending order
    filtered_df = filtered_df.sort_values(by="period", ascending=True)

    # Create the strip plot
    plt.figure(figsize=(12, 8))
    sns.stripplot(x="period", y="value", data=filtered_df, hue="period", jitter=True, size=6, 
                  palette="Set2", alpha=0.7, dodge=False, legend=False)

    # Customize the plot
    plt.title("CO2 Emissions Distribution by Year", fontsize=16, fontweight='bold')
    plt.xlabel("Year", fontsize=14)
    plt.ylabel("CO2 Emissions (Million Metric Tons)", fontsize=14)
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()


def plot_geographical_distribution(df):
    """
    Create an animated geographical map of CO2 emissions by state over the years (2012-2022).
    Excludes rows where sectorId == 'TT' and fuelId == 'TO'.
    
    :param df: DataFrame with CO2 emissions per state.
    """
    # filter rows
    filtered_data = df[(df["sectorId"] != "TT") & (df["fuelId"] != "TO") & (df["stateId"] != "US")]

    # Map full state names to abbreviations
    state_abbreviations = {
        'Alabama': 'AL', 'Alaska': 'AK', 'Arizona': 'AZ', 'Arkansas': 'AR', 'California': 'CA',
        'Colorado': 'CO', 'Connecticut': 'CT', 'Delaware': 'DE', 'Florida': 'FL', 'Georgia': 'GA',
        'Hawaii': 'HI', 'Idaho': 'ID', 'Illinois': 'IL', 'Indiana': 'IN', 'Iowa': 'IA',
        'Kansas': 'KS', 'Kentucky': 'KY', 'Louisiana': 'LA', 'Maine': 'ME', 'Maryland': 'MD',
        'Massachusetts': 'MA', 'Michigan': 'MI', 'Minnesota': 'MN', 'Mississippi': 'MS',
        'Missouri': 'MO', 'Montana': 'MT', 'Nebraska': 'NE', 'Nevada': 'NV', 'New Hampshire': 'NH',
        'New Jersey': 'NJ', 'New Mexico': 'NM', 'New York': 'NY', 'North Carolina': 'NC',
        'North Dakota': 'ND', 'Ohio': 'OH', 'Oklahoma': 'OK', 'Oregon': 'OR', 'Pennsylvania': 'PA',
        'Rhode Island': 'RI', 'South Carolina': 'SC', 'South Dakota': 'SD', 'Tennessee': 'TN',
        'Texas': 'TX', 'Utah': 'UT', 'Vermont': 'VT', 'Virginia': 'VA', 'Washington': 'WA',
        'West Virginia': 'WV', 'Wisconsin': 'WI', 'Wyoming': 'WY'
    }
    
    # Map state-name to abbreviations
    filtered_data['state-abbrev'] = filtered_data['state-name'].map(state_abbreviations)

    # Aggregate emissions by year and state abbreviation
    state_emissions = filtered_data.groupby(["period", "state-abbrev"])["value"].sum().reset_index()

    # fixed range for the color scale
    max_emissions = state_emissions["value"].max()
    min_emissions = state_emissions["value"].min()

    # Create an animated choropleth map
    fig = px.choropleth(
        state_emissions,
        locations="state-abbrev",
        locationmode="USA-states",
        color="value",
        color_continuous_scale="OrRd",
        scope="usa",
        range_color=[min_emissions, max_emissions], 
        animation_frame="period",
        labels={"value": "CO2 Emissions (Million Metric Tons)"},
        title="Geographical Distribution of CO2 Emissions by State (2012-2022)"
    )

    fig.show()

def show_all_graphs(df):
    """
    Display all the graphs for CO2 emissions analysis simultaneously.
    :param df: Cleaned DataFrame with CO2 emissions data.
    """
    print("Plot 1: Total CO2 Emissions by Year")
    plot_total_emissions_by_year(df)

    print("\nPlot 2: Total CO2 Emissions by Sector and Year")
    plot_sector_emissions_by_year(df)

    print("\nPlot 3: Average Percentage of CO2 Emissions by Fuel Type")
    plot_fuel_emissions(df)

    print("\nPlot 4: Stacked Bar Chart of CO2 Emissions by Sector and Fuel Type")
    plot_stacked_bar_emissions_by_sector_and_fuel(df)

    print("\nPlot 5: Strip Plot of CO2 Emissions Distribution by Year")
    plot_emissions_stripplot(df)

    print("\nPlot 6: Animated Geographical Distribution of CO2 Emissions by State")
    plot_geographical_distribution(df)

