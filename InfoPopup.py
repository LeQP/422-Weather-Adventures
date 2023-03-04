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

'''
def imageAppender(pathLarge:str, pathSmall:str, sizeLarge:tuple, sizeSmall:tuple):
    midpointLarge = sizeLarge[0] / 2
    midpointSmall = sizeSmall[0] / 2
    position = midpointLarge - midpointSmall
    position = int(position)
    imageLarge = Image.open(pathLarge)
    imageSmall = Image.open(pathSmall)
    imageLarge = imageLarge.resize(sizeLarge)
    imageSmall = imageSmall.resize(sizeSmall)
    imageLarge.paste(imageSmall, (position,position), mask = imageSmall)
    return imageLarge
    

def createPopup():
    pass

if __name__ == "__main__":
    cwd = os.getcwd()
    #cwd = os.path.dirname(os.path.abspath(__file__))
    pathL = cwd + "/images/mapImages/Eugene2x2/1.png"
    pathS = cwd + "/images/weatherSymbols/overcast.png"
    tupleL = (300, 300)
    tupleS = (50, 50)
    imageRet = imageAppender(pathL, pathS, tupleL, tupleS)
    imageRet.show()
