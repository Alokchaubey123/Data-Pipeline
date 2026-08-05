import json
import pandas as pd


def main():

    with open("data/raw_weather.json", "r") as file:
        weather_data = json.load(file)

    print(f"Loaded {len(weather_data)} records")

    data = []
    for item in weather_data:

        data.append({
            "city": item["name"],
            "country": item["sys"]["country"],
            "temperature": item["main"]["temp"],
            "feels_like": item["main"]["feels_like"],
            "temp_min": item["main"]["temp_min"],
            "temp_max": item["main"]["temp_max"],
            "humidity": item["main"]["humidity"],
            "pressure": item["main"]["pressure"],
            "wind_speed": item["wind"]["speed"],
            "weather": item["weather"][0]["main"],
            "description": item["weather"][0]["description"],
            "timestamp": item["dt"]
        })#all this data is present in .json file, some points are extracted 
    df = pd.DataFrame(data)
    print(df)

if __name__ == "__main__":
    main()
