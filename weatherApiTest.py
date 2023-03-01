# input: lat, long, request type

import requests
import json
import sys

def getWeatherInfo(lat, lon, units):

    query = "https://api.openweathermap.org/data/2.5/weather?lat=" + lat + "&lon=" + lon + "&units=" + units + "&appid=f69661f19f90747329bfc3fe6cbc1d0d"
    response = requests.get(query)

    json_object = json.dumps(response.json(), indent=4)

    data = json.loads(json_object)

    print("WEATHER DESCRIPTION: " + data['weather'][0]['description'])
    weatherSymStr = "/images/weatherSymbols/" + weatherSymLookup(data['weather'][0]['description'])
    print("WEATHER SYMBOL PATH: " + weatherSymStr)
 
    print("TEMP: "+ str(data['main']['temp']))

    print("AVG WIND SPEED: " + str(int(data['wind']['speed']) + int(data['wind']['gust']) / 2))
    print("WIND DIRECTION: " + str(data['wind']['deg']))
    
    windDir = int(data['wind']['deg'])
    if (windDir % 15) < 7:
        windDirRounded = windDir - (15 - windDir % 15)
    else:
        windDirRounded = windDir + (15 - windDir % 15)

    # not sure about this logic
    if windDirRounded < 0:
        windDirRounded = 0
    elif windDirRounded > 345:
        windDirRounded = 345

    windSymFPath = "/images/weatherSymbols/w" + str(windDirRounded)
    print("WIND SYMBOL PATH: " + windSymFPath)            

def weatherSymLookup(weatherStr):

    dict = {
        "few clouds": "broken_clouds.png",
        "scattered clouds": "broken_clouds.png",
        "broken clouds": "overcast.png",
        "overcast clouds": "overcast.png",

        "clear sky": "clear.png",

        "light snow": "snow.png",
        "snow": "snow.png",
        "heavy snow": "snow.png",

        "light rain": "rain.png",
        "heavy intensity rain": "rain.png",
        "moderate rain": "rain.png",
        "very heavy rain": "rain.png",

        # add more cases
        "drizzle" : "rain.png"
    }

    return dict[weatherStr]


lat = input("Enter lat: \n")
lon = input("Enter lon: \n")
units = input("Enter units: (imperial, standard, metric) \n")
getWeatherInfo(lat, lon, units)

