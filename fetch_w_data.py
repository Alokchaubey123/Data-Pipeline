import requests
import os

import json
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.environ.get("OPENWEATHER_API_KEY", "")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

CITIES = [
    "London",
    "Tokyo",
    "Delhi",
    "Paris",
    "Kyoto",
    "Kolkata"
]

def fetch_weather_for_city(city):
    #fetching city data

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric",
    }

    try:
        response = requests.get(BASE_URL, params=params, timeout=10)

        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error for {city}: {response.status_code}")
            return None

    except requests.exceptions.RequestException:
        print(f"Request failed for {city}")
        return None

def main():

    print("Fetching weather data searching started")



    if API_KEY:
        print("Fetching using OpenWeather API\n")

    else:

        print("API key not found.\n")



    weather_data = []



    for city in CITIES:

        print(f"Getting data for {city}")



        if API_KEY:

            city_data = fetch_weather_for_city(city)

        else:

            print("city_data not found.\n")
            break



        if city_data is not None:

            weather_data.append(city_data)


    os.makedirs("data", exist_ok=True)

    output_file = "data/raw_weather.json"

    with open(output_file, "w") as file:

        json.dump(weather_data, file, indent=4)



    print(f"\nData Saved in raw_weather.json")



if __name__ == "__main__":

    main()

