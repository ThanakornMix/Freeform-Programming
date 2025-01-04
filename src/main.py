from api_data_fetcher import fetch_all_data  # Import the fetch function from data_fetcher.py
from data_collection import save_data_to_csv  # Import the save function from data_collection.py

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

# Run the main function
if __name__ == "__main__":
    main()
