'''
Activity_Recommender.py
--------
Author: Angela Pelky
Created: 3/3/2023
Last Modified: 3/12/2023
Purpose: Activity_Reccomender.py is part of the Weather Adventures system. This program reads through the activities.json file and based on
zoom level and weather data it will spit out reccomendations!

Revision History (Date | Author | Modifications)
----------------------------------------------
3/3/2023  | Angela Pelky | Created initial file
3/7/2023  | Angela Pelky | Added sorting functionality
3/12/2023 | Angela Pelky | Signed off on final version
'''

# importing json library
import json

DEBUG = False

# open activities.json 
with open('activities.json') as f:
  data = json.load(f)

'''
sort(): this function sorts a list of reccomended activites based on location

Parameters:
    reccomended: a list of recommended activities (dictionaries)
    coordinates: a tuple containing two floats

Return: 
    top3: a list of top 3 activities (dictionaries) based on location
'''
def sort(reccomended, coordinates):
    to_sort = {}
    top3 = []
    # loop through the activities in the reccomended list of activities
    for activity in reccomended:
        comp_coord = activity['coordinates']
        distance = ((abs(coordinates[0]) - abs(comp_coord[0]))**2 + (abs(coordinates[1]) - abs(comp_coord[1]))**2)**0.5
        to_sort[distance] = activity
    done_sort = sorted(to_sort)
    # loop through the first 3 recommended activities
    for i in range(3):
        top3.append(to_sort[done_sort[i]])
    # return list of top 3 activites
    return top3 

'''
parse(): this function sorts through the json file and finds activities based on weather and wind parameters

Parameters:
    specific_data: list of activities (dictionaries) from zoom level 1 or 2
    weather: isClear, isRain, isSnoworIce
    wind: Yes or No

Return: 
    reccomended: a list of recommended activities
'''
def parse(specific_data, weather, wind):
    reccomended = []
    # loop through the activities in specific_data
    for activity in specific_data:
        # if it's windy
        if wind == "Yes":
            # if activity can be done in current weather and in the wind
            if activity[weather] == "Yes" and activity["isWind"] == "Yes":
                # add activity to reccomended
                reccomended.append(activity)
        # if it isn't windy
        else: 
            # if activity can be done in current weather
            if activity[weather] == "Yes":
                # add activity to recommended
                reccomended.append(activity)
    # return list of recommended activities
    return reccomended
 
'''
zoom(): this function determines which zoom level the user is on and calls parse() and sort() 

Parameters:
    zoom: an integer of the current map level
    weather:  
    wind:
    coordinates:

Return: 
    top3: a list of top 3 activities
'''
def zoom(zoom, weather, wind, coordinates):

    # if current map is Eugene
    if zoom == 1:
        reccomended = parse(data["groups"][0]["1"], weather, wind)
    # else if current map is Lane County
    elif zoom == 2:
        reccomended = parse(data["groups"][1]["2"], weather, wind)
    
    # initialize top 3 activites based on closest location
    top3 = sort(reccomended, coordinates)
    # return top 3 activities
    return top3

# code to run file separately for testing if debugging
if DEBUG:
    def main():
        zoom(1, "isSnoworIce", "yes", (44.081303, -123.146928))

    if __name__ == "__main__":
        main()
