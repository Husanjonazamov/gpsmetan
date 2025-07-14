import time
import math
import random
import requests
from datetime import datetime, timedelta

CENTER_LAT = 41.3123
CENTER_LON = 69.2791
RADIUS_KM = 120  

DAYS = 31   # 31 kunlik
TOTAL_POSTS = DAYS  # Har kuni 1 dona

# API ma'lumotlari
API_URL = "https://gpsmetan.felixits.uz/api/sensor-data/"
DEVICE_ID = 897

POST_HOUR = 13
POST_MINUTE = 54

def generate_path_coordinates(center_lat, center_lon, radius_km, points):
    coords = []
    for i in range(points):
        angle = 2 * math.pi * i / points
        dlat = (radius_km / 111) * math.cos(angle)
        dlon = (radius_km / (111 * math.cos(math.radians(center_lat)))) * math.sin(angle)
        coords.append((center_lat + dlat, center_lon + dlon))
    return coords

coordinates = generate_path_coordinates(CENTER_LAT, CENTER_LON, RADIUS_KM, TOTAL_POSTS)

simulation_start_date = datetime(2025, 7, 8)

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

for day_offset in range(DAYS):
    current_time = simulation_start_date + timedelta(days=day_offset, hours=POST_HOUR, minutes=POST_MINUTE)
    lat, lon = coordinates[day_offset]
    data = generate_random_data(lat, lon, current_time)

    try:
        response = requests.post(API_URL, json=data)
        print(f"[{current_time}] Yuborildi: {data} => Status: {response.status_code}")
    except Exception as e:
        print(f"Xato: {e}")

    time.sleep(0.05)  

print(f"{DAYS} kunlik simulyatsiya yuborildi.")
