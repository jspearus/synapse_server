import datetime
import json
import os
import threading
import time
import holidays
import requests
from channels.generic.websocket import AsyncWebsocketConsumer
from dateutil.easter import *

Holidays = [
    "New Year's Day", "Easter", "Memorial Day", "Independence Day", "Halloween",
    "Thanksgiving", "Christmas Day"
]

holidayDates = {}
year = datetime.date.today().year
nxtHoliday = ''

weather = ""
sunset = ""

# weather condition lists
snowing =["snow", "flurries"]
clear =["fair", "clear"]
fog =["fog", "mist", "haze", "squall", "smoke", "dust"]
raining =["rain", "mist", "drizzle", "thunderstorm"]
cloud =["cloud", "cloudy", "clouds"]



def update_weather():
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
    elif curWeather.lower() in cloud:
        weatherCondition = "cloud"
    elif curWeather.lower() in fog:
        weatherCondition = "fog"
    return weatherCondition

    # print(f"current weather: {curWeather.lower()}")
    # print(f"current condition: {curDesctiption.lower()}")
    
def update_sunset():
    global sunset
    response2 = requests.get(
        "https://api.sunrise-sunset.org/json?lat=41.287810&lng=-88.285618&date=noon")
    json_data2 = json.loads(response2.text)
    time = json_data2['results']
    sunset = time['sunset']
    
def check_weather():
    global weather
    while True:
        weather = update_weather()
        time.sleep(200)
    
def check_sunset():
    global sunset
    while True:
        update_sunset()
        time.sleep(43200)
        
def get_weather():
    global weather
    return weather

def get_sunset():
    global sunset
    # print(f"sunset: {sunset}")
    return sunset
        
        
        
def get_holidays():
    h_added = False
    e_added = False
    hList = holidays.US(years=year).items()
    # add Custom Holidays
    for date, name in sorted(hList):
        if easter(year) < date and e_added == False:
            holidayDates[easter(year)] = "Easter"
            e_added = True

        if datetime.date(year, 10, 31) < date and h_added == False:
            holidayDates[datetime.date(year, 10, 31)] = "Halloween"
            h_added = True
        holidayDates[date] = name


def getNxtHoliday():
    get_holidays()
    for date, name in holidayDates.items():
        if datetime.date.today() <= date and name in Holidays:
            nxtDate = date
            nxtHoliday = name
            break
            
    return nxtHoliday
    
weatherThead = threading.Thread(target=check_weather, args=())
weatherThead.setDaemon(True)
weatherThead.start()

sunsetThead = threading.Thread(target=check_sunset, args=())
sunsetThead.setDaemon(True)
sunsetThead.start()