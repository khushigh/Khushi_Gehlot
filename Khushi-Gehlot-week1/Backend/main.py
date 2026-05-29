from flask import Flask, jsonify, request
from flask_cors import CORS
import requests
import os
from dotenv import load_dotenv
from pydantic import BaseModel, ValidationError
app = Flask(__name__)
CORS(app)

load_dotenv()

API_KEY = os.getenv("API_KEY")

if not API_KEY:
    raise ValueError("API_KEY not set in .env")

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


# -------- Pydantic Models --------

class MainInfo(BaseModel):
    temp: float
    humidity: int


class Wind(BaseModel):
    speed: float


class WeatherResponse(BaseModel):
    name: str
    main: MainInfo
    wind: Wind

def validate_weather(raw_data: dict):

    try:
        validated_data = WeatherResponse(**raw_data)
        return validated_data

    except ValidationError as e:
        print(e)
        return None
# -------- Route --------
@app.route("/weather")
def fetch_weather():

    city = request.args.get("city", "Jaipur")

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    response = requests.get(BASE_URL, params=params, timeout=10)

    raw_data = response.json()

    validated_data = validate_weather(raw_data)

    if not validated_data:
        return jsonify({
            "error": "Invalid city"
        }), 400

    return jsonify({
        "city": validated_data.name,
        "temperature": validated_data.main.temp,
        "humidity": validated_data.main.humidity,
        "wind_speed": validated_data.wind.speed
    })

# -------- Run Server --------

if __name__ == "__main__":
    app.run(debug=True)
