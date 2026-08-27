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

