import requests
import json
import time
from decouple import config
import asyncio

class Interface():
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
            value = json.loads(newData['channel']['last_values'])
            temp = round(value['field1']['value'])
            humidity = value['field2']['value']   #not sure about this TODO
            lightLevel = value['field3']['value'] #not sure about this TODO
            print(value)
            return temp, humidity, lightLevel
        except:
            raise Exception("asd")

if __name__ == "__main__":
    interface = Interface()
    while True:
        x = asyncio.run(interface.main())
        temp, humidity, lightLevel = x
        print(temp, humidity, lightLevel)
        time.sleep(5)