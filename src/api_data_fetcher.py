import os
import requests
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Define the base URL and API key
URL_BASE = "https://api.eia.gov/v2/co2-emissions/co2-emissions-aggregates/data/"
API_KEY = os.getenv("API_KEY")  # Fetching the API key from the environment variable

# Function to fetch data with query parameters
def fetch_data(route, frequency, start_year, end_year, offset=0, length=5000):
    """
    Fetches data using query parameters.

    :param route: API route
    :param frequency: Data frequency (e.g., annual)
    :param start_year: Start year for the data
    :param end_year: End year for the data
    :param offset: Offset for pagination
    :param length: Number of records per page
    :return: Response data as a JSON object
    """
    # Construct the query parameters
    params = {
        "api_key": API_KEY,
        "frequency": frequency,
        "data[0]": "value",
        "sort[0][column]": "period",
        "sort[0][direction]": "desc",
        "offset": offset,
        "length": length
    }

    # Add start and end date range if specified
    if start_year and end_year:
        params["start"] = f"{start_year}-01-01"
        params["end"] = f"{end_year}-12-31"

    # Send the GET request
    response = requests.get(route, params=params)

    # Handle the response
    if response.status_code == 200:
        return response.json()  # Return the JSON response
    else:
        print(f"Error: Failed to fetch data. Status Code: {response.status_code}")
        return None

# Function to fetch all data with pagination
def fetch_all_data(frequency, start_year, end_year, max_records=60000):
    """
    Fetch all data for a given range of years, handling pagination.

    :param frequency: Data frequency
    :param start_year: Start year for the data
    :param end_year: End year for the data
    :param max_records: Maximum number of records to fetch
    :return: Combined data as a list
    """
    all_data = []
    offset = 0
    length = 2000  # Number of records per request

    while len(all_data) < max_records:
        print(f"Fetching data with offset {offset}...")
        data = fetch_data(URL_BASE, frequency, start_year, end_year, offset, length)

        # Validate and append data
        if data and "response" in data and "data" in data["response"]:
            current_data = data["response"]["data"]
            all_data.extend(current_data)
            if len(current_data) < length:
                print("Reached the last page of data.")
                break  # Stop fetching if fewer records were returned
            offset += length  # Increment the offset for pagination
        else:
            print("No more data or invalid response.")
            break

    return all_data
