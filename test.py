#@ to extract api key from .env  (to see and extract whats inside .env to other file)
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("NASA_API_KEY")
print(api_key)

#@ to extract data from api 
import requests

url = "https://api.nasa.gov/planetary/apod"
params = {"api_key": api_key} # dictionary

response = requests.get(url, params=params) # send request

print(response.status_code) #@ 200 means success

#@ now request/response have reply and we have to look now
# we will use json(word wall) here

data = response.json()
print(data)

# now lets break it into pices  product.title,customer like

title = data["title"]
explanation = data["explanation"]
image_url = data["url"]

print("Title:", title)
print("Explanation:", explanation)
print("Image URL:", image_url)

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

asteroid_data = get_asteroids()
print(asteroid_data)


#!   NOW ITS TIME TO SHOW ASTEROIDS (FROM get_asteroids)

# data["near_earth_objects"] is itself a dictionary

#&  looping through a dictionary's keys
for day in asteroid_data["near_earth_objects"]:
    print(day)


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

if asteroid_data:
    show_asteroids(asteroid_data)
        