import time
import math
import random
import requests
from datetime import datetime, timedelta

CENTER_LAT = 41.3123
CENTER_LON = 69.2791
RADIUS_KM = 120  

TOTAL_POSTS = 24  # Har soatga bitta

# API ma'lumotlari
API_URL = "https://gpsmetan.felixits.uz/api/sensor-data/"
DEVICE_ID = 789

# 1 gradus taxminan 111 km
KM_IN_DEGREE = 111

# Harakat uchun trayektoriya yasash
def generate_movement_path(start_lat, start_lon, radius_km, points):
    path = []
    current_lat = start_lat
    current_lon = start_lon

    for i in range(points):
        # Har soatda kichik farq bilan oldinga yurish
        step_km = random.uniform(3, 7)  # Har soatda 3km dan 7km gacha yurish
        angle = random.uniform(0, 2 * math.pi)  # Tasodifiy yo'nalish

        dlat = (step_km / KM_IN_DEGREE) * math.cos(angle)
        dlon = (step_km / (KM_IN_DEGREE * math.cos(math.radians(current_lat)))) * math.sin(angle)

        current_lat += dlat
        current_lon += dlon

        # Radiusdan chiqib ketmasin
        distance_from_center = math.sqrt(((current_lat - start_lat) * KM_IN_DEGREE) ** 2 +
                                         ((current_lon - start_lon) * KM_IN_DEGREE * math.cos(math.radians(start_lat))) ** 2)

        if distance_from_center > radius_km:
            # Agar 120km dan chiqib ketsa, orqaga qaytarib olamiz
            current_lat -= dlat * 2
            current_lon -= dlon * 2

        path.append((current_lat, current_lon))

    return path

today = datetime.now().date()

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

# Trayektoriya hosil qilamiz
movement_path = generate_movement_path(CENTER_LAT, CENTER_LON, RADIUS_KM, TOTAL_POSTS)

print("Bugungi 24 soatlik yurish trayektoriyasi yuborish boshlandi...")

for hour in range(24):
    current_time = datetime.combine(today, datetime.min.time()) + timedelta(hours=hour)
    lat, lon = movement_path[hour]
    data = generate_random_data(lat, lon, current_time)

    try:
        response = requests.post(API_URL, json=data)
        print(f"[{current_time}] Yuborildi: {data} => Status: {response.status_code}")
    except Exception as e:
        print(f"Xato: {e}")

    time.sleep(0.05)

print("24 soatlik simulyatsiya tugadi.")
