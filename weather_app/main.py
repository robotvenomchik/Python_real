import time
import datetime
import requests
import sys

cities = sys.argv[-3:]

# https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid=47503e85fabbabc93cff28c52398ae97&units=metric

base_url = 'https://api.openweathermap.org/data/2.5/weather'

while True:
    for city in cities:
        params = {
            'q': city,
            'appid': '47503e85fabbabc93cff28c52398ae97',
            'units': 'metric',
        }
        response = requests.get(url=base_url, params=params)
        data = response.json()
        result = f'{datetime.datetime.now()},{data["name"]},{data["main"]["temp"]}\n'
        print(result, end='')
        with open(f'statistic/{city}.csv', 'a') as file:
            file.write(result)
        time.sleep(5)
