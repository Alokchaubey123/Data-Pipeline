import pandas as pd
from sqlalchemy import create_engine


def run_query(engine, title, query):

    print(f"\n{title}")

    df = pd.read_sql(query, engine)

    print(df)

    return df


def main():

    engine = create_engine("sqlite:///weather.db")
    run_query(
        engine,
        "1. Weather data",
        """
        SELECT city_id, temperature, humidity, weather
        FROM weather_readings
        ORDER BY temperature DESC
        """
    )


if __name__ == "__main__":
    main()