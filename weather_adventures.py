'''
weather_adventures.py
--------
Author: Melodie Collins
Created: 3/3/2023
Last Modified: 3/12/2023
Purpose: This is the user interface file that will be run by the main weather_adventures_main.py file.

Revision History (Date | Author | Modifications)
----------------------------------------------
3/6/2023  | Melodie Collins | Made the initial file and split map images
3/7/2023  | Melodie Collins | Resized map images for tkinter use
3/9/2023  | Melodie Collins | Worked on combining with weather_adventures_main.py
3/10/2023 | Melodie Collins | Finished interaction weather_adventures_main.py
3/12/2023 | Melodie Collins | Signed off on final version
'''

# import weather_adventures_main
import weather_adventures_main

# import tkinter modules
from tkinter import * 
import tkinter as tk
from tkinter.ttk import *
import tkinter.font as tkFont # For setting text fonts

# import os to access current working directory
import os

# import PIL modules to manipulate images
from PIL import Image   # Open images
from PIL import ImageTk # Have images available for Tkinter

'''
on_click(): this function is used to remove the current map title

Parameters: none

Return: none
'''
def on_click():
    # remove the map title
    label.after(0, label.destroy())

'''
button_click(): this function is for for when a button is clicked; 
                It will change the selected button's image appropriately

Parameters: none

Return: none
'''
def button_click():
    # if wind is selected:
    if wind.get() == 1:
        # if current map is Eugene
        if num == 1:
            # display Eugene wind images
            setEugeneWind()
        # else current map is Lane County
        else:
            # display Lane wind images
            setLaneWind()
    # if weather is selected:
    elif weather.get() == 1:
        # if current map is Eugene
        if num == 1:
            # display Eugene wind images
            setEugeneWeather()
        # else current map is Lane County
        else:
            # display Lane wind images
            setLaneWeather()
    # if empty is selected
    elif empty.get() == 1:
        # if current map is Eugene
        if num == 1:
            # display Eugene wind images
            setEugeneEmpty()
        # else current map is Lane County
        else:
            # display Lane wind images
            setLaneEmpty()
    else:
        # if current map is Eugene
        if num == 1:
            # display Eugene wind images
            setEugeneEmpty()
        # else current map is Lane County
        else:
            # display Lane wind images
            setLaneEmpty()

'''
zoom(): this function is for the Zoom Buttons; It will change the dimensions of 
            the grid and number displayed

Parameters:
    closer: a bool that determines if the map can zoom in closer
    buttonIn: the zoom in button
    buttonOut: the zoom out button

Return: none
'''
def zoom(closer:bool, buttonIn, buttonOut):
    # set global num
    global num 
    if (closer == False):
        # reset button images
        setLaneEmpty()
        # change Eugene map to Lane County map
        oneToTwo()
        # reset empty checkbox to unselected
        empty.set(0)
        # reset wind checkbox to unselected
        wind.set(0)
        # reset weather checkbox to unselected
        weather.set(0)
        # set map level
        num = 2
        # remove current map title
        on_click()
        # set the map title to Lane County
        mapTitle(num)
        # set zoom in button to disabled
        buttonIn["state"] = NORMAL
        # set zoom in button to enabled
        buttonOut["state"] = DISABLED
    else:
        # reset button images
        setEugeneEmpty()
        # change Lane map to Eugene map
        twoToOne()
        # reset empty checkbox to unselected
        empty.set(0)
        # reset wind checkbox to unselected
        wind.set(0)
        # reset weather checkbox to unselected
        weather.set(0)
        # set map level
        num = 1
        # remove current map title
        on_click()
        # set the map title to Eugene
        mapTitle(num)
        # set zoom in button to disabled
        buttonIn["state"] = DISABLED
        # set zoom in button to enabled
        buttonOut["state"] = NORMAL

'''
oneToTwo(): this function removes the current buttons for X from the window, but does 
            not destroy them; Next, it adds each button for Y into the tkinter window.

Parameters: none

Return: none
'''
def oneToTwo():
    # loop through the Eugene buttons button1 and remove the buttons from the window
    for i in range(len(button1)):
        button1[i].grid_forget()
    # loop through the rows
    for i in range(3):
        # loop through the columns
        for j in range(5):
            # add each button Y into the tkinter window
            button2[i * 5 + j].grid(row = i*2, column = j*2, rowspan = 2, columnspan = 2)
    
'''
twoToOne(): this function removes the current buttons for X from the window, but does not destroy them.
            Next, it adds each button for Y into the tkinter window.

Parameters: none

Return: none
'''
def twoToOne(): 
    # loop through the Lane County buttons button2 and remove the buttons from the window
    for i in range(len(button2)):
        button2[i].grid_forget()
    # loop through the rows
    for i in range(2):
        # loop through the columns
        for j in range(2):
            # add each button Y into the tkinter window
            button1[i * 2 + j].grid(row = i*3, column = j*5, rowspan = 3, columnspan = 5, ipadx = 2.5, ipady = 2.5)

'''
mapTitle(): this function sets the title for the current map

Parameters:
    num: an integer that provides the current map level

Return: none
'''
def mapTitle(num:int):
    # set global label
    global label
    # if current map is Eugene
    if num == 1:
        # set title to Eugene
        label = tk.Label(window, text ='Eugene', bg='white', fg = "dark green", font = "Helvetica 16 bold italic")
    # else current map is Lane County
    else:
        # set title to Lane County
        label = tk.Label(window, text ='Lane County', bg='white', fg = "dark green", font = "Helvetica 16 bold italic")
    # set title location
    label.grid(row = 7, column = 4)

'''
setEugene(): this function puts all the buttons for viewing Eugene into button1; 2x2

Parameters: none

Return: none
'''
def setEugene():
    # set global button1 for Lane County buttons
    global button1
    button1 = []
    # add buttons with images and call weather_adventures_main.more_info() when clicked
    button1.append(tk.Button(window, image = windowImage4, highlightthickness = 0, borderwidth=0, command=lambda: weather_adventures_main.more_info(1, 1)))
    button1.append(tk.Button(window, image = windowImage5, highlightthickness = 0, borderwidth=0, command=lambda: weather_adventures_main.more_info(1, 2)))
    button1.append(tk.Button(window, image = windowImage6, highlightthickness = 0, borderwidth=0, command=lambda: weather_adventures_main.more_info(1, 3)))
    button1.append(tk.Button(window, image = windowImage7, highlightthickness = 0, borderwidth=0, command=lambda: weather_adventures_main.more_info(1, 4)))

'''
setEugeneEmpty(): this function sets all Eugene button images to Eugene images

Parameters: none

Return: none
'''
def setEugeneEmpty():
    button1[0].config(image=windowImage4)
    button1[1].config(image=windowImage5)
    button1[2].config(image=windowImage6)
    button1[3].config(image=windowImage7)

'''
setEugeneWeather(): this function sets all Eugene button images to Eugene weather images

Parameters: none

Return: none
'''
def setEugeneWeather():
    button1[0].config(image=windowImage23)
    button1[1].config(image=windowImage25)
    button1[2].config(image=windowImage27)
    button1[3].config(image=windowImage29)

'''
setEugeneWind(): this function sets all Eugene button images to Eugene wind images

Parameters: none

Return: none
'''
def setEugeneWind():
    button1[0].config(image=windowImage24)
    button1[1].config(image=windowImage26)
    button1[2].config(image=windowImage28)
    button1[3].config(image=windowImage30)

'''
setLane(): this function puts all the buttons for viewing Lane County into button2; 5x3

Parameters: none

Return: none
'''
def setLane():
    # set gloabl button2 for Lane County buttons
    global button2
    button2 = []

    # add buttons with images and call weather_adventures_main.more_info() when clicked
    button2.append(tk.Button(window, image = windowImage8, highlightthickness = 0, command=lambda: weather_adventures_main.more_info(2, 1)))
    button2.append(tk.Button(window, image = windowImage9, highlightthickness = 0, command=lambda: weather_adventures_main.more_info(2, 2)))
    button2.append(tk.Button(window, image = windowImage10, highlightthickness = 0, command=lambda: weather_adventures_main.more_info(2, 3)))
    button2.append(tk.Button(window, image = windowImage11, highlightthickness = 0, command=lambda: weather_adventures_main.more_info(2, 4)))
    button2.append(tk.Button(window, image = windowImage12, highlightthickness = 0, command=lambda: weather_adventures_main.more_info(2, 5)))
    button2.append(tk.Button(window, image = windowImage13, highlightthickness = 0, command=lambda: weather_adventures_main.more_info(2, 6)))
    button2.append(tk.Button(window, image = windowImage14, highlightthickness = 0, command=lambda: weather_adventures_main.more_info(2, 7)))
    button2.append(tk.Button(window, image = windowImage15, highlightthickness = 0, command=lambda: weather_adventures_main.more_info(2, 8)))
    button2.append(tk.Button(window, image = windowImage16, highlightthickness = 0, command=lambda: weather_adventures_main.more_info(2, 9)))
    button2.append(tk.Button(window, image = windowImage17, highlightthickness = 0, command=lambda: weather_adventures_main.more_info(2, 10)))
    button2.append(tk.Button(window, image = windowImage18, highlightthickness = 0, command=lambda: weather_adventures_main.more_info(2, 11)))
    button2.append(tk.Button(window, image = windowImage19, highlightthickness = 0, command=lambda: weather_adventures_main.more_info(2, 12)))
    button2.append(tk.Button(window, image = windowImage20, highlightthickness = 0, command=lambda: weather_adventures_main.more_info(2, 13)))
    button2.append(tk.Button(window, image = windowImage21, highlightthickness = 0, command=lambda: weather_adventures_main.more_info(2, 14)))
    button2.append(tk.Button(window, image = windowImage22, highlightthickness = 0, command=lambda: weather_adventures_main.more_info(2, 15)))

'''
setLaneEmpty(): this function sets all Lane County button images to Lane County images

Parameters: none

Return: none
'''
def setLaneEmpty():
    button2[0].config(image=windowImage8)
    button2[1].config(image=windowImage9)
    button2[2].config(image=windowImage10)
    button2[3].config(image=windowImage11)
    button2[4].config(image=windowImage12)
    button2[5].config(image=windowImage13)
    button2[6].config(image=windowImage14)
    button2[7].config(image=windowImage15)
    button2[8].config(image=windowImage16)
    button2[9].config(image=windowImage17)
    button2[10].config(image=windowImage18)
    button2[11].config(image=windowImage19)
    button2[12].config(image=windowImage20)
    button2[13].config(image=windowImage21)
    button2[14].config(image=windowImage22)

'''
setLaneWeather(): this function sets all Lane County button images to Lane County weather images

Parameters: none

Return: none
'''
def setLaneWeather():
    button2[0].config(image=windowImage31)
    button2[1].config(image=windowImage33)
    button2[2].config(image=windowImage35)
    button2[3].config(image=windowImage37)
    button2[4].config(image=windowImage39)
    button2[5].config(image=windowImage41)
    button2[6].config(image=windowImage43)
    button2[7].config(image=windowImage45)
    button2[8].config(image=windowImage47)
    button2[9].config(image=windowImage49)
    button2[10].config(image=windowImage51)
    button2[11].config(image=windowImage53)
    button2[12].config(image=windowImage55)
    button2[13].config(image=windowImage57)
    button2[14].config(image=windowImage59)

'''
setLaneWind(): this function sets all Lane County button images to Lane County wind images

Parameters: none

Return: none
'''
def setLaneWind():
    button2[0].config(image=windowImage32)
    button2[1].config(image=windowImage34)
    button2[2].config(image=windowImage36)
    button2[3].config(image=windowImage38)
    button2[4].config(image=windowImage40)
    button2[5].config(image=windowImage42)
    button2[6].config(image=windowImage44)
    button2[7].config(image=windowImage46)
    button2[8].config(image=windowImage48)
    button2[9].config(image=windowImage50)
    button2[10].config(image=windowImage52)
    button2[11].config(image=windowImage54)
    button2[12].config(image=windowImage56)
    button2[13].config(image=windowImage58)
    button2[14].config(image=windowImage60)

'''
clearWindWeather(): this function sets the wind and weather checkboxes to unselected

Parameters: none

Return: none
'''
def clearWindWeather():
    wind.set(0) # set wind checkbox to unselected
    weather.set(0) # set weather checkbox to unselected

'''
clearEmptyWeatehr(): this function sets the empty and weather checkboxes to unselected

Parameters: none

Return: none
'''
def clearEmptyWeather():
    empty.set(0) # set empty checkbox to unselected
    weather.set(0) # set weather checkbox to unselected


'''
clearEmptyWind(): this function sets the empty and wind checkboxes to unselected

Parameters: none

Return: none
'''
def clearEmptyWind():
    empty.set(0) # set empty checkbox to unselected
    wind.set(0) # set wind checkbox to unselected

'''
main(): This function sets up the Tkinter Window and runs the program

Paramters: none

Return: none
'''
def main():
    global window
    window = Tk()
    window.geometry("1000x1000")

    # Set the Title of Tkinter window
    window.title("Weather Adventures")

    ''' Add image '''
    cwd = os.getcwd() # current working directory

    # get the location for the original images
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

    # New weather and wind images
    path23 = cwd + "/images/mapImages_symbols/Eugene2x2/1.png"
    path24 = cwd + "/images/mapImages_symbols/Eugene2x2/1_w.png"
    path25 = cwd + "/images/mapImages_symbols/Eugene2x2/2.png"
    path26 = cwd + "/images/mapImages_symbols/Eugene2x2/2_w.png"
    path27 = cwd + "/images/mapImages_symbols/Eugene2x2/3.png"
    path28 = cwd + "/images/mapImages_symbols/Eugene2x2/3_w.png"
    path29 = cwd + "/images/mapImages_symbols/Eugene2x2/4.png"
    path30 = cwd + "/images/mapImages_symbols/Eugene2x2/4_w.png"
    path31 = cwd + "/images/mapImages_symbols/LaneCounty5x3/1.png"
    path32 = cwd + "/images/mapImages_symbols/LaneCounty5x3/1_w.png"
    path33 = cwd + "/images/mapImages_symbols/LaneCounty5x3/2.png"
    path34 = cwd + "/images/mapImages_symbols/LaneCounty5x3/2_w.png"
    path35 = cwd + "/images/mapImages_symbols/LaneCounty5x3/3.png"
    path36 = cwd + "/images/mapImages_symbols/LaneCounty5x3/3_w.png"
    path37 = cwd + "/images/mapImages_symbols/LaneCounty5x3/4.png"
    path38 = cwd + "/images/mapImages_symbols/LaneCounty5x3/4_w.png"
    path39 = cwd + "/images/mapImages_symbols/LaneCounty5x3/5.png"
    path40 = cwd + "/images/mapImages_symbols/LaneCounty5x3/5_w.png"
    path41 = cwd + "/images/mapImages_symbols/LaneCounty5x3/6.png"
    path42 = cwd + "/images/mapImages_symbols/LaneCounty5x3/6_w.png"
    path43 = cwd + "/images/mapImages_symbols/LaneCounty5x3/7.png"
    path44 = cwd + "/images/mapImages_symbols/LaneCounty5x3/7_w.png"
    path45 = cwd + "/images/mapImages_symbols/LaneCounty5x3/8.png"
    path46 = cwd + "/images/mapImages_symbols/LaneCounty5x3/8_w.png"
    path47 = cwd + "/images/mapImages_symbols/LaneCounty5x3/9.png"
    path48 = cwd + "/images/mapImages_symbols/LaneCounty5x3/9_w.png"
    path49 = cwd + "/images/mapImages_symbols/LaneCounty5x3/10.png"
    path50 = cwd + "/images/mapImages_symbols/LaneCounty5x3/10_w.png"
    path51 = cwd + "/images/mapImages_symbols/LaneCounty5x3/11.png"
    path52 = cwd + "/images/mapImages_symbols/LaneCounty5x3/11_w.png"
    path53 = cwd + "/images/mapImages_symbols/LaneCounty5x3/12.png"
    path54 = cwd + "/images/mapImages_symbols/LaneCounty5x3/12_w.png"
    path55 = cwd + "/images/mapImages_symbols/LaneCounty5x3/13.png"
    path56 = cwd + "/images/mapImages_symbols/LaneCounty5x3/13_w.png"
    path57 = cwd + "/images/mapImages_symbols/LaneCounty5x3/14.png"
    path58 = cwd + "/images/mapImages_symbols/LaneCounty5x3/14_w.png"
    path59 = cwd + "/images/mapImages_symbols/LaneCounty5x3/15.png"
    path60 = cwd + "/images/mapImages_symbols/LaneCounty5x3/15_w.png"

    # open the images
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
    openImage23 = Image.open(path23)
    openImage24 = Image.open(path24)
    openImage25 = Image.open(path25)
    openImage26 = Image.open(path26)
    openImage27 = Image.open(path27)
    openImage28 = Image.open(path28)
    openImage29 = Image.open(path29)
    openImage30 = Image.open(path30)
    openImage31 = Image.open(path31)
    openImage32 = Image.open(path32)
    openImage33 = Image.open(path33)
    openImage34 = Image.open(path34)
    openImage35 = Image.open(path35)
    openImage36 = Image.open(path36)
    openImage37 = Image.open(path37)
    openImage38 = Image.open(path38)
    openImage39 = Image.open(path39)
    openImage40 = Image.open(path40)
    openImage41 = Image.open(path41)
    openImage42 = Image.open(path42)
    openImage43 = Image.open(path43)
    openImage44 = Image.open(path44)
    openImage45 = Image.open(path45)
    openImage46 = Image.open(path46)
    openImage47 = Image.open(path47)
    openImage48 = Image.open(path48)
    openImage49 = Image.open(path49)
    openImage50 = Image.open(path50)
    openImage51 = Image.open(path51)
    openImage52 = Image.open(path52)
    openImage53 = Image.open(path53)
    openImage54 = Image.open(path54)
    openImage55 = Image.open(path55)
    openImage56 = Image.open(path56)
    openImage57 = Image.open(path57)
    openImage58 = Image.open(path58)
    openImage59 = Image.open(path59)
    openImage60 = Image.open(path60)

    # resize the images for 2x2
    resizeImage4 = openImage4.resize((350, 350))
    resizeImage5 = openImage5.resize((350, 350))
    resizeImage6 = openImage6.resize((350, 350))
    resizeImage7 = openImage7.resize((350, 350))

    # resize the images for 5x3
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

    # resize the images for 2x2
    resizeImage23 = openImage23.resize((350, 350))
    resizeImage24 = openImage24.resize((350, 350))
    resizeImage25 = openImage25.resize((350, 350))
    resizeImage26 = openImage26.resize((350, 350))
    resizeImage27 = openImage27.resize((350, 350))
    resizeImage28 = openImage28.resize((350, 350))
    resizeImage29 = openImage29.resize((350, 350))
    resizeImage30 = openImage30.resize((350, 350))

    # resize the images for 5x3
    resizeImage31 = openImage31.resize((160, 160))
    resizeImage32 = openImage32.resize((160, 160))
    resizeImage33 = openImage33.resize((160, 160))
    resizeImage34 = openImage34.resize((160, 160))
    resizeImage35 = openImage35.resize((160, 160))
    resizeImage36 = openImage36.resize((160, 160))
    resizeImage37 = openImage37.resize((160, 160))
    resizeImage38 = openImage38.resize((160, 160))
    resizeImage39 = openImage39.resize((160, 160))
    resizeImage40 = openImage40.resize((160, 160))
    resizeImage41 = openImage41.resize((160, 160))
    resizeImage42 = openImage42.resize((160, 160))
    resizeImage43 = openImage43.resize((160, 160))
    resizeImage44 = openImage44.resize((160, 160))
    resizeImage45 = openImage45.resize((160, 160))
    resizeImage46 = openImage46.resize((160, 160))
    resizeImage47 = openImage47.resize((160, 160))
    resizeImage48 = openImage48.resize((160, 160))
    resizeImage49 = openImage49.resize((160, 160))
    resizeImage50 = openImage50.resize((160, 160))
    resizeImage51 = openImage51.resize((160, 160))
    resizeImage52 = openImage52.resize((160, 160))
    resizeImage53 = openImage53.resize((160, 160))
    resizeImage54 = openImage54.resize((160, 160))
    resizeImage55 = openImage55.resize((160, 160))
    resizeImage56 = openImage56.resize((160, 160))
    resizeImage57 = openImage57.resize((160, 160))
    resizeImage58 = openImage58.resize((160, 160))
    resizeImage59 = openImage59.resize((160, 160))
    resizeImage60 = openImage60.resize((160, 160))

    # set global variables for opened and resized images
    global windowImage4
    global windowImage5
    global windowImage6
    global windowImage7
    global windowImage8
    global windowImage9
    global windowImage10
    global windowImage11
    global windowImage12
    global windowImage13
    global windowImage14
    global windowImage15
    global windowImage16
    global windowImage17
    global windowImage18
    global windowImage19
    global windowImage20
    global windowImage21
    global windowImage22
    global windowImage23
    global windowImage24
    global windowImage25
    global windowImage26
    global windowImage27
    global windowImage28
    global windowImage29
    global windowImage30
    global windowImage31
    global windowImage32
    global windowImage33
    global windowImage34
    global windowImage35
    global windowImage36
    global windowImage37
    global windowImage38
    global windowImage39
    global windowImage40
    global windowImage41
    global windowImage42
    global windowImage43
    global windowImage44
    global windowImage45
    global windowImage46
    global windowImage47
    global windowImage48
    global windowImage49
    global windowImage50
    global windowImage51
    global windowImage52
    global windowImage53
    global windowImage54
    global windowImage55
    global windowImage56
    global windowImage57
    global windowImage58
    global windowImage59
    global windowImage60

    # open and resize the map image
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
    windowImage23 = ImageTk.PhotoImage(resizeImage23)
    windowImage24 = ImageTk.PhotoImage(resizeImage24)
    windowImage25 = ImageTk.PhotoImage(resizeImage25)
    windowImage26 = ImageTk.PhotoImage(resizeImage26)
    windowImage27 = ImageTk.PhotoImage(resizeImage27)
    windowImage28 = ImageTk.PhotoImage(resizeImage28)
    windowImage29 = ImageTk.PhotoImage(resizeImage29)
    windowImage30 = ImageTk.PhotoImage(resizeImage30)
    windowImage31 = ImageTk.PhotoImage(resizeImage31)
    windowImage32 = ImageTk.PhotoImage(resizeImage32)
    windowImage33 = ImageTk.PhotoImage(resizeImage33)
    windowImage34 = ImageTk.PhotoImage(resizeImage34)
    windowImage35 = ImageTk.PhotoImage(resizeImage35)
    windowImage36 = ImageTk.PhotoImage(resizeImage36)
    windowImage37 = ImageTk.PhotoImage(resizeImage37)
    windowImage38 = ImageTk.PhotoImage(resizeImage38)
    windowImage39 = ImageTk.PhotoImage(resizeImage39)
    windowImage40 = ImageTk.PhotoImage(resizeImage40)
    windowImage41 = ImageTk.PhotoImage(resizeImage41)
    windowImage42 = ImageTk.PhotoImage(resizeImage42)
    windowImage43 = ImageTk.PhotoImage(resizeImage43)
    windowImage44 = ImageTk.PhotoImage(resizeImage44)
    windowImage45 = ImageTk.PhotoImage(resizeImage45)
    windowImage46 = ImageTk.PhotoImage(resizeImage46)
    windowImage47 = ImageTk.PhotoImage(resizeImage47)
    windowImage48 = ImageTk.PhotoImage(resizeImage48)
    windowImage49 = ImageTk.PhotoImage(resizeImage49)
    windowImage50 = ImageTk.PhotoImage(resizeImage50)
    windowImage51 = ImageTk.PhotoImage(resizeImage51)
    windowImage52 = ImageTk.PhotoImage(resizeImage52)
    windowImage53 = ImageTk.PhotoImage(resizeImage53)
    windowImage54 = ImageTk.PhotoImage(resizeImage54)
    windowImage55 = ImageTk.PhotoImage(resizeImage55)
    windowImage56 = ImageTk.PhotoImage(resizeImage56)
    windowImage57 = ImageTk.PhotoImage(resizeImage57)
    windowImage58 = ImageTk.PhotoImage(resizeImage58)
    windowImage59 = ImageTk.PhotoImage(resizeImage59)
    windowImage60 = ImageTk.PhotoImage(resizeImage60)

    setEugene() # set up each Eugene button within their grid set

    setLane() # set up each Lane County button within their grid set

    # set up the inital buttons to display corresponding Eugene images
    button1[0].grid(row = 0, column = 0, rowspan = 3, columnspan = 3, ipadx = 2.5, ipady = 2.5)
    button1[1].grid(row = 0, column = 3, rowspan = 3, columnspan = 3, ipadx = 2.5, ipady = 2.5)
    button1[2].grid(row = 3, column = 0, rowspan = 3, columnspan = 3, ipadx = 2.5, ipady = 2.5)
    button1[3].grid(row = 3, column = 3, rowspan = 3, columnspan = 3, ipadx = 2.5, ipady = 2.5)

    # set global num to keep track of which map is on display 
    global num
    num = 1 # the initial map level is 1

    ''' Incorporate additional labels and zoom buttons '''
    # add buttons to change the image
    buttonIn = tk.Button(window, text = "ZOOM IN", fg = "dark green", command=lambda: zoom(True, buttonIn, buttonOut))
    buttonOut = tk.Button(window, text = "ZOOM OUT", fg = "dark green", command=lambda: zoom(False, buttonIn, buttonOut))
    buttonIn.grid(row=7, column=10)
    buttonOut.grid(row=7, column=11)

    # set global empty to track empty checkbox
    global empty
    empty = IntVar()
    # set checkbox label and what function to call when it is clicked
    emptyBox = tk.Checkbutton(window, text='Clear', variable=empty, onvalue=1, offvalue=0, command=lambda:[clearWindWeather(), button_click()])
    # set location of empty checkbox
    emptyBox.grid(row = 9, column = 9)

    # set global empty to track wind checkbox
    global wind
    wind = IntVar()
    # set checkbox label and what function to call when it is clicked
    windBox = tk.Checkbutton(window, text='Wind', variable=wind, onvalue=1, offvalue=0, command=lambda:[clearEmptyWeather(), button_click()])
    # set location of wind checkbox
    windBox.grid(row = 9, column = 10)

    # set global empty to track weather checkbox
    global weather
    weather = IntVar()
    # set checkbox label and what function to call when it is clicked
    weatherBox = tk.Checkbutton(window, text='Weather', variable=weather, onvalue=1, offvalue=0, command=lambda:[clearEmptyWind(), button_click()])
    # set location of weather checkbox
    weatherBox.grid(row = 9, column = 11)

    mapTitle(num) # set the map title

    buttonIn["state"] = DISABLED # set initial zoom in button to disabled
    
    mainloop() # run tkinter

if __name__ == "__main__":
    weather_adventures_main.image_initializer()
    main()