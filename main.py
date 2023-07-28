import requests
import time
import datetime
import sys
base_url="http://api.open-notify.org/iss-now.json"
while True:

        params = {
            'longitude': "68.5446",
            'latitude': "0.0905"
        }
        response = requests.get(url=base_url, params=params)
        data = response.json()
        result = f'{datetime.datetime.now()},{data["timestamp"]},{data["iss_position"]}\n'
        print(result, end='')
        with open(f'positions/pos.csv', 'a') as file:
            file.write(result)
        time.sleep(5)
