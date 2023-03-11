'''
Activity_Reccomender.py is part of the Weather Adventures system. This program reads through the activities.json file and based on
zoom level and weather data it will spit out reccomendations!

Author: Angela Pelky
Date: 03/03/2023
'''

# importing json library
import json

DEBUG = True
 
with open('activities.json') as f:
  data = json.load(f)

def sort(reccomended, coordinates):
    to_sort = {}
    top3 = []
    for activity in reccomended:
        comp_coord = activity['coordinates']
        distance = ((abs(coordinates[0]) - abs(comp_coord[0]))**2 + (abs(coordinates[1]) - abs(comp_coord[1]))**2)**0.5
        to_sort[distance] = activity
    done_sort = sorted(to_sort)
    for i in range(3):
        top3.append(to_sort[done_sort[i]])
    return top3 

def parse(specific_data, weather, wind):
    reccomended = []
    for activity in specific_data:
        if wind == "Yes":
            if activity[weather] == "Yes" and activity["isWind"] == "Yes":
                reccomended.append(activity)
        else: 
            if activity[weather] == "Yes":
                reccomended.append(activity)
    return reccomended
 
def zoom(zoom, weather, wind, coordinates):
    if zoom == 1:
        reccomended = parse(data["groups"][0]["1"], weather, wind)
    elif zoom == 2:
        reccomended = parse(data["groups"][1]["2"], weather, wind)
    
    top3 = sort(reccomended, coordinates)
    return top3

if DEBUG:
    def main():
        zoom(1, "isSnoworIce", "yes", (44.081303, -123.146928))

    if __name__ == "__main__":
        main()
