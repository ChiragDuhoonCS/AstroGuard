#! for solor space weather (currently unavailable 505) nasa mistake

import requests
import time

def get_solar_flares(api_key, start_date, end_date):
    url = "https://api.nasa.gov/DONKI/FLR"
    params = {
        "api_key": api_key,
        "startDate": start_date,
        "endDate": end_date
    }

    for attempt in range(3):
        response = requests.get(url, params=params)

        if response.status_code == 200:
            return response.json()

        print(f"Attempt {attempt + 1} failed with status {response.status_code}, retrying...")
        time.sleep(2)

    print("All attempts failed.")
    return None