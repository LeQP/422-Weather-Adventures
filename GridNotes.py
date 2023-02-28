# This file shows how to use Tkinter Grid features with implemtning text, buttons, images and textboxes

#  Function for updating text in the window
def getValue():
   newDisplay1 = entry1.get()
   newDisplay2 = entry2.get()
   
   labelE1.grid(row = 3, column = 2, sticky = E)
   labelE2.grid(row = 4, column = 2, sticky = E)
   labelE1.configure(text=newDisplay1)
   labelE2.configure(text=newDisplay2)

# import tkinter module
from tkinter import * 
from tkinter.ttk import *
import os
import tkinter.font as tkFont
# creating main tkinter window
window = Tk()
 
# Use geometry() to adjust window size 
window.geometry("750x750")

# Use Label() to display text
# Other function parameters to alter the Label such as font or justify, need tkFont.Font()
# Interact with row, column, fontStyles, sticky to play around with them
# Tkinter decides how to position them accordingly (except may need to increase window size to accomdate cutoffs)
       # sticky refers to cardinal directions and acts like justification
       # columnspan decides how many columns that the label can strethc, placing any adjacent ones should be +columnspan past it
       # There is ipadx, ipady, padx, pady that deal with padding (not sure "padding means")
              # i = internal
              # p = external
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


# Use Entry() to add a textbox
display1 = "Hello"
display2 = "World"
entry1 = Entry(window)
entry2 = Entry(window)
entry1.grid(row = 4, column = 0, pady = 2)
entry2.grid(row = 3, column = 0, pady = 2)
entry1.grid(row = 3, column = 0)
entry2.grid(row = 4, column = 0)


labelE1 = Label(window, text = "", font=fontStyle1)
labelE2 = Label(window, text = "", font=fontStyle1)

# Add buttons
button= Button(window, text="Enter", command= getValue)
button.grid(row = 5, column = 0)
# checkbutton widget
#c1 = Checkbutton(master, text = "Preserve")
#c1.grid(row = 2, column = 0, sticky = W, columnspan = 2)
 

#cwd = os.getcwd()
#path = cwd + "/testImages/one.png"
#print("Path =")
#print(path)
# adding image (remember image should be PNG and not JPG)
#img = PhotoImage(file = path)
#img1 = img.subsample(2, 2)
 
# setting image with the help of label
#Label(master, image = img1).grid(row = 0, column = 2, columnspan = 2, rowspan = 1, padx = 5, pady = 5)
 
# button widget
#b1 = Button(master, text = "Zoom in")
#b2 = Button(master, text = "Zoom out")
 
# arranging button widgets
#b1.grid(row = 2, column = 2, sticky = E)
#b2.grid(row = 2, column = 3, sticky = E)
 
# infinite loop which can be terminated
# by keyboard or mouse interrupt
mainloop()