import requests
import json

class Locator():
    API_URL = 'http://api.ipstack.com/{}?access_key={}'

    KEY_FILE = 'key.txt'
    def __init__(self, key = None):
        if key:
            self.key = key
        else:
            try:
                with json.load(open(self.KEY_FILE)) as jsonObject:
                    self.key = self.KEY_FILE['key']
            except IOError:
                print("LOCATOR: Cannot find key file '{}'".format(self.KEY_FILE))

        if not self.key:
            return

        self.location = None
        self.getLocation()

    def getLocationJson(self):
        return self.location


    def getLocationText(self):
        ret = "Location Information:\n"
        for key in self.location:
            ret += "\t{}: {}\n".format(key, self.location[key])
        return ret

    def getLocation(self, ip = None):
        if not self.key:
            print("LOCATOR: No API key defined!")
            return

        if self.location and not ip:
            return

        if ip:
            req = requests.get(self.API_URL.format(ip, self.key))
        else:
            req = requests.get(self.API_URL.format('check', self.key))

        self.location = req.json()

if __name__ == "__main__":
    loc = Locator()
    print(loc.getLocationText())
