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
3/4/2023 | Joey Le | Further developed createPopup() for a basic format

"""

''' Module needed to form Windows '''
# Import tkinter module to create windows
import tkinter
# For setting text fonts
import tkinter.font as tkFont 
# Import os Access current working directory
import os
# Manipulate images
from PIL import Image   # Open images
# Import weather.py to gather weather data
import weather
from PIL import ImageTk # Have images available for Tkinter

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
    imperial: a bool for if the user wants to see the temperature in fahrenheit and wind direction in miles (True) 
              or temperature in celsius and wind direction in kilometers (False)

Return:
    A tkinter window to view
'''

def createPopup(title:str, lat:float, lon:float, imperial:bool):
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
    # Declare variable to decide imperial or metric values
    unit = ""
    # If the user wants fahrenheit, then set unit to reflect that
    if (imperial == True):
        # API uses "imperial" to search fahrenheit and miles
        unit = "imperial"
    # If the user wants  celsius, then set unit to reflect that
    else:
        # Api uses "metric" to search celsius and kilometers
        unit = "metric"

    ''' Access openWeatherMap API by making a call to its module for its information;'''
    # Acquire all the releveant weather data in a list
    weatherInfo = weather.getWeatherInfo(lat, lon, unit)
    # 0th index = a string description of the weather
    weatherDesc = weatherInfo[0]
     # 1st index = the path to open the relevant weather icon image
    weatherIconPath = os.getcwd() + weatherInfo[1]
    # 2nd index = the temperature of the weather
    tempVal = weatherInfo[2]
    # 3rd index = the average wind speed
    avgWindSpeed = weatherInfo[3]
    # 4th index = the direction of the wind from 0 - 360 degrees
    windDirDeg = weatherInfo[4]
    # 5th index = the path to open the relevant wind direction icon image
    windDirIconPath = os.getcwd() + weatherInfo[5]
    
    ''' Open the different images and make them compatable with Tkinter windows'''
    # Open the weather image for use
    imageWeather = Image.open(weatherIconPath)
    # Open the wind direction image for use
    imageWind = Image.open(windDirIconPath)
    # Reformat the weather iamge to an appropiate size for the pop-up
    imageWeather = imageWeather.resize((200, 200))
    # Reformat the wind direction iamge to an appropiate size for the pop-up
    imageWind = imageWind.resize((200, 200))
    # Allow the weather image to be placed in a Tkinter window for the pop-up
    imageWeather = ImageTk.PhotoImage(imageWeather)
    # Allow the wind direction image to be placed in a Tkinter window for the pop-up
    imageWind = ImageTk.PhotoImage(imageWind)

    ''' Create the text to go alongside the images '''
    # Create the different fonts to use between the heading and body text
    fontStyleHeading = tkFont.Font(family="Arial", size=36) # Heading font font: Arial font of Size 36
    fontStyleBody = tkFont.Font(family="Arial", size=18)    # Body text font: Arial font of size 18
    
    ''' 
    Use frames to organize the weather and wind information into their own distinct groups; 
    also include a frame for the pop-up heading.
    After putting in the applicable images and text, put those frames into the window for viewing.
    '''
    frameHeading = tkinter.Frame(window)    # Heading
    frameWeather = tkinter.Frame(window)    # Weather Information
    frameWind = tkinter.Frame(window)       # Wind direction image
    
    ''' Put the images into labels to apply to the frames'''
    # Create the label for the weather image
    labelWeatherImage = tkinter.Label(frameWeather, image = imageWeather) 
    # Create the label for the wind direction image
    labelWindImage = tkinter.Label(frameWind, image = imageWind) 

    ''' Create the different labels that incorporate the text to put into each frame '''
    labelHeading = tkinter.Label(frameHeading, text = "Title", justify='center', font = fontStyleHeading)                       # Heading/Title text
    labelWeatherText = tkinter.Label(frameWeather, text = "This displays the weather", justify = "right", font = fontStyleBody) # Descriptive text to go alongside weather iamge
    labelWindText = tkinter.Label(frameWind, text = "This displays the wind", justify = "right", font = fontStyleBody)          # Descriptive text to go alongside wind direction iamge

    ''' Place the heading, weather information, and wind direction information into their respective frames'''
    # Place the header text into the Heading Frame
    labelHeading.pack(side = "top")
    frameHeading.grid(row = 0, column = 0)

    # The Weather Frame
    labelWeatherImage.pack(side = "left")   # Place the image into the frame first
    labelWeatherText.pack(side = "left")    # Place the text into the frame second

    # The Wind Frame
    labelWindImage.pack(side = "left")  # Place the image into the frame first
    labelWindText.pack(side = "left")   # Place the text into the frame second
    
    ''' Finally, put the frames onto the tkinter window'''
    frameHeading.grid(row = 0, column = 0)                  # Heading goes first
    frameWeather.grid(row = 1, column = 0, sticky = "W")    # Followed by the weather information
    frameWind.grid(row = 2, column = 0, sticky = "W")       # Then finish the window with the wind information
    
    # Run the window
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
    pathS = cwd + "/images/weatherSymbols/misc.png"
    # The large image dimension
    tupleL = (300, 250)
    # The large image dimension
    tupleS = (50, 78)
    # Run the function
    imageRet = imageAppender(pathL, pathS, tupleL, tupleS)
    # Display the image; comment out if you only see want to see the sample popup
    imageRet.show()
    # Variable that can be changed to view fahrenheit or celsius for sample popup
    viewImperial = True
    # Display sample popup

    createPopup("Spencer Buttle", 50, -126, viewImperial)

