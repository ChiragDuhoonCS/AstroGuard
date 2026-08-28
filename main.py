from dotenv import load_dotenv
import os

from apod import get_apod, show_apod
from neows import get_asteroids, show_asteroids, get_date_range
from donki import get_solar_flares
from logger import log_apod, log_asteroids
from epic import get_epic_images, show_epic_images

load_dotenv()
api_key = os.getenv("NASA_API_KEY")

start_date, end_date = get_date_range()

while True:
    print("------ Daily Space Briefing -----")
    print("1. Today's Astronomy Picture")
    print("2. Near-Earth Asteroids (Next 7 Days)")
    print("3. Earth Imaginary pic (EPIC)")
    print("0. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        apod_data = get_apod(api_key)
        if apod_data:
            show_apod(apod_data)
            log_apod(apod_data)

    elif choice == "2":
        asteroid_data = get_asteroids(api_key, start_date, end_date)
        if asteroid_data:
            show_asteroids(asteroid_data)
            log_asteroids(asteroid_data)

    elif choice == "30":
        epic_data = get_epic_images(api_key)
        if epic_data:
            show_epic_images(epic_data)
            log_epic_image(epic_data)        

    elif choice == "0":
        print("Goodbye!")
        break

    else:
        print("Invalid choice, try again.")