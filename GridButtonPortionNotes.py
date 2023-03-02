'''
By Joey Le
This file is a continuation of GridButtonNotes 
in where I try to alter the dimensions of a grid by zooming in and out instead of a constant 2x2
'''
# Side note when working on this:
#   To get the button images to be perfectly side by side, I had to make sure all the other widgets (Zoom buttons and labels)
#   had to not be in the same row and column as any of the button. That is why the zoom buttons and texts are displayed not 
#   directly below or to the side of the button grid.
#
#   Also, the size between numbers slightly differs but we can fine tune that as we work on the project
#
#   For each button list, the placement into Tkinter is something like
#       0 1 2 
#       3 4 5
#       6 7 8 ...


''' Function to display the Tkinter window coordinate of the button'''
def buttonFunc(coordinates:str):
    inputStr = "Button Clicked at " + coordinates
    labelButton.configure(text=inputStr)

''' Function for the Zoom Buttons; It will change the dimenisions of the grid and number displayed  '''
def zoom(closer:bool):
    global num 
    if (closer == False):
        # Change 1 into 2
        if (num == 1):
            labelZ.configure(text = "Number zoomed out to 2")
            oneToTwo()
            num = 2
            buttonIn["state"] = NORMAL
        # Change 2 into 3
        elif (num == 2):
            labelZ.configure(text = "Number zoomed out to 3")
            twoToThree()
            num = 3
            buttonOut["state"] = DISABLED
    else:
        # Change 3 into 2
        if (num == 3):
            labelZ.configure(text = "Number zoomed in to 2")
            threeToTwo()
            num = 2
            buttonOut["state"] = NORMAL
        # Change 2 into 1
        elif (num == 2):
            labelZ.configure(text = "Number zoomed in to 1")
            twoToOne()
            num = 1
            buttonIn["state"] = DISABLED

''' Functions to change X into Y (xToY)'''
# Each one starts by removing the current buttons for X from the window, but not destroy them
# Next, it will add each button for Y into the tkinter window.
def oneToTwo():
    for i in range(len(button1)):
        button1[i].grid_forget()
    for i in range(3):
        for j in range(3):
            button2[i * 3 + j].grid(row = i*2, column = j*2, rowspan = 2, columnspan = 2)

def twoToThree():
    for i in range(len(button2)):
        button2[i].grid_forget()
    for i in range(6):
        for j in range(6):
            button3[i * 6 + j].grid(row = i, column = j, rowspan = 1, columnspan = 1)

def threeToTwo(): 
    for i in range(len(button3)):
        button3[i].grid_forget()
    for i in range(3):
        for j in range(3):
            button2[i * 3 + j].grid(row = i*2, column = j*2, rowspan = 2, columnspan = 2)
    
def twoToOne(): 
    for i in range(len(button2)):
        button2[i].grid_forget()
    for i in range(2):
        for j in range(2):
            button1[i * 2 + j].grid(row = i*3, column = j*3, rowspan = 3, columnspan = 3)


    
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
window.geometry("1000x1000")

''' Add image (needs to be PNG) '''
cwd = os.getcwd()
path1 = cwd + "/testImages/one.png"
path2 = cwd + "/testImages/two.png"
path3 = cwd + "/testImages/three.png"
openImage1 = Image.open(path1)
openImage2 = Image.open(path2)
openImage3 = Image.open(path3)
resizeImage1 = openImage1.resize((240, 240))
resizeImage2 = openImage2.resize((160, 160))
resizeImage3 = openImage3.resize((80, 80))
windowImage1 = ImageTk.PhotoImage(resizeImage1)
windowImage2 = ImageTk.PhotoImage(resizeImage2)
windowImage3 = ImageTk.PhotoImage(resizeImage3)

''' Set up each button within their grid set'''
# Put all the buttons for viewing 1 into button1; 2x2
button1 = []
button1.append(Button(window, image = windowImage1, command=lambda: buttonFunc("(0,0)")))
button1.append(Button(window, image = windowImage1, command=lambda: buttonFunc("(0,1)")))
button1.append(Button(window, image = windowImage1, command=lambda: buttonFunc("(1,0)")))
button1.append(Button(window, image = windowImage1, command=lambda: buttonFunc("(1,1)")))

# Put all the buttons for viewing 2 into button2; 3x3
button2 = []
button2.append(Button(window, image = windowImage2, command=lambda: buttonFunc("(0,0)")))
button2.append(Button(window, image = windowImage2, command=lambda: buttonFunc("(0,1)")))
button2.append(Button(window, image = windowImage2, command=lambda: buttonFunc("(0,2)")))
button2.append(Button(window, image = windowImage2, command=lambda: buttonFunc("(1,0)")))
button2.append(Button(window, image = windowImage2, command=lambda: buttonFunc("(1,1)")))
button2.append(Button(window, image = windowImage2, command=lambda: buttonFunc("(1,2)")))
button2.append(Button(window, image = windowImage2, command=lambda: buttonFunc("(2,0)")))
button2.append(Button(window, image = windowImage2, command=lambda: buttonFunc("(2,1)")))
button2.append(Button(window, image = windowImage2, command=lambda: buttonFunc("(2,2)")))

# Put all the buttons for viewing 3 into button2; 6x6
button3 = []
button3.append(Button(window, image = windowImage3, command=lambda: buttonFunc("(0,0)")))
button3.append(Button(window, image = windowImage3, command=lambda: buttonFunc("(0,1)")))
button3.append(Button(window, image = windowImage3, command=lambda: buttonFunc("(0,2)")))
button3.append(Button(window, image = windowImage3, command=lambda: buttonFunc("(0,3)")))
button3.append(Button(window, image = windowImage3, command=lambda: buttonFunc("(0,4)")))
button3.append(Button(window, image = windowImage3, command=lambda: buttonFunc("(0,5)")))
button3.append(Button(window, image = windowImage3, command=lambda: buttonFunc("(1,0)")))
button3.append(Button(window, image = windowImage3, command=lambda: buttonFunc("(1,1)")))
button3.append(Button(window, image = windowImage3, command=lambda: buttonFunc("(1,2)")))
button3.append(Button(window, image = windowImage3, command=lambda: buttonFunc("(1,3)")))
button3.append(Button(window, image = windowImage3, command=lambda: buttonFunc("(1,4)")))
button3.append(Button(window, image = windowImage3, command=lambda: buttonFunc("(1,5)")))
button3.append(Button(window, image = windowImage3, command=lambda: buttonFunc("(2,0)")))
button3.append(Button(window, image = windowImage3, command=lambda: buttonFunc("(2,1)")))
button3.append(Button(window, image = windowImage3, command=lambda: buttonFunc("(2,2)")))
button3.append(Button(window, image = windowImage3, command=lambda: buttonFunc("(2,3)")))
button3.append(Button(window, image = windowImage3, command=lambda: buttonFunc("(2,4)")))
button3.append(Button(window, image = windowImage3, command=lambda: buttonFunc("(2,5)")))
button3.append(Button(window, image = windowImage3, command=lambda: buttonFunc("(3,0)")))
button3.append(Button(window, image = windowImage3, command=lambda: buttonFunc("(3,1)")))
button3.append(Button(window, image = windowImage3, command=lambda: buttonFunc("(3,2)")))
button3.append(Button(window, image = windowImage3, command=lambda: buttonFunc("(3,3)")))
button3.append(Button(window, image = windowImage3, command=lambda: buttonFunc("(3,4)")))
button3.append(Button(window, image = windowImage3, command=lambda: buttonFunc("(3,5)")))
button3.append(Button(window, image = windowImage3, command=lambda: buttonFunc("(4,0)")))
button3.append(Button(window, image = windowImage3, command=lambda: buttonFunc("(4,1)")))
button3.append(Button(window, image = windowImage3, command=lambda: buttonFunc("(4,2)")))
button3.append(Button(window, image = windowImage3, command=lambda: buttonFunc("(4,3)")))
button3.append(Button(window, image = windowImage3, command=lambda: buttonFunc("(4,4)")))
button3.append(Button(window, image = windowImage3, command=lambda: buttonFunc("(4,5)")))
button3.append(Button(window, image = windowImage3, command=lambda: buttonFunc("(5,0)")))
button3.append(Button(window, image = windowImage3, command=lambda: buttonFunc("(5,1)")))
button3.append(Button(window, image = windowImage3, command=lambda: buttonFunc("(5,2)")))
button3.append(Button(window, image = windowImage3, command=lambda: buttonFunc("(5,3)")))
button3.append(Button(window, image = windowImage3, command=lambda: buttonFunc("(5,4)")))
button3.append(Button(window, image = windowImage3, command=lambda: buttonFunc("(5,5)")))


# Set up the inital buttons to display 1
button1[0].grid(row = 0, column = 0, ipadx = 100, ipady = 100, rowspan = 3, columnspan = 3)
button1[1].grid(row = 0, column = 3, padx = 100, pady = 100, rowspan = 3, columnspan = 3)
button1[2].grid(row = 3, column = 0, rowspan = 3, columnspan = 3)
button1[3].grid(row = 3, column = 3, rowspan = 3, columnspan = 3)


# num is used to keep track of which number is on display
num = 1

''' Incorporate additional labels and zoom buttons '''
# Add buttons to change the image
buttonIn = Button(window, text = "ZOOM IN", command=lambda: zoom(True))
buttonOut = Button(window, text = "ZOOM OUT", command=lambda: zoom(False))
buttonIn.grid(row = 6, column = 7)
buttonOut.grid(row = 6, column = 8)

# Labels to display when using the zoom button and when a grid button is clicked
labelZ = Label(window, text = "")
labelZ.grid(row = 7, column = 7)
buttonIn["state"] = DISABLED
labelButton = Label(window, text = "")
labelButton.grid(row = 8, column = 7)


mainloop()