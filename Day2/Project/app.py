"""
Fetch weather data from OpenWeather API, validate with Pydantic,
write a clean summary report to report.txt
"""

import os
import requests
from datetime import datetime
from dotenv import load_dotenv
from pydantic import BaseModel, ValidationError
from typing import List

load_dotenv()

API_KEY = os.getenv("API_KEY")

if not API_KEY:
    raise ValueError("API_KEY not set in .env")

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
class MainWeather(BaseModel):
    temp: float
    humidity: int
    pressure: int


class WeatherInfo(BaseModel):
    main: str
    description: str


class Wind(BaseModel):
    speed: float


class WeatherResponse(BaseModel):
    name: str
    weather: List[WeatherInfo]
    main: MainWeather
    wind: Wind

def fetch_weather(city: str) -> dict:
    """Fetch raw weather data from OpenWeather API."""

    print(f"Fetching weather for {city}...")

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    response = requests.get(BASE_URL, params=params, timeout=10)

    response.raise_for_status()

    return response.json()


def validate_weather(raw_data: dict) -> WeatherResponse:
    """Validate weather response using Pydantic."""

    try:
        validated_data = WeatherResponse(**raw_data)
        return validated_data

    except ValidationError as e:
        print("Validation Error:")
        print(e)
        raise


def write_report(weather: WeatherResponse,
                 output: str = "report.txt"):
    """Write clean weather report."""

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    lines = [
        "=" * 60,
        f"WEATHER REPORT — generated {now}",
        "=" * 60,

        f"\nCity:        {weather.name}",

        f"Temperature: {weather.main.temp} °C",

        f"Humidity:    {weather.main.humidity}%",

        f"Pressure:    {weather.main.pressure} hPa",

        f"Condition:   {weather.weather[0].main}",

        f"Description: {weather.weather[0].description}",

        f"Wind Speed:  {weather.wind.speed} m/s"
    ]

    with open(output, "w", encoding="utf-8") as file:
        file.write("\n".join(lines))

    print(f"Report written → {output}")

def main():

    city = "Jaipur"

    raw_weather = fetch_weather(city)

    validated_weather = validate_weather(raw_weather)

    print("Weather data validated successfully!")

    write_report(validated_weather)


if __name__ == "__main__":
    main()