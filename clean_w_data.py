import json
import pandas as pd


def main():

    with open("data/raw_weather.json", "r") as file:
        weather_data = json.load(file)

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

    print("\nCleaning data started")

    df["timestamp"] = pd.to_datetime(df["timestamp"], unit="s")

    df["temperature"] = df["temperature"].round(1)
    df["feels_like"] = df["feels_like"].round(1)
    df["temp_min"] = df["temp_min"].round(1)
    df["temp_max"] = df["temp_max"].round(1)

    df = df.dropna()
    df = df.drop_duplicates()
    df = df.sort_values("city")

    output_file = "data/clean_weather.csv"

    df.to_csv(output_file, index=False)
    print(df.head())


if __name__ == "__main__":
    main()
