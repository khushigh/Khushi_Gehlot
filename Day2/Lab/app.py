import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")


city_name = "Jaipur"
country_code = "IN"
url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name},{country_code}&appid={API_KEY}"


#USING PARAMS
# url = "https://api.openweathermap.org/data/2.5/weather"

# params = {
#     "q": "Jaipur,IN",
#     "appid": API_KEY
# }

# response = requests.get(url, params=params)

response = requests.get(url)
print(response.json())

#parse json response
data = response.json()
temparature = data.get("main").get("temp")
humidity = data.get("main").get("humidity")


print("Temparature=", temparature)
print("Humidity=", humidity)