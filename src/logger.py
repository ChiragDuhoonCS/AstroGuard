import os

def get_log_path():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(script_dir, "space_log.txt")

def log_apod(data):
    with open(get_log_path(), "a") as file:
        file.write(f"\n[APOD] {data['date']}\n")
        file.write(f"Title: {data['title']}\n")
        file.write(f"URL: {data['url']}\n")

def log_asteroids(data):
    neo_data = data["near_earth_objects"]
    with open(get_log_path(), "a") as file:
        for day in neo_data:
            file.write(f"\n[ASTEROIDS] {day}\n")
            for asteroid in neo_data[day]:
                name = asteroid["name"]
                hazardous = asteroid["is_potentially_hazardous_asteroid"]
                file.write(f"  {name} - Hazardous: {hazardous}\n")