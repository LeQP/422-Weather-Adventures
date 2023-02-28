# This file describes an idea I have for making an interactable map by using images as buttons
# Could not exactly put a new grid on a prexisting image (as of now), so I'm making the images become the grid

# Function for getting buttons
def buttonFunc(coordinates:str):
    inputStr = "Button Clicked at " + coordinates
    labelButton.configure(text=inputStr)


''' Imports '''
# import tkinter module
from tkinter import * 
from tkinter.ttk import *
import tkinter.font as tkFont # For setting text fonts
# Access current working directory
import os
# Manipulate images
from PIL import Image   # Open images
from PIL import ImageTk # Have images available for Tkinter


'''Set up Tkinter Window'''
window = Tk()
window.geometry("750x750")

''' Add image (needs to be PNG) '''
cwd = os.getcwd()
path = cwd + "/testImages/one.png"
openImage = Image.open(path)
resizeImage = openImage.resize((150, 150))
windowImage = ImageTk.PhotoImage(resizeImage)
button1a = Button(window, image = windowImage, command=lambda: buttonFunc("(0,0)"))
button1a.grid(row = 0, column = 0)
button1b = Button(window, image = windowImage, command=lambda: buttonFunc("(0,1)"))
button1b.grid(row = 0, column = 1)
button1c = Button(window, image = windowImage, command=lambda: buttonFunc("(1,0)"))
button1c.grid(row = 1, column = 0)
button1d = Button(window, image = windowImage, command=lambda: buttonFunc("(1,1)"))
button1d.grid(row = 1, column = 1)
labelButton = Label(window, text = "")
labelButton.grid(row = 2, column = 2)



mainloop()