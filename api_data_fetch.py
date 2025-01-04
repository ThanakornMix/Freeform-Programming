import requests
import pandas as pd

# Define the base URL and your API Key
URL_BASE = "https://api.eia.gov/v2/"
API_KEY = "jhkTkcgtidrXrRFPGYXtgug0ZCygKtgvzS4LwDw2"  # Replace with your actual API key

# Function to fetch data from a specific API route
def fetch_data_from_api(route):
    url = f"{URL_BASE}{route}/data"  # Construct the full URL
    params = {'api_key': API_KEY}
    
    # Send GET request to fetch data from the API
    res = requests.get(url, params=params)
    
    # Check if the request was successful
    if res.status_code == 200:
        return res.json()  # Return the response data in JSON format
    else:
        print(f"Failed to fetch data. HTTP Status Code: {res.status_code}")
        return None
