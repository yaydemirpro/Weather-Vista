import requests
import os
import json

def getWeather(place):   
    api_key = "1a21baead2df1a53d7ea57d08feb0025"
    units = "metric"
    lang = "en"

    url = f'https://api.openweathermap.org/data/2.5/weather?q={place}&appid={api_key}&units={units}&lang={lang}'

    response  = requests.get(url)

    print(response)
    print(response.text)
    print(response.json())

    weathers = response.json()

    file_path = os.path.join(os.getcwd(), "weather.json")
    with open(file_path, 'w', encoding="utf-8") as json_file:
        json.dump(weathers, json_file)


getWeather('Amstelveen')

