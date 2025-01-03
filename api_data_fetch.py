import requests
import pandas as pd

#base URL and your API Key
BASE_URL = "https://api.eia.gov/v2/"
API_KEY = "jhkTkcgtidrXrRFPGYXtgug0ZCygKtgvzS4LwDw2"

# Function to fetch data from a specific API route
def fetch_data_from_api(route):
    params = {'api_key': API_KEY}
    # Construct the full URL by appending the route to the base URL
    url = f"{BASE_URL}{route}?api_key={API_KEY}"
    print(url)
    # Send GET request to fetch data from the API
    res = requests.get(url, params=params)
    
    if res.status_code == 200:
        return res.json()  # Return the response data in JSON format
    else:
        print(f"Failed to fetch data. HTTP Status Code: {res.status_code}")
        return None

# Test Fetch data from the "electricity" endpoint
route = "electricity/rto/region-data"  # change this to any valid route from the API
data = fetch_data_from_api(route)

# Process and display the fetched data
if data and 'response' in data and 'routes' in data['response']:
    df = pd.DataFrame(data['response']['routes'])
    print(df)  
else:
    print("Error")