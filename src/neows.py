import requests
from datetime import date, timedelta

today = date.today()
week_later = today + timedelta(days=7)

start_date = today.strftime("%Y-%m-%d") #@ %a day nasa api wouldnot accept
end_date = week_later.strftime("%Y-%m-%d")

def get_asteroids(api_key, start_date, end_date):
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

def show_asteroids(data):
    neo_data = data["near_earth_objects"]

    for day in neo_data:
        print(f"\n----> Date: {day}")
        asteroids = neo_data[day]

        for asteroid in asteroids:
            name = asteroid["name"]
            hazardous = asteroid["is_potentially_hazardous_asteroid"]
            diameter = asteroid["estimated_diameter"]["meters"]["estimated_diameter_max"]

            print(f"\n Name: {name}")
            print(f"\n Hazardous: {hazardous}")
            print(f"\n Diameter: {diameter}")
            print("===================================")
