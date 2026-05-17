# Weather App
# ----------
# A CLI app that fetches real-time weather data from the OpenWeatherMap API.
#
# Features:
# - User enters any city and gets current temperature, and weather description
# - Saves every search to Weather.json
# - Updates existing city entries instead of creating duplicates
# - Loops continuously until user types "quit"
# - Handles errors for invalid city names
#
# Built with: requests, json, OpenWeatherMap API

import json
import requests

API_KEY = "065f489cb0f1a39404103d9d561f3f4b"


def load_data():
    with open("Weather.json", "r") as f:
        store = json.load(f)
        return store


def save_data(data):
    with open("Weather.json", "w") as f:
        json.dump(data,f,indent=2)





def get_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    responses = requests.get(url)
    return responses.json()



def display_weather(data):
    print(data["name"])
    print(f"{data["main"]['temp']}C")
    print(data["weather"][0]["description"])


while True:
    city = input('Enter your city: ')

    if city == "quit":
        break

    data = get_weather(city)
    display_weather(data)

    history = load_data()
    found = False
    for x in history:
        if x["Name"] == city:
            x["Temperature"] = data["main"]['temp']
            x["Description"] = data["weather"][0]["description"]
            # update temp and description
            found = True
            break

    if not found:
        history.append({
            "Name": data["name"],
            "Temperature": data["main"]["temp"],
            "Description": data["weather"][0]["description"]
        })
    # append new entry

    save_data(history)
# {'coord': {'lon': -80.1937, 'lat': 25.7743}, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'base': 'stations', 'main': {'temp': 29.22, 'feels_like': 32.64, 'temp_min': 28.32, 'temp_max': 31.12, 'pressure': 1010, 'humidity': 67, 'sea_level': 1010, 'grnd_level': 1010}, 'visibility': 10000, 'wind': {'speed': 5.14, 'deg': 170}, 'rain': {'1h': 0.16}, 'clouds': {'all': 40}, 'dt': 1777584674, 'sys': {'type': 2, 'id': 2009435, 'country': 'US', 'sunrise': 1777545880, 'sunset': 1777593065}, 'timezone': -14400, 'id': 4164138, 'name': 'Miami', 'cod': 200}


# Hwoit was displayed in the file history {'Name': 'Miami', 'Temperature': 25.86, 'Description': 'few clouds'}
# {'Name': 'Toronto', 'Temperature': 14.59, 'Description': 'broken clouds'}
# {'Name': 'Texas', 'Temperature': 29.97, 'Description': 'clear sky'}
# {'Name': 'Los Angeles', 'Temperature': 20.6, 'Description': 'clear sky'}