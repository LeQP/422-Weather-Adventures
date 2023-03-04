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
"""


''' Module needed to form Windows '''
# import tkinter module
import tkinter
from tkinter import ttk

# Access current working directory
import os
# Manipulate images
from PIL import Image   # Open images
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
    

def createPopup():
    pass

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
    tupleL = (300, 300)
    # The large image dimension
    tupleS = (50, 50)
    # Run the function
    imageRet = imageAppender(pathL, pathS, tupleL, tupleS)
    # Display the image
    imageRet.show()
