




# def get_weather():
#     try:
#         response = requests.get(
#             "https://api.open-meteo.com/v1/forecast?latitude=26.92&longitude=75.82&current_weather=true",
#             timeout=10
#         )

#         response.raise_for_status()

#         data = response.json()

#         weather = WeatherReport(
#             city="Jaipur",
#             temperature_c=data["current_weather"]["temperature"],
#             humidity=42,
#             conditions=["sunny"]
#         )

#         return weather

#     except requests.RequestException:
#         return {"error": "Failed to fetch weather data"}


