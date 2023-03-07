"""
weather.py
--------
Authors: Peter Nelson
Created: 2/25/2023
Last Modified: 3/3/2023
Purpose: This file queries openweathermap API with user input and parses response

"""


# requests for api calls
import requests
# json for json handling
import json

def getWeatherInfo(lat, lon, units):

    # create api query string from input
    query = "https://api.openweathermap.org/data/2.5/weather?lat=" + str(lat) + "&lon=" + str(lon) + "&units=" + units + "&appid=f69661f19f90747329bfc3fe6cbc1d0d"
    # call api 
    response = requests.get(query)
    # fill weatherReport with api response 
    weatherReport = json.dumps(response.json(), indent=4)

    # DEBUG write weatherReport
    with open("sample.json", "w") as outfile:
        outfile.write(weatherReport)

    # load weather report into data container
    data = json.loads(weatherReport)
    
    # get weather description 
    weatherDesc = data['weather'][0]['main']
    # create path string to correct weather symbol image
    weatherSymStr = "/images/weatherSymbols/" + weatherSymLookup(weatherDesc)
    
    # get temperature
    temp = data['main']['temp']

    # get wind data
    windSpeed = int(data['wind']['speed'])
    windDir = int(data['wind']['deg'])

    # round wind direction to nearest 15 degrees
    if (windDir % 15) < 7:
        windDirRounded = windDir - (windDir % 15)
    else:
        windDirRounded = windDir + (15 - windDir % 15)

    # if rounded wind direction underflows or overflows 360 degrees, set to max or min
    if windDirRounded < 0:
        windDirRounded = 0
    elif windDirRounded > 345:
        windDirRounded = 345

    # create path string to correct wind direction image
    windSymFPath = "/images/weatherSymbols/w" + str(windDirRounded) + ".png"

    visibility = int(data['visibility'])
    humidity = int(data['main']['humidity'])

    # create return information list
    infoList = weatherSymStr, windSymFPath, weatherDesc, temp, windSpeed, windDirRounded, visibility, humidity
    # return information list
    return infoList            

def weatherSymLookup(weatherStr):

    # initialize weather description dictionary
    dict = {
        "Drizzle" : "rain.png",
        "Rain": "rain.png",
        "Snow": "snow.png",
        "snow": "snow.png",
        "Clear": "clear.png",
        "Clouds": "clouds.png",
        "Mist" : "misc.png",
        "Smoke" : "misc.png",
        "Haze" : "misc.png",
        "Dust" : "misc.png",
        "Fog" : "misc.png",
        "Sand" : "misc.png",
        "Dust" : "misc.png",
        "Ash" : "misc.png",
        "Squall" : "misc.png",
        "Tornado" : "misc.png"
    }

    # return correct image name from weather description
    return dict[weatherStr]

# DEBUG DEBUG DEBUG
if __name__ == "__main__":
    lat = input("Enter lat: \n")
    lon = input("Enter lon: \n")
    units = input("Enter units: (imperial, standard, metric) \n")
    infolist = getWeatherInfo(lat, lon, units)
    print(infolist)

    