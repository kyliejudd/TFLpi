import requests
import json



reponse = requests.get("https://api.tfl.gov.uk/StopPoint/910GFORESTH/Arrivals")

json = reponse.json()

for i in json:
    station = (i["stationName"])
    line = i["lineName"]
    direction = i["direction"]
    destination = i["destinationName"]
    arrival = i["expectedArrival"]
    due = (i["timeToStation"] / 60).__round__()
    print("Train going to {} due to arrive in {} minutes".format(destination, due))
