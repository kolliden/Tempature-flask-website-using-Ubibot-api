import requests
import json
import time

class getWeather():
    def __init__(self):
        self.channel  = 10481

    def request(self, x):
        y = requests.get(url = x)
        return y.json()

    async def main(self, account_key):
        try:
            newURL = f"http://api.ubibot.io/channels/{self.channel}?account_key={account_key}"
            newData = self.request(newURL)
            valuex = json.loads(newData['channel']['last_values'])
            value = round(valuex['field1']['value'])
            #print(newData)

            return value
        except:
            pass

if __name__ == "__main__":
    getter = getWeather()
    while True:
        print(getter.main())