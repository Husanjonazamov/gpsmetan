import time
import math
import random
import requests
from datetime import datetime, timedelta

CENTER_LAT = 41.3123
CENTER_LON = 69.2791
RADIUS_KM = 120  

DAYS = 7
HOURS_PER_DAY = 24
POSTS_PER_HOUR = 2
TOTAL_POSTS = DAYS * HOURS_PER_DAY * POSTS_PER_HOUR

# API ma'lumotlari
API_URL = "http://127.0.0.1:8045/api/sensor-data/"
DEVICE_ID = 456

POST_MINUTES = [13, 54]

def generate_path_coordinates(center_lat, center_lon, radius_km, points):
    coords = []
    for i in range(points):
        angle = 2 * math.pi * i / points
        dlat = (radius_km / 111) * math.cos(angle)
        dlon = (radius_km / (111 * math.cos(math.radians(center_lat)))) * math.sin(angle)
        coords.append((center_lat + dlat, center_lon + dlon))
    return coords

coordinates = generate_path_coordinates(CENTER_LAT, CENTER_LON, RADIUS_KM, TOTAL_POSTS)

simulation_start_date = datetime(2024, 7, 8)

def generate_random_data(lat, lon, current_time):
    return {
        "deviceId": DEVICE_ID,
        "flow": round(random.uniform(1.0, 3.0), 2),
        "pressure": round(random.uniform(1.0, 2.0), 2),
        "lat": lat,
        "lon": lon,
        "time": current_time.isoformat(),
        "temperature": round(random.uniform(20.0, 30.0), 1)
    }

print("Yuborish boshlandi...")

index = 0

for day_offset in range(DAYS):
    for hour in range(HOURS_PER_DAY):
        for minute in POST_MINUTES:
            current_time = simulation_start_date + timedelta(days=day_offset, hours=hour, minutes=minute)
            lat, lon = coordinates[index % len(coordinates)]
            data = generate_random_data(lat, lon, current_time)

            try:
                response = requests.post(API_URL, json=data)
                print(f"[{current_time}] Yuborildi: {data} => Status: {response.status_code}")
            except Exception as e:
                print(f"Xato: {e}")

            index += 1
            time.sleep(0.05)  

print("Haftalik 336 ta simulyatsiya yuborildi.")
