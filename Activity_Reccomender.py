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

def parse(specific_data, weather):
    reccomended = []
    for activity in specific_data:
        if activity[weather] == "Yes":
            reccomended.append(activity)
    return reccomended
 
def zoom(zoom, weather):
    if zoom == 1:
        reccomended = parse(data["groups"][0]["1"], weather)
    elif zoom == 2:
        reccomended = parse(data["groups"][1]["2"], weather)

    return reccomended

if DEBUG:
    def main():
        print(zoom(2, "isSnoworIce"))

    if __name__ == "__main__":
        main()
