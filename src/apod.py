import requests

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
