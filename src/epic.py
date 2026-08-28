import requests

def get_epic_images(api_key):
    url = "https://api.nasa.gov/EPIC/api/natural/images"
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
        year, month, day = date_part.split("-") # put - in between
        image_name = item["image"]

        image_url = f"https://epic.gsfc.nasa.gov/archive/natural/{year}/{month}/{day}/png/{image_name}.png"

        print(f"\nDate: {item['date']}")
        print(f"Caption: {item['caption']}")
        print(f"Image URL: {image_url}")