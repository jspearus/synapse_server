import json, os, requests
from channels.generic.websocket import AsyncWebsocketConsumer



# weather condition lists
snowing =["snow", "flurries"]
clear =["fair", "clear"]
fog =["fog", "mist", "haze", "squall", "smoke", "dust"]
raining =["rain", "mist", "drizzle", "thunderstorm"]
cloud =["cloud", "cloudy", "clouds"]



def get_weather():
    response = requests.get(
        "https://api.openweathermap.org/data/2.5/weather?q=Coal%20City,Illinois&units=imperial&appid=fb1746a57b7d298207e7d62a0067f503")
    json_data = json.loads(response.text)
    weather = json_data['weather']
    curWeather = weather[0]['main']
    curDesctiption = weather[0]['description']
    if curWeather.lower() in snowing:
        weatherCondition = "snow"
    elif curWeather.lower() in clear:
        weatherCondition = "clear"
    elif curWeather.lower() in raining:
        weatherCondition = "rain"
    return weatherCondition

    print(f"current weather: {curWeather.lower()}")
    print(f"current condition: {curDesctiption.lower()}")