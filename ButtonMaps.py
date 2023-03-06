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


''' Function to display the Tkinter window coordinate of the button'''
def buttonFunc(coordinates:str):
    inputStr = "Button Clicked at " + coordinates
    labelButton.configure(text=inputStr)

''' Function for the Zoom Buttons; It will change the dimensions of the grid and number displayed  '''
def zoom(closer:bool):
    global num 
    if (closer == False):
        # Change 1 into 2
        oneToTwo()
        num = 2
        buttonIn["state"] = NORMAL
        buttonOut["state"] = DISABLED
    else:
        # Change 2 into 1
        twoToOne()
        num = 1
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

'''
path23 = cwd + "/images/mapImages/Oregon7x6/1.png"
path24 = cwd + "/images/mapImages/Oregon7x6/2.png"
path25 = cwd + "/images/mapImages/Oregon7x6/3.png"
path26 = cwd + "/images/mapImages/Oregon7x6/4.png"
path27 = cwd + "/images/mapImages/Oregon7x6/5.png"
path28 = cwd + "/images/mapImages/Oregon7x6/6.png"
path29 = cwd + "/images/mapImages/Oregon7x6/7.png"
path30 = cwd + "/images/mapImages/Oregon7x6/8.png"
path31 = cwd + "/images/mapImages/Oregon7x6/9.png"
path32 = cwd + "/images/mapImages/Oregon7x6/10.png"
path33 = cwd + "/images/mapImages/Oregon7x6/11.png"
path34 = cwd + "/images/mapImages/Oregon7x6/12.png"
path35 = cwd + "/images/mapImages/Oregon7x6/13.png"
path36 = cwd + "/images/mapImages/Oregon7x6/14.png"
path37 = cwd + "/images/mapImages/Oregon7x6/15.png"
path38 = cwd + "/images/mapImages/Oregon7x6/16.png"
path39 = cwd + "/images/mapImages/Oregon7x6/17.png"
path40 = cwd + "/images/mapImages/Oregon7x6/18.png"
path41 = cwd + "/images/mapImages/Oregon7x6/19.png"
path42 = cwd + "/images/mapImages/Oregon7x6/20.png"
path43 = cwd + "/images/mapImages/Oregon7x6/21.png"
path44 = cwd + "/images/mapImages/Oregon7x6/22.png"
path45 = cwd + "/images/mapImages/Oregon7x6/23.png"
path46 = cwd + "/images/mapImages/Oregon7x6/24.png"
path47 = cwd + "/images/mapImages/Oregon7x6/25.png"
path48 = cwd + "/images/mapImages/Oregon7x6/26.png"
path49 = cwd + "/images/mapImages/Oregon7x6/27.png"
path50 = cwd + "/images/mapImages/Oregon7x6/28.png"
path51 = cwd + "/images/mapImages/Oregon7x6/29.png"
path52 = cwd + "/images/mapImages/Oregon7x6/30.png"
path53 = cwd + "/images/mapImages/Oregon7x6/31.png"
path54 = cwd + "/images/mapImages/Oregon7x6/32.png"
path55 = cwd + "/images/mapImages/Oregon7x6/33.png"
path56 = cwd + "/images/mapImages/Oregon7x6/34.png"
path57 = cwd + "/images/mapImages/Oregon7x6/35.png"
path58 = cwd + "/images/mapImages/Oregon7x6/36.png"
path59 = cwd + "/images/mapImages/Oregon7x6/37.png"
path60 = cwd + "/images/mapImages/Oregon7x6/38.png"
path61 = cwd + "/images/mapImages/Oregon7x6/39.png"
path62 = cwd + "/images/mapImages/Oregon7x6/40.png"
path63 = cwd + "/images/mapImages/Oregon7x6/41.png"
path64 = cwd + "/images/mapImages/Oregon7x6/42.png"
'''

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

'''
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
openImage61 = Image.open(path61)
openImage62 = Image.open(path62)
openImage63 = Image.open(path63)
openImage64 = Image.open(path64)
'''

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

'''
resizeImage23 = openImage23.resize((80, 80))
resizeImage24 = openImage24.resize((80, 80))
resizeImage25 = openImage25.resize((80, 80))
resizeImage26 = openImage26.resize((80, 80))
resizeImage27 = openImage27.resize((80, 80))
resizeImage28 = openImage28.resize((80, 80))
resizeImage29 = openImage29.resize((80, 80))
resizeImage30 = openImage30.resize((80, 80))
resizeImage31 = openImage31.resize((80, 80))
resizeImage32 = openImage32.resize((80, 80))
resizeImage33 = openImage33.resize((80, 80))
resizeImage34 = openImage34.resize((80, 80))
resizeImage35 = openImage35.resize((80, 80))
resizeImage36 = openImage36.resize((80, 80))
resizeImage37 = openImage37.resize((80, 80))
resizeImage38 = openImage38.resize((80, 80))
resizeImage39 = openImage39.resize((80, 80))
resizeImage40 = openImage40.resize((80, 80))
resizeImage41 = openImage41.resize((80, 80))
resizeImage42 = openImage42.resize((80, 80))
resizeImage43 = openImage43.resize((80, 80))
resizeImage44 = openImage44.resize((80, 80))
resizeImage45 = openImage45.resize((80, 80))
resizeImage46 = openImage46.resize((80, 80))
resizeImage47 = openImage47.resize((80, 80))
resizeImage48 = openImage48.resize((80, 80))
resizeImage49 = openImage49.resize((80, 80))
resizeImage50 = openImage50.resize((80, 80))
resizeImage51 = openImage51.resize((80, 80))
resizeImage52 = openImage52.resize((80, 80))
resizeImage53 = openImage53.resize((80, 80))
resizeImage54 = openImage54.resize((80, 80))
resizeImage55 = openImage55.resize((80, 80))
resizeImage56 = openImage56.resize((80, 80))
resizeImage57 = openImage57.resize((80, 80))
resizeImage58 = openImage58.resize((80, 80))
resizeImage59 = openImage59.resize((80, 80))
resizeImage60 = openImage60.resize((80, 80))
resizeImage61 = openImage61.resize((80, 80))
resizeImage62 = openImage62.resize((80, 80))
resizeImage63 = openImage63.resize((80, 80))
resizeImage64 = openImage64.resize((80, 80))
'''

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

'''
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
windowImage61 = ImageTk.PhotoImage(resizeImage61)
windowImage62 = ImageTk.PhotoImage(resizeImage62)
windowImage63 = ImageTk.PhotoImage(resizeImage63)
windowImage64 = ImageTk.PhotoImage(resizeImage64)
'''

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

# Put all the buttons for viewing Oregon into button2; 7x6
'''
button3 = []
button3.append(Button(window, image = windowImage23, command=lambda: buttonFunc("(0,0)")))
button3.append(Button(window, image = windowImage24, command=lambda: buttonFunc("(0,1)")))
button3.append(Button(window, image = windowImage25, command=lambda: buttonFunc("(0,2)")))
button3.append(Button(window, image = windowImage26, command=lambda: buttonFunc("(0,3)")))
button3.append(Button(window, image = windowImage27, command=lambda: buttonFunc("(0,4)")))
button3.append(Button(window, image = windowImage28, command=lambda: buttonFunc("(0,5)")))
button3.append(Button(window, image = windowImage29, command=lambda: buttonFunc("(1,0)")))
button3.append(Button(window, image = windowImage30, command=lambda: buttonFunc("(1,1)")))
button3.append(Button(window, image = windowImage31, command=lambda: buttonFunc("(1,2)")))
button3.append(Button(window, image = windowImage32, command=lambda: buttonFunc("(1,3)")))
button3.append(Button(window, image = windowImage33, command=lambda: buttonFunc("(1,4)")))
button3.append(Button(window, image = windowImage34, command=lambda: buttonFunc("(1,5)")))
button3.append(Button(window, image = windowImage35, command=lambda: buttonFunc("(2,0)")))
button3.append(Button(window, image = windowImage36, command=lambda: buttonFunc("(2,1)")))
button3.append(Button(window, image = windowImage37, command=lambda: buttonFunc("(2,2)")))
button3.append(Button(window, image = windowImage38, command=lambda: buttonFunc("(2,3)")))
button3.append(Button(window, image = windowImage39, command=lambda: buttonFunc("(2,4)")))
button3.append(Button(window, image = windowImage40, command=lambda: buttonFunc("(2,5)")))
button3.append(Button(window, image = windowImage41, command=lambda: buttonFunc("(3,0)")))
button3.append(Button(window, image = windowImage42, command=lambda: buttonFunc("(3,1)")))
button3.append(Button(window, image = windowImage43, command=lambda: buttonFunc("(3,2)")))
button3.append(Button(window, image = windowImage44, command=lambda: buttonFunc("(3,3)")))
button3.append(Button(window, image = windowImage45, command=lambda: buttonFunc("(3,4)")))
button3.append(Button(window, image = windowImage46, command=lambda: buttonFunc("(3,5)")))
button3.append(Button(window, image = windowImage47, command=lambda: buttonFunc("(4,0)")))
button3.append(Button(window, image = windowImage48, command=lambda: buttonFunc("(4,1)")))
button3.append(Button(window, image = windowImage49, command=lambda: buttonFunc("(4,2)")))
button3.append(Button(window, image = windowImage50, command=lambda: buttonFunc("(4,3)")))
button3.append(Button(window, image = windowImage51, command=lambda: buttonFunc("(4,4)")))
button3.append(Button(window, image = windowImage52, command=lambda: buttonFunc("(4,5)")))
button3.append(Button(window, image = windowImage53, command=lambda: buttonFunc("(5,0)")))
button3.append(Button(window, image = windowImage54, command=lambda: buttonFunc("(5,1)")))
button3.append(Button(window, image = windowImage55, command=lambda: buttonFunc("(5,2)")))
button3.append(Button(window, image = windowImage56, command=lambda: buttonFunc("(5,3)")))
button3.append(Button(window, image = windowImage57, command=lambda: buttonFunc("(5,4)")))
button3.append(Button(window, image = windowImage58, command=lambda: buttonFunc("(5,5)")))
button3.append(Button(window, image = windowImage59, command=lambda: buttonFunc("(6,0)")))
button3.append(Button(window, image = windowImage60, command=lambda: buttonFunc("(6,1)")))
button3.append(Button(window, image = windowImage61, command=lambda: buttonFunc("(6,2)")))
button3.append(Button(window, image = windowImage62, command=lambda: buttonFunc("(6,3)")))
button3.append(Button(window, image = windowImage63, command=lambda: buttonFunc("(6,4)")))
button3.append(Button(window, image = windowImage64, command=lambda: buttonFunc("(6,5)")))
'''

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

# Set initial zoom in button to disabled
buttonIn["state"] = DISABLED


mainloop()