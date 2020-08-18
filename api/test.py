import requests
from secrets import Evan_Mac_ip

BASE = "http://" + Evan_Mac_ip + ":5000/"

response = requests.get(BASE + "/meantweet/@RealDonaldTrump")
print(response.json())

