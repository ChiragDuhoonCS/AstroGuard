#! for earth image (currently error 404)

import requests

def get_epic_images(api_key):
    url = "https://api.nasa.gov/EPIC/api/natural"
    params = {"api_key": api_key}
    response = requests.get(url, params=params)

    if response.status_code != 200:
        print("Something went wrong:", response.status_code)
        return None

    data = response.json()
    return data

def show_epic_images(data):
    if len(data) == 0:
        print("No EPIC images available.")
        return

    for item in data:
    #& means break stuff into three  "2026-08-28 01:08:12"  this in api 
       date_part = item["date"].split(" ")[0]
        #& we will take only date
       year, month, day = date_part.split("-")
       image_name = item["image"]
   
      # print("DEBUG date_part:", date_part)
      # print("DEBUG year/month/day:", year, month, day)
      # print("DEBUG image_name:", image_name)

       image_url = f"https://epic.gsfc.nasa.gov/archive/natural/{year}/{month}/{day}/png/{image_name}.png"
       print("DEBUG full URL:", image_url)

    
