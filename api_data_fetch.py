import requests
import pandas as pd


URL_BASE = "https://api.eia.gov/v2/"
API_KEY = "jhkTkcgtidrXrRFPGYXtgug0ZCygKtgvzS4LwDw2"  


def fetch_data_from_api(route):
    url = f"{URL_BASE}{route}/data"  
    params = {'api_key': API_KEY}
    
  
    res = requests.get(url, params=params)
    

    if res.status_code == 200:
        return res.json()  
    else:
        print(f"Failed to fetch data. HTTP Status Code: {res.status_code}")
        return None

