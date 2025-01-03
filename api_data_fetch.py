import requests
import pandas as pd

URL = "https://api.eia.gov/v2/"
API_KEY = "jhkTkcgtidrXrRFPGYXtgug0ZCygKtgvzS4LwDw2"

params = {'api_key': API_KEY}

# Fetch data from API
res = requests.get(url=URL, params=params)

# Parse the JSON response
data = res.json()

# Check if the 'response' and 'routes' keys exist before trying to use them
if 'response' in data and 'routes' in data['response']:
    # Convert the 'routes' part of the data into a DataFrame
    df = pd.DataFrame(data['response']['routes'])
    print(df)  # Print the DataFrame to verify the result
else:
    print("Error: 'response' or 'routes' not found in the API response.")
