import requests
import json
import time

api_key = "e8f68457747d3735390442fee34982df"
city_name = "chittagong"

def weather_data(api_key, city):
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

    response = requests.get(url).json()

    weather_details = {
        'location_name' : response['name'],
        'current_temp' : round(response['main']['temp'] -  273.15, 2),
        'feels_like' : round(response['main']['feels_like'] -  273.15, 2),
        'weather' : response['weather'][0]['description']
    }

    print(f"Location name: {weather_details['location_name']}\nCurrent Temp: {weather_details['current_temp']} degree c\nFeels Like: {weather_details['feels_like']} degree c\nWeather Description: {weather_details['weather']}")

while True:
    weather_data(api_key, city_name)
    print()
    time.sleep(30 * 60)

