import requests
import json
import time
from decouple import config

class getWeather():
    def __init__(self):
        self.channel  = config('CHANNEL')
        self.account_key = config('KEY')
        self.URL = f"http://api.ubibot.io/channels/{self.channel}?account_key={self.account_key}"

    def request(self, x):
        y = requests.get(url = x)
        return y.json()

    async def main(self):
        try:
            newData = self.request(self.URL)
            valuex = json.loads(newData['channel']['last_values'])
            value = round(valuex['field1']['value'])
            #print(newData)

            return value
        except:
            raise Exception("asd")

if __name__ == "__main__":
    getter = getWeather()
    while True:
        print(getter.main())
        time.sleep(5)