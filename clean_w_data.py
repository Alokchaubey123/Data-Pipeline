import json
import pandas as pd


def main():

    with open("data/raw_weather.json", "r") as file:
        weather_data = json.load(file)

    print(f"Loaded {len(weather_data)} records")
    print(weather_data)

if __name__ == "__main__":
    main()
