# see test2 to understand if missed out

#@ to extract api key from .env  (to see and extract whats inside .env to other file)
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("NASA_API_KEY")


#@ to extract data from api 
import requests



#& now lets convert them into functions

#@ to show image
def get_log_path():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(script_dir, "space_log.txt")


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




#! SOLOR WEATHER   can ignore coz nasa server suck

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



#@ converting url into image   from apod  we use log

def log_apod(data):
    with open(get_log_path(), "a") as file:
        file.write(f"\n[APOD] {data['date']}\n")
        file.write(f"Title: {data['title']}\n")
        file.write(f"URL: {data['url']}\n") 

def log_asteroids(data):
    neo_data = data["near_earth_objects"]
    print("Logging asteroids...")
    with open(get_log_path(), "a") as file:
        for day in neo_data:
            file.write(f"\n[ASTEROIDS] {day}\n")
            for asteroid in neo_data[day]:
                name = asteroid["name"]
                hazardous = asteroid["is_potentially_hazardous_asteroid"]
                file.write(f"  {name} - Hazardous: {hazardous}\n")      


#!  main menu
while True:
    print("------ Daily Space Briefing -----")
    print("1. Today's Astronomy Picture")
    print("2. Near-Earth Asteroids (Next 7 Days)")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        apod_data = get_apod()
        if apod_data:
            show_apod(apod_data)
            log_apod(apod_data) 

    elif choice == "2":
        asteroid_data = get_asteroids()
        if asteroid_data:
            show_asteroids(asteroid_data)
            log_asteroids(asteroid_data)
    
    elif choice == "3":
        print("Goodbye!")
        break
    
    else:
        print("Invalid choice, try again.")  


             