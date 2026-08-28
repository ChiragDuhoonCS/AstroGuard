#@ to extract api key from .env  (to see and extract whats inside .env to other file)
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("NASA_API_KEY")


#@ to extract data from api 
import requests



#& now lets convert them into functions


#! APOD   DAILY PIC
def get_apod():
    url = "https://api.nasa.gov/planetary/apod"
    params = {"api_key": api_key}
    response = requests.get(url, params=params)
    
    if response.status_code != 200:
        print("Something went wrong:", response.status_code)
        return None
    
    data = response.json()
    return data

def show_apod(data):
    print("Title:", data["title"])
    print("Date:", data["date"])
    print("Explanation:", data["explanation"])
    print("Image URL:", data["url"])

apod_data = get_apod()
if apod_data:
    show_apod(apod_data)


#! NeoWs  track asteriod   we need time   multiple asteroid on same day

from datetime import date, timedelta

today = date.today()
week_later = today + timedelta(days=7)

start_date = today.strftime("%Y-%m-%d") #@ %a day nasa api wouldnot accept
end_date = week_later.strftime("%Y-%m-%d")

def get_asteroids():
    url = "https://api.nasa.gov/neo/rest/v1/feed"
    params = {
        "api_key": api_key,
        "start_date": start_date,
        "end_date": end_date
    }
    response = requests.get(url, params=params)

    if response.status_code != 200:
        print("Something went wrong:", response.status_code)
        return None

    data = response.json()
    return data




#!   NOW ITS TIME TO SHOW ASTEROIDS (FROM get_asteroids)

# data["near_earth_objects"] is itself a dictionary

asteroid_data = get_asteroids()

#&  Now nesting a second loop to get each asteroid on that day
def show_asteroids(data):
    neo_data = data["near_earth_objects"]

    for day in neo_data:
        print(f"\nDate: {day}")
        asteroids = neo_data[day]

        for asteroid in asteroids:
            name = asteroid["name"]
            hazardous = asteroid["is_potentially_hazardous_asteroid"]
            diameter = asteroid["estimated_diameter"]["meters"]["estimated_diameter_max"]

            print(f"\n Name: {name}")
            print(f"\n Hazardous: {hazardous}")
            print(f"\n Diameter: {diameter}")
            print("===================================")

if asteroid_data:
    show_asteroids(asteroid_data)


#! SOLOR WEATHER

#@ CHECK
def get_solar_flares():
    url = "https://api.nasa.gov/DONKI/FLR"
    params = {
        "api_key": api_key,
        "startDate": start_date,
        "endDate": end_date
    }
    response = requests.get(url, params=params)

    if response.status_code != 200:
        print("Something went wrong:", response.status_code)
        return None

    data = response.json()
    return data

flare_data = get_solar_flares()
print(flare_data)

#& RETRY IF FAIL 503 SERVICE UNAVAILABLE
import time

def get_solar_flares():
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
        time.sleep(2) # to give server 2 second break s it can reset properly

    print("All attempts failed.")
    return None