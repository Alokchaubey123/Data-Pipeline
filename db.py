import pandas as pd
from sqlalchemy import create_engine


def main():

    df = pd.read_csv("data/clean_weather.csv", parse_dates=["timestamp"])


    engine = create_engine("sqlite:///weather.db")

    # Cities table
    cities = df[["city", "country"]].drop_duplicates().reset_index(drop=True) #only contain distinct city

    cities["city_id"] = cities.index + 1

    # Weather table
    weather = df.merge(cities, on=["city", "country"])

    weather = weather.drop(columns=["city", "country"])

    cities.to_sql("cities", engine, if_exists="replace", index=False)

    weather.to_sql("weather_readings", engine, if_exists="replace", index=False)

    print("Database created")

    result = pd.read_sql(
        "SELECT COUNT(*) AS total FROM weather_readings",
        engine
    )
    print(result)


if __name__ == "__main__":
    main()