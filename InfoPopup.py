"""
GraphGen.py
--------
Authors: Joey Le
Created: 3/3/2023
Last Modified: 3/3/2023
Purpose: This file creates the additional pop-up windows for when a user wants to learn more about a particular area's weather
and outdoor activities.

Revision History (Date | Author | Modifications)
----------------------------------------------
3/3/2023 | Joey Le | Created initial file
3/3/2023 | Joey Le | Created imageAppender()
3/4/2023 | Joey Le | Created createPopup()
"""

''' Module needed to form Windows '''
# Import tkinter module to create windows
import tkinter
# Import os Access current working directory
import os
# Manipulate images
from PIL import Image   # Open images
# Import weather.py to gather weather data
import weather
from PIL import ImageTk # Have images available for Tkinter

# []
# 1. Weather description: ex. "light rain"
# 2. Path to weather image
# 3. temperature in imperial(fahrenheit), standard(kelvin), metric (celcius)
# 4. average wind speed
# 5. average wind direction
# 6. Path to wind image

#########################################################################################################################################
'''
imageAppender(): this function allows a large image to have a smaller image placed on of it

Parameters:
    pathLarge: a string that provides the path to access the image file for the large image
    pathSmall: a string that provides the path to access the image file for the small image
    sizeLarge: a tuple containing the dimensions for the large image (length, width)
    sizeSmall: a tuple containing the dimensions for the Small image (length, width)

Return
    imageLarge: the large image with the small image placed in the middle of it
'''
def imageAppender(pathLarge:str, pathSmall:str, sizeLarge:tuple, sizeSmall:tuple):
    ''' Calculate the position to place the small image in the center of the large image'''
    # Need the length midpoint of the large image
    midpointLargeX = sizeLarge[0] / 2
    # Need the length midpoint of the small image
    midpointSmallX = sizeSmall[0] / 2
    # Need the width midpoint of the large image
    midpointLargeY = sizeLarge[1] / 2
    # Need the width midpoint of the small image
    midpointSmallY = sizeSmall[1] / 2
    # Calculate the length position to place the image
    positionX = midpointLargeX - midpointSmallX
    # Calculate the width position to place the image
    positionY = midpointLargeY - midpointSmallY
    # Convert the length position to an int since paste() won't accept floats
    positionX = int(positionX)
    # Convert the width position to an int since paste() won't accept floats
    positionY = int(positionY)
    # Open the large image to use
    imageLarge = Image.open(pathLarge)
    # Open the small image to use
    imageSmall = Image.open(pathSmall)
    # Resize the large image with the provided dimension tuple
    imageLarge = imageLarge.resize(sizeLarge)
    # Resize the small image with the provided dimension tuple
    imageSmall = imageSmall.resize(sizeSmall)
    # Put the small image on the large image
    imageLarge.paste(imageSmall, (positionX,positionY), mask = imageSmall)
    # Return the large image with the appended small image
    return imageLarge



'''
createPopup(): a function that creates a small tkinter pop-up window when a user wishes to know more
               about a specific region on the grid 

Parameters:
    title: a string that 
    lat: a float that is the lattitude of the specific region
    lon: a float that is the longitude of the specific region
    fahrenheit: a bool for if the user wants to see the temperature in fahrenheit(True) or celsius(False)

Return
    imageLarge: the large image with the small image placed in the middle of it
'''

def createPopup(title:str, lat:float, lon:float, fahrenheit:bool):
    '''
    Set up the Tkinter Window for the pop-up
    '''
    # Initialize the window
    window = tkinter.Tk()
    # Initialize the window's dimensions
    window.geometry("500x500")
    # Set the window's title
    window.title(title)
    #window.config(bg="blue")
    ''' Use the fahrenheit parameter to determine the weather search to result in fahrenheit or celcius'''
    # Declare variable to perform the fahrenheit or celsius search
    unit = ""
    # If the user wants fahrenheit, then set unit to reflect that
    if (fahrenheit == True):
        # API uses "imperial" to search fahrenheit temperatures
        unit = "imperial"
    # If the user wants  celsius, then set unit to reflect that
    else:
        # Api uses "metric" to search celsius temperatures
        unit = "metric"
    weatherInfo = weather.getWeatherInfo(lat, lon, unit)
    weatherDesc = weatherInfo[0]
    weatherIconPath = os.getcwd() + weatherInfo[1]
    tempVal = weatherInfo[2]
    avgWindSpeed = weatherInfo[3]
    windDirDeg = weatherInfo[4]
    windDirIconPath = os.getcwd() + weatherInfo[5]


    imageWeather = Image.open(weatherIconPath)
    imageWind = Image.open(windDirIconPath)

    imageWeather = imageWeather.resize((200, 200))
    imageWind = imageWind.resize((200, 200))

    imageWeather = ImageTk.PhotoImage(imageWeather)
    imageWind = ImageTk.PhotoImage(imageWind)

    labelWeather = tkinter.Label(window, image = imageWeather) 
    labelWind = tkinter.Label(window, image = imageWind) 

    labelWeather.grid(row = 0, column = 0, sticky = "W")
    labelWind.grid(row = 1, column = 0, sticky = "W")

    # []
    # 1. Weather description: ex. "light rain"
    # 2. Path to weather image
    # 3. temperature in imperial(fahrenheit), standard(kelvin), metric (celcius)
    # 4. average wind speed
    # 5. average wind direction
    # 6. Path to wind image


    window.mainloop()


''' Run the program on it is own for debugging purposes'''
if __name__ == "__main__":
    # Get the current working directory
    cwd = os.getcwd()
    #cwd = os.path.dirname(os.path.abspath(__file__))
    ''' Feel free to change the paths and tuple sizes to test other images and sizes '''
    # The large image 
    pathL = cwd + "/images/mapImages/Eugene2x2/1.png"
    # The small image 
    pathS = cwd + "/images/weatherSymbols/overcast.png"
    # The large image dimension
    tupleL = (300, 250)
    # The large image dimension
    tupleS = (50, 78)
    # Run the function
    imageRet = imageAppender(pathL, pathS, tupleL, tupleS)
    # Display the image; comment out if you only see want to see the sample popup
    #imageRet.show()
    # Variable that can be changed to view fahrenheit or celsius for sample popup
    viewFahrenheit = True
    # Display sample popup
    createPopup("Spencer Buttle", 49.99115780445145, -123.09715087568385, viewFahrenheit)

