# input: lat, long, request type

import requests
import json
import sys

lat = input("Enter lat: \n")
lon = input("Enter lon: \n")
request = input("Enter request (desc, wind, temp): \n")

query = "https://api.openweathermap.org/data/2.5/weather?lat=" + lat + "&lon=" + lon + "&appid=f69661f19f90747329bfc3fe6cbc1d0d"
response = requests.get(query)

json_object = json.dumps(response.json(), indent=4)

data = json.loads(json_object)

if request == 'desc':
    print(data['weather'][0]['description'])

elif request == 'temp': 
    print(data['main']['temp'])

elif request == 'wind':
    print(data['wind']['speed'])
    print(data['wind']['deg'])
    print(data['wind']['gust'])

else:
    sys.exit("Invalid request")



# DEBUG 
# with open("sample.json", "w") as outfile:
#     outfile.write(json_object)

