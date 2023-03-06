'''
By Melodie Collins
This file is based on GridButtonPortionNotes.py 
'''
# Side note when working on this:
#   To get the button images to be perfectly side by side, I had to make sure all the other widgets (Zoom buttons and labels)
#   had to not be in the same row and column as any of the button. That is why the zoom buttons and texts are displayed not 
#   directly below or to the side of the button grid.
#
#   Also, the size between numbers slightly differs but we can fine tune that as we work on the project; can use ipadx and ipady to help with this
#
#   For each button list, the placement into Tkinter is something like
#       0 1 2 
#       3 4 5
#       6 7 8 ...

# Set up global map coordinates for Eugene buttons
COORDINATES_EUG_1 = (44.081303, -123.146928)
COORDINATES_EUG_2 = (44.083770, -123.046695)
COORDINATES_EUG_3 = (44.019559, -123.143883)
COORDINATES_EUG_4 = (44.015600, -123.047490)

# Set up global map coordinates for Lane County buttons
COORDINATES_LANE_1 = (44.169810, -123.959655)
COORDINATES_LANE_2 = (44.140252, -123.489990)
COORDINATES_LANE_3 = (44.199846, -122.998352)
COORDINATES_LANE_4 = (44.178182, -122.492981)
COORDINATES_LANE_5 = (44.191969, -122.006836)
COORDINATES_LANE_6 = (44.140252, -123.489990)
COORDINATES_LANE_7 = (43.830482, -123.487243)
COORDINATES_LANE_8 = (43.856234, -123.006592)
COORDINATES_LANE_9 = (43.850292, -122.471008)
COORDINATES_LANE_10 = (43.842369, -121.987610)
COORDINATES_LANE_11 = (43.540004, -123.995361)
COORDINATES_LANE_12 = (43.541001, -123.486545)
COORDINATES_LANE_13 = (43.528811, -122.955678)
COORDINATES_LANE_14 = (43.549707, -122.463245)
COORDINATES_LANE_15 = (43.523586, -122.040473)

''' Function to display the Tkinter window coordinate of the button'''
def buttonFunc(coordinates:str):
    inputStr = "Button Clicked at " + coordinates
    labelButton.configure(text=inputStr)

# Remove current map title
def on_click():
   label.after(0, label.destroy())

''' Function for the Zoom Buttons; It will change the dimensions of the grid and number displayed  '''
def zoom(closer:bool):
    global num 
    if (closer == False):
        # Change 1 into 2
        oneToTwo()
        num = 2
        # Remove current map title
        on_click()
        # Set the map title to Lane County
        mapTitle(num)
        buttonIn["state"] = NORMAL
        buttonOut["state"] = DISABLED
    else:
        # Change 2 into 1
        twoToOne()
        num = 1
        # Remove current map title
        on_click()
        # Set the map title to Eugene
        mapTitle(num)
        buttonIn["state"] = DISABLED
        buttonOut["state"] = NORMAL

''' Functions to change X into Y (xToY)'''
# Each one starts by removing the current buttons for X from the window, but not destroy them
# Next, it will add each button for Y into the tkinter window.
def oneToTwo():
    for i in range(len(button1)):
        button1[i].grid_forget()
    for i in range(3):
        for j in range(5):
            button2[i * 5 + j].grid(row = i*2, column = j*2, rowspan = 2, columnspan = 2)
    
def twoToOne(): 
    for i in range(len(button2)):
        button2[i].grid_forget()
    for i in range(2):
        for j in range(2):
            button1[i * 2 + j].grid(row = i*3, column = j*5, rowspan = 3, columnspan = 5, ipadx = 2.5, ipady = 2.5)


''' Imports '''
# import tkinter module
from tkinter import * 
import tkinter as tk
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

'''Set up a frame for the zoom buttons'''
#root = Tk()
#root.geometry("1000x1000")
#frame = Frame(root)
#frame.pack()

#bottomframe = Frame(root)
#bottomframe.pack( side = BOTTOM )

#Set the Title of Tkinter window
window.title("Weather Adventures")

''' Add image (needs to be PNG) '''
cwd = os.getcwd()

path4 = cwd + "/images/mapImages/Eugene2x2/1.png"
path5 = cwd + "/images/mapImages/Eugene2x2/2.png"
path6 = cwd + "/images/mapImages/Eugene2x2/3.png"
path7 = cwd + "/images/mapImages/Eugene2x2/4.png"

path8 = cwd + "/images/mapImages/LaneCounty5x3/1.png"
path9 = cwd + "/images/mapImages/LaneCounty5x3/2.png"
path10 = cwd + "/images/mapImages/LaneCounty5x3/3.png"
path11 = cwd + "/images/mapImages/LaneCounty5x3/4.png"
path12 = cwd + "/images/mapImages/LaneCounty5x3/5.png"
path13 = cwd + "/images/mapImages/LaneCounty5x3/6.png"
path14 = cwd + "/images/mapImages/LaneCounty5x3/7.png"
path15 = cwd + "/images/mapImages/LaneCounty5x3/8.png"
path16 = cwd + "/images/mapImages/LaneCounty5x3/9.png"
path17 = cwd + "/images/mapImages/LaneCounty5x3/10.png"
path18 = cwd + "/images/mapImages/LaneCounty5x3/11.png"
path19 = cwd + "/images/mapImages/LaneCounty5x3/12.png"
path20 = cwd + "/images/mapImages/LaneCounty5x3/13.png"
path21 = cwd + "/images/mapImages/LaneCounty5x3/14.png"
path22 = cwd + "/images/mapImages/LaneCounty5x3/15.png"

#def addImage(path:str)
    #openImage = Image.open(path)
    #return openImage

#def resizeImage(openImage, size:int)
    #resizeImage = openImage.resize((size, size))
    #return resizeImage


openImage4 = Image.open(path4)
openImage5 = Image.open(path5)
openImage6 = Image.open(path6)
openImage7 = Image.open(path7)

openImage8 = Image.open(path8)
openImage9 = Image.open(path9)
openImage10 = Image.open(path10)
openImage11 = Image.open(path11)
openImage12 = Image.open(path12)
openImage13 = Image.open(path13)
openImage14 = Image.open(path14)
openImage15 = Image.open(path15)
openImage16 = Image.open(path16)
openImage17 = Image.open(path17)
openImage18 = Image.open(path18)
openImage19 = Image.open(path19)
openImage20 = Image.open(path20)
openImage21 = Image.open(path21)
openImage22 = Image.open(path22)

resizeImage4 = openImage4.resize((350, 350))
resizeImage5 = openImage5.resize((350, 350))
resizeImage6 = openImage6.resize((350, 350))
resizeImage7 = openImage7.resize((350, 350))

resizeImage8 = openImage8.resize((160, 160))
resizeImage9 = openImage9.resize((160, 160))
resizeImage10 = openImage10.resize((160, 160))
resizeImage11 = openImage11.resize((160, 160))
resizeImage12 = openImage12.resize((160, 160))
resizeImage13 = openImage13.resize((160, 160))
resizeImage14 = openImage14.resize((160, 160))
resizeImage15 = openImage15.resize((160, 160))
resizeImage16 = openImage16.resize((160, 160))
resizeImage17 = openImage17.resize((160, 160))
resizeImage18 = openImage18.resize((160, 160))
resizeImage19 = openImage19.resize((160, 160))
resizeImage20 = openImage20.resize((160, 160))
resizeImage21 = openImage21.resize((160, 160))
resizeImage22 = openImage22.resize((160, 160))

windowImage4 = ImageTk.PhotoImage(resizeImage4)
windowImage5 = ImageTk.PhotoImage(resizeImage5)
windowImage6 = ImageTk.PhotoImage(resizeImage6)
windowImage7 = ImageTk.PhotoImage(resizeImage7)

windowImage8 = ImageTk.PhotoImage(resizeImage8)
windowImage9 = ImageTk.PhotoImage(resizeImage9)
windowImage10 = ImageTk.PhotoImage(resizeImage10)
windowImage11 = ImageTk.PhotoImage(resizeImage11)
windowImage12 = ImageTk.PhotoImage(resizeImage12)
windowImage13 = ImageTk.PhotoImage(resizeImage13)
windowImage14 = ImageTk.PhotoImage(resizeImage14)
windowImage15 = ImageTk.PhotoImage(resizeImage15)
windowImage16 = ImageTk.PhotoImage(resizeImage16)
windowImage17 = ImageTk.PhotoImage(resizeImage17)
windowImage18 = ImageTk.PhotoImage(resizeImage18)
windowImage19 = ImageTk.PhotoImage(resizeImage19)
windowImage20 = ImageTk.PhotoImage(resizeImage20)
windowImage21 = ImageTk.PhotoImage(resizeImage21)
windowImage22 = ImageTk.PhotoImage(resizeImage22)

''' Set up each button within their grid set'''
# Put all the buttons for viewing Eugene into button1; 2x2
button1 = []
button1.append(Button(window, image = windowImage4, command=lambda: buttonFunc("(0,0)")))
button1.append(Button(window, image = windowImage5, command=lambda: buttonFunc("(0,1)")))
button1.append(Button(window, image = windowImage6, command=lambda: buttonFunc("(1,0)")))
button1.append(Button(window, image = windowImage7, command=lambda: buttonFunc("(1,1)")))

# Put all the buttons for viewing Lane County into button2; 5x3
button2 = []
button2.append(Button(window, image = windowImage8, command=lambda: buttonFunc("(0,0)")))
button2.append(Button(window, image = windowImage9, command=lambda: buttonFunc("(0,1)")))
button2.append(Button(window, image = windowImage10, command=lambda: buttonFunc("(0,2)")))
button2.append(Button(window, image = windowImage11, command=lambda: buttonFunc("(0,3)")))
button2.append(Button(window, image = windowImage12, command=lambda: buttonFunc("(0,4)")))
button2.append(Button(window, image = windowImage13, command=lambda: buttonFunc("(1,0)")))
button2.append(Button(window, image = windowImage14, command=lambda: buttonFunc("(1,1)")))
button2.append(Button(window, image = windowImage15, command=lambda: buttonFunc("(1,2)")))
button2.append(Button(window, image = windowImage16, command=lambda: buttonFunc("(1,3)")))
button2.append(Button(window, image = windowImage17, command=lambda: buttonFunc("(1,4)")))
button2.append(Button(window, image = windowImage18, command=lambda: buttonFunc("(2,0)")))
button2.append(Button(window, image = windowImage19, command=lambda: buttonFunc("(2,1)")))
button2.append(Button(window, image = windowImage20, command=lambda: buttonFunc("(2,2)")))
button2.append(Button(window, image = windowImage21, command=lambda: buttonFunc("(2,3)")))
button2.append(Button(window, image = windowImage22, command=lambda: buttonFunc("(2,4)")))

# Set up the inital buttons to display 1
button1[0].grid(row = 0, column = 0, rowspan = 3, columnspan = 3, ipadx = 2.5, ipady = 2.5)
button1[1].grid(row = 0, column = 3, rowspan = 3, columnspan = 3, ipadx = 2.5, ipady = 2.5)
button1[2].grid(row = 3, column = 0, rowspan = 3, columnspan = 3, ipadx = 2.5, ipady = 2.5)
button1[3].grid(row = 3, column = 3, rowspan = 3, columnspan = 3, ipadx = 2.5, ipady = 2.5)


# num is used to keep track of which number is on display
num = 1

''' Incorporate additional labels and zoom buttons '''
# Add buttons to change the image
buttonIn = Button(window, text = "ZOOM IN", command=lambda: zoom(True))
buttonOut = Button(window, text = "ZOOM OUT", command=lambda: zoom(False))
buttonIn.grid(row = 6, column = 7)
buttonOut.grid(row = 6, column = 8)

# Set the Title for the current map
def mapTitle(num:int):
    global label
    if num == 1:
        label = tk.Label(window, text ='Eugene', bg='white', fg = "dark green", font = "Helvetica 16 bold italic")
    else:
        label = tk.Label(window, text ='Lane County', bg='white', fg = "dark green", font = "Helvetica 16 bold italic")
    label.grid(row = 7, column = 4)

# Set default title
label = tk.Label(window, text ='Eugene', bg='white', fg = "dark green", font = "Helvetica 16 bold italic")
label.grid(row = 7, column = 4)

# Set initial zoom in button to disabled
buttonIn["state"] = DISABLED


mainloop()