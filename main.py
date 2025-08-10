import requests
import pandas as pd
import mysql.connector

# Fetch data from WeatherAPI
url = 'http://api.weatherapi.com/v1/current.json?key=766b1edc578a44a8ba6161712250908&q=Kristiansand&aqi=yes'
response = requests.get(url)
data = response.json()

# Extract relevant fields
weather_info = {
    'location': data['location']['name'],
    'time_stamp': data['location']['localtime'],
    'temp_c': data['current']['temp_c'],
    'humidity': data['current']['humidity'],
    'cond': data['current']['condition']['text'],
    'wind_kph': data['current']['wind_kph'],
    'pressure_mb': data['current']['pressure_mb'],
    
}

# Convert to DataFrame
df = pd.DataFrame([weather_info])


# Connect to MySQL
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Pia&Victor0935',
    database='krs_weather_db'
)
cursor = conn.cursor()

# Insert each row from DataFrame
for _, row in df.iterrows():
    cursor.execute("""
        INSERT INTO krs_weather_data (location, time_stamp, temp_c, humidity, cond, wind_kph, pressure_mb)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """, tuple(row))

conn.commit()
cursor.close()
conn.close()

