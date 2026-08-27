from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("NASA_API_KEY")
print(api_key)

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