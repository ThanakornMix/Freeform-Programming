from api_data_fetcher import fetch_all_data  # Import the fetch function from data_fetcher.py
from collection_data import save_data_to_csv  # Import the save function from data_collection.py
from process_data import process_api_data  # Import the inspect function from process_data.py
from eda import perform_eda, plot_distribution, detect_outliers, show_all_plots
from visualization import show_all_graphs

SAVE_GRAPHS = False # save all visualization (optional, Chnage to True to save)

def main():
    # Configuration for data fetching
    frequency = "annual"
    start_year = 2012
    end_year = 2022
    max_records = 60000

    # Step 1: Fetch all data
    all_data = fetch_all_data(frequency, start_year, end_year, max_records)

    if not all_data:
        print("No data fetched.")
        return

    # Step 2: Save raw data to CSV (optional, uncomment to enable)
    output_file = "co2_emissions_2012_2022.csv"
    # save_data_to_csv(all_data, output_file)

    # Step 3: Process and clean the data
    cleaned_data = process_api_data(all_data, start_year, end_year)

    # Step 4: Save cleaned data to CSV (optional, uncomment to enable)
    # cleaned_output_file = "cleaned_co2_emissions_2012_2022.csv"
    # cleaned_data.to_csv(cleaned_output_file, index=False)
    # print(f"Cleaned data saved to '{cleaned_output_file}'.")

    # Step 5: Perform Exploratory Data Analysis (optional, uncomment to enable)
    # perform_eda(cleaned_data)
    # plot_distribution(cleaned_data)
    # detect_outliers(cleaned_data)
    # show_all_plots()

    # Step 6: Generate visualizations
    show_all_graphs(cleaned_data, SAVE_GRAPHS)

# Entry point for the script
if __name__ == "__main__":
    main()
