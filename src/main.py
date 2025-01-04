from api_data_fetcher import fetch_all_data  # Import the fetch function from data_fetcher.py
from collection_data import save_data_to_csv  # Import the save function from data_collection.py
from process_data import inspect_data # Improt the inspect function from process_data
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

    # Inspect the data
    if all_data:
        inspect_data(all_data)
    else:
        print("Inspect Error")

# Run the main function
if __name__ == "__main__":
    main()
