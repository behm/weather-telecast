from pprint import pprint
import requests

# API Key from openweathermap.org
API_KEY = ""

location = input("Enter your desired location: ")
weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={API_KEY}"

print(weather_url)

weather_data = requests.get(weather_url).json()

pprint(weather_data)