# This file shows how to use Tkinter Grid features with implementing text, buttons, images and textboxes

#  Function for updating text in the window
def getValue():
   newDisplay1 = entry1.get()
   newDisplay2 = entry2.get()
   labelE1.grid(row = 3, column = 2, sticky = E)
   labelE2.grid(row = 4, column = 2, sticky = E)
   labelE1.configure(text=newDisplay1)
   labelE2.configure(text=newDisplay2)

# Function for updating check mark value
def checkOn():
   # Will cause other labels to reformat if text is quite long
   if checkVal.get() == "yes":
      labelC.configure(text="Is On")
   elif checkVal.get() == "no":
      labelC.configure(text="Is Off")
   else:
      labelC.configure(text="ERROR!")
   labelC.grid(row = 5, column = 3, sticky = E)
   
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

'''Use Tk() to create a Tkinter window'''
window = Tk()
 
''' Use geometry() to adjust window size '''
window.geometry("750x750")

# Use Label() to display text
# Other function parameters to alter the Label such as font or justify, need tkFont.Font()
# Interact with row, column, fontStyles, sticky to play around with them
# Tkinter decides how to position them accordingly (except may need to increase window size to accomdate cutoffs)
       # sticky refers to cardinal directions and acts like justifify
       # columnspan decides how many columns that the label can strethc, placing any adjacent ones should be +columnspan past it
       # There is ipadx, ipady, padx, pady that deal with padding
              # ipad = internal; deals with increasing the size of a widgets's area to space itself from other widgets
              # pad = external; deals with increasing the gap (empty space) between the target widget to other widgets
              # x/y = respective axis
      
fontStyle1 = tkFont.Font(family="Arial", size=8)
fontStyle2 = tkFont.Font(family="Arial", size=16)
fontStyle3 = tkFont.Font(family="Arial", size=32)
label1 = Label(window, text = "Test1", font=fontStyle1)
label2 = Label(window, text = "Test2", font=fontStyle3)
label3 = Label(window, text = "Test3", font=fontStyle2)
label4 = Label(window, text = "Test4", font=fontStyle1)
label5 = Label(window, text = "Test5", font=fontStyle2)
label1.grid(row = 0, column = 0, sticky = W, pady = 10)
label2.grid(row = 1, column = 0, sticky = W, columnspan=3, pady = 10)
label3.grid(row = 1, column = 3, sticky = E, pady = 10)
label4.grid(row = 2, column = 0, sticky = E)
label5.grid(row = 2, column = 2, sticky = E, pady = 10)

''' Use Entry() to add a textbox '''
display1 = ""
display2 = ""
entry1 = Entry(window)
entry2 = Entry(window)
entry1.grid(row = 4, column = 0, pady = 2)
entry2.grid(row = 3, column = 0, pady = 2)
entry1.grid(row = 3, column = 0)
entry2.grid(row = 4, column = 0)


labelE1 = Label(window, text = "", font=fontStyle1)
labelE2 = Label(window, text = "", font=fontStyle1)

''' Add buttons '''
# Add a click button
button= Button(window, text="Enter", command= getValue)
button.grid(row = 5, column = 0)

# Add a checkmark button
labelC = Label(window, text = "", font=fontStyle1)
checkVal = StringVar()
   # Can set a variable associated with check box (variable) and the values for when it is checked (onvalue) or not checked (offvalue)
   # Default values are 1 for onvalue and 0 for offvalue
checkButton = Checkbutton(window, text = "Checkmark", variable = checkVal, onvalue = "yes", offvalue = "no", command = checkOn)
checkButton.grid(row = 5, column = 1, sticky = W)

''' Add image (needs to be PNG) '''
# Get the currrent working directory and path to access image
cwd = os.getcwd()
path = cwd + "/testImages/one.png"
# Need pillow module to open the image
openImage = Image.open(path)
# Use resize() to alter image size (values based on the tkinter window dimensions. i.e same units of measurements)
resizeImage = openImage.resize((100, 100))
# Use PhotoImage to make it Tkinter comptabile
windowImage = ImageTk.PhotoImage(resizeImage)
# Place image on Tkinter window with a label
labelI = Label(window, image = windowImage)
labelI.grid(row = 6, column = 0, columnspan = 2, rowspan = 2, padx = 5, pady = 5)
mainloop()