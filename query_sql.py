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

    # run_query(
    #     engine,
    #     "2. Weather count",
    #     """
    #     SELECT weather, COUNT(*) AS city_count
    #     FROM weather_readings
    #     GROUP BY weather
    #     ORDER BY city_count DESC
    #     """
    # )

    # run_query(
    #     engine,
    #     "3. Temperature by city",
    #     """
    #     SELECT c.city,
    #            c.country,
    #            ROUND(AVG(r.temperature),1) AS avg_temp,
    #            MIN(r.temp_min) AS lowest_temp,
    #            MAX(r.temp_max) AS highest_temp,
    #            COUNT(*) AS readings
    #     FROM weather_readings r
    #     JOIN cities c
    #     ON r.city_id = c.city_id
    #     GROUP BY c.city
    #     ORDER BY avg_temp DESC
    #     """
    # )

    # run_query(
    #     engine,
    #     "4. Cities above average temperature",
    #     """
    #     SELECT c.city, r.temperature
    #     FROM weather_readings r
    #     JOIN cities c
    #     ON r.city_id = c.city_id
    #     WHERE r.temperature >
    #     (
    #         SELECT AVG(temperature)
    #         FROM weather_readings
    #     )
    #     ORDER BY r.temperature DESC
    #     """
    # )

    # run_query(
    #     engine,
    #     "5. Highest humidity",
    #     """
    #     SELECT c.city, r.humidity
    #     FROM weather_readings r
    #     JOIN cities c
    #     ON r.city_id = c.city_id
    #     ORDER BY r.humidity DESC
    #     LIMIT 1
    #     """
    # )

    print("\nDone")

if __name__ == "__main__":
    main()