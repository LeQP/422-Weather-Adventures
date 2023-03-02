'''
By Joey Le
This file describes an idea I have for making an interactable map by using images as buttons
Could not exactly put a new grid on a prexisting image (as of now), so I'm making the images become the grid 
'''

''' Function for getting buttons; provide label for number clicked '''
def buttonFunc(coordinates:str):
    inputStr = "Button Clicked at " + coordinates
    labelButton.configure(text=inputStr)

''' Function for the Zoom Buttons; update the number images and update button states  '''
#   zoom in = decrease val, zoom out = increase val
#   Use .configure(image =) to update image
#   Update num after images are reconfigured for prog to know which number it is at
#   Disable buttons with button["state"] to prevent any further zooming in or out
def zoom(closer:bool):
    # Acces global variable with global
    global num 
    # Zoom Out
    if (closer == False):
        # First if-then will not happen
        if (num == 3):
            labelZ.configure(text = "Can't zoom out any farther")
        # Change 1 into 2
        elif (num == 1):
            labelZ.configure(text = "Number zoomed out to 2")
            buttonA.configure(image = windowImage2)
            buttonB.configure(image = windowImage2)
            buttonC.configure(image = windowImage2)
            buttonD.configure(image = windowImage2)
            num = 2
            buttonIn["state"] = NORMAL
         # Change 2 into 3
        elif (num == 2):
            labelZ.configure(text = "Number zoomed out to 3")
            buttonA.configure(image = windowImage3)
            buttonB.configure(image = windowImage3)
            buttonC.configure(image = windowImage3)
            buttonD.configure(image = windowImage3)
            num = 3
            buttonOut["state"] = DISABLED
    # Zoom in
    else:
         # First if-then will not happen
        if (num == 1):
            labelZ.configure(text = "Can't zoom in any closer")
        # Change 3 into 2
        elif (num == 3):
            labelZ.configure(text = "Number zoomed in to 2")
            buttonA.configure(image = windowImage2)
            buttonB.configure(image = windowImage2)
            buttonC.configure(image = windowImage2)
            buttonD.configure(image = windowImage2)
            num = 2
            buttonOut["state"] = NORMAL
        # Change 2 into 1
        elif (num == 2):
            labelZ.configure(text = "Number zoomed in to 1")
            buttonA.configure(image = windowImage1)
            buttonB.configure(image = windowImage1)
            buttonC.configure(image = windowImage1)
            buttonD.configure(image = windowImage1)
            num = 1
            buttonIn["state"] = DISABLED
        
''' Change the display of buttons '''
def buttonVis(visibility:bool):
    if (visibility == True):
        # Re-insert buttons with grid placement
        buttonA.grid(row = 0, column = 0)
        buttonB.grid(row = 0, column = 1)
        buttonC.grid(row = 1, column = 0)
        buttonD.grid(row = 1, column = 1)
        buttonShow["state"] = DISABLED
        buttonHide["state"] = NORMAL
    else:
        # Use .grid_forget() to remove buttons from the window, but not delete them within the code
        buttonA.grid_forget()
        buttonB.grid_forget()
        buttonC.grid_forget()
        buttonD.grid_forget()
        buttonShow["state"] = NORMAL
        buttonHide["state"] = DISABLED
        

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
window.geometry("750x1000")

''' Add image (needs to be PNG) '''
cwd = os.getcwd()
# 1. Set the path
path1 = cwd + "/testImages/one.png"
path2 = cwd + "/testImages/two.png"
path3 = cwd + "/testImages/three.png"

# 2. Open the images
openImage1 = Image.open(path1)
openImage2 = Image.open(path2)
openImage3 = Image.open(path3)

# 3. Resize them
resizeImage1 = openImage1.resize((240, 240))
resizeImage2 = openImage2.resize((160, 160))
resizeImage3 = openImage3.resize((80, 80))

# 4. Set them to be on Tkinter
windowImage1 = ImageTk.PhotoImage(resizeImage1)
windowImage2 = ImageTk.PhotoImage(resizeImage2)
windowImage3 = ImageTk.PhotoImage(resizeImage3)

# Place the image buttons using the .grid()
buttonA = Button(window, image = windowImage1, command=lambda: buttonFunc("(0,0)"))
buttonA.grid(row = 0, column = 0)
buttonB = Button(window, image = windowImage1, command=lambda: buttonFunc("(0,1)"))
buttonB.grid(row = 0, column = 1)
buttonC = Button(window, image = windowImage1, command=lambda: buttonFunc("(1,0)"))
buttonC.grid(row = 1, column = 0)
buttonD = Button(window, image = windowImage1, command=lambda: buttonFunc("(1,1)"))
buttonD.grid(row = 1, column = 1)
labelButton = Label(window, text = "")
labelButton.grid(row = 1, column = 2)

# num is used to keep track of which number is on display
num = 1

''' Additional property-changing buttons '''
# Add buttons to change the image
buttonIn = Button(window, text = "ZOOM IN", command=lambda: zoom(True))
buttonOut = Button(window, text = "ZOOM OUT", command=lambda: zoom(False))
buttonIn.grid(row = 5, column = 0)
buttonOut.grid(row = 5, column = 1)
labelZ = Label(window, text = "")
labelZ.grid(row = 3, column = 2)
buttonIn["state"] = DISABLED

# Add buttons to change visbility
#   Note: Changing the buttons's presence causes shift in labels, widgets, etc in the window
buttonHide = Button(window, text = "Hide Buttons", command=lambda: buttonVis(False))
buttonShow = Button(window, text = "Show Buttons", command=lambda: buttonVis(True))
buttonHide.grid(row = 6, column = 0)
buttonShow.grid(row = 6, column = 1)
buttonShow["state"] = DISABLED


mainloop()