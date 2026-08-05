import requests
import os


API_KEY = os.environ.get("OPENWEATHER_API_KEY", "")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"



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