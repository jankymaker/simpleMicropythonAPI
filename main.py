import network
station = network.WLAN(network.STA_IF)
station.active(True)
station.connect("YOURWIFINAME","YOURWIFIPASSWORD")

import urequests 
import json

f = urequests.get('https://official-joke-api.appspot.com/random_joke')

t = json.loads(f.text)

print(t)

firstValue = ("{0}".format(str(t['setup'])))

secondValue = ("{0}".format(str(t['punchline'])))


print(firstValue)
print(secondValue)
