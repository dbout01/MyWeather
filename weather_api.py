import requests

def get_weather(location):
    response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid=93c5c74f2ef46cb3722057f1f93d5144&units=metric")
    weather_data = response.json()
    return weather_data
