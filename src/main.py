from api_data_fetcher import fetch_all_data  # Import the fetch function from data_fetcher.py
from collection_data import save_data_to_csv  # Import the save function from data_collection.py
from process_data import process_api_data # Improt the inspect function from process_data
from eda import perform_eda, plot_distribution, detect_outliers, show_all_plots

def main():
    frequency = "annual"
    start_year = 2012 # start year
    end_year = 2022  # end year
    max_records = 60000 # max rows 

    # Fetch all data using the function from data_fetcher.py
    all_data = fetch_all_data(frequency, start_year, end_year, max_records)

    # save data to csv
    if all_data:
        output_file = "co2_emissions_2012_2022.csv"
        # save_data_to_csv(all_data, output_file)
    else:
        print("No data fetched.")

    if all_data:
        cleaned_data = process_api_data(all_data, start_year, end_year)
        """
        Uncomment to save cleaned data to CSV
        """
        # cleaned_output_file = "cleaned_co2_emissions_2012_2022.csv"
        # cleaned_data.to_csv(cleaned_output_file, index=False)
        # print(f"Cleaned data saved to '{cleaned_output_file}'.")
    else:
        print("Clean Error")
    
    """
    Perform Exploratory Data Analysis (EDA)
    EDA is used to:
    1. Understand the data's structure and identify key patterns and trends.
    2. Explore relationships between variables (e.g., emissions by year, sector, fuel type, state).
    3. Detect anomalies or outliers in the data that might affect analysis.
    4. Generate visual insights such as distributions and correlations that can guide further analysis or model building.
    5. Summarize statistical metrics like mean, median, standard deviation to understand data characteristics.
    UNCOMMENT FOR ILLUSTRATION
    """
    # if all_data:
    #     # Perform EDA
    #     perform_eda(cleaned_data)
    #     plot_distribution(cleaned_data)
    #     detect_outliers(cleaned_data)
    #     show_all_plots()
    # else:
    #     print("EDA Error")

# Run the main function
if __name__ == "__main__":
    main()

