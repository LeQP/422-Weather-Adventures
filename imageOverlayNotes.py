'''
By Joey Le
This is a file to learn how to insert an image on top of another image to display in a Tkinter Window
Additionally, this uses radio buttons so this file contains info on how to use them.
'''

''' Function to create image overlapping another image'''
def formImage():
    # Get the images like in the other Notes files
    cwd = os.getcwd()
    path1 = cwd + "/testImages/one.png"
    path2 = cwd + "/testImages/two.png"
    path3 = cwd + "/testImages/three.png"
    print(path1)
    openImage1 = Image.open(path1)
    openImage2 = Image.open(path2)
    openImage3 = Image.open(path3)
    # Create 2 different images for each test image (large and small)
    resizeImage1L = openImage1.resize((300, 300))
    resizeImage2L = openImage2.resize((300, 300))
    resizeImage3L = openImage3.resize((300, 300))
    resizeImage1S = openImage1.resize((100, 100))
    resizeImage2S = openImage2.resize((100, 100))
    resizeImage3S = openImage3.resize((100, 100))

    # Declare the image variables that will be used
    lImage = None
    sImage = None
    # Get the radio button options with get()
    lVal = large.get()
    sVal = small.get()
    xVal = xCord.get()
    yVal = yCord.get()

    # Set the large image
    if (lVal == 1):
        lImage = resizeImage1L
    elif (lVal == 2):
        lImage = resizeImage2L
    elif (lVal == 3):
        lImage = resizeImage3L 
    # Set the small image
    if (sVal == 1):
        sImage = resizeImage1S
    elif (sVal == 2):
        sImage = resizeImage2S
    elif (sVal == 3):
        sImage = resizeImage3S 
    
    # Use .paste() to add the small image to the large image (large image calls this method)
    #   1st Parameter = small image to add
    #   2nd Parameter = tuple of the coordinates to place small image (in respects to the large image starting at (0,0) in its top left corner)
    #   3rd Parameter (Optional) = image mask used if you want it to be transparent
    lImage.paste(sImage, (xVal,yVal), mask = sImage)

    # Make the image Tkinter compatabile
    windowImage = ImageTk.PhotoImage(lImage)

    # Need both lines to update the current image; 
    #   configure() sets the member to the new image
    #   .image creates a reference to the new image so that it does not immediatly disappear after the configure() line
    overlapImage.configure(image = windowImage)
    overlapImage.image = windowImage

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
window.geometry("600x600")


''' Set up the radio buttons '''
# Large Image to use as the background
# (All Radio buttons follow the commented structure, so only commented on this one)

# Ensure that the large is an int
large = IntVar()
lLabel = Label(text = "Please select the large image to use:   ")
# Use Radiobutton() to create the radio button
#   value assigns the value to the assigned variable
#   variable establishes which variable is associated with that radio button
l1 = Radiobutton(window, text='One', value=1, variable=large)
l2 = Radiobutton(window, text='Two', value=2, variable=large)
l3 = Radiobutton(window, text='Three', value=3, variable=large)
lLabel.grid(row = 0, column = 0)
l1.grid(row = 0, column = 1)
l2.grid(row = 0, column = 2)
l3.grid(row = 0, column = 3)
# .set() assigns a default value upon opening the program
large.set(1)

# Small image to use in the foreground
small = IntVar()
sLabel = Label(text = "Please select the small image to use:   ")
s1 = Radiobutton(window, text='One', value=1, variable=small)
s2 = Radiobutton(window, text='Two', value=2, variable=small)
s3 = Radiobutton(window, text='Three', value=3, variable=small)
sLabel.grid(row = 1, column = 0)
s1.grid(row = 1, column = 1)
s2.grid(row = 1, column = 2)
s3.grid(row = 1, column = 3)
small.set(1)

# X Coordinate to place the small image
xCord = IntVar()
xLabel = Label(text = "Select the x coordinate to place the small image:")
x0 = Radiobutton(window, text='0', value=0, variable=xCord)
x1 = Radiobutton(window, text='100', value=100, variable=xCord)
x2 = Radiobutton(window, text='200', value=200, variable=xCord)
xLabel.grid(row = 2, column = 0)
x0.grid(row = 2, column = 1)
x1.grid(row = 2, column = 2)
x2.grid(row = 2, column = 3)
xCord.set(0)

# Y Coordinate to place the small image
yCord = IntVar()
yLabel = Label(text = "Select the y coordinate to place the small image:")
y0 = Radiobutton(window, text='0', value=0, variable=yCord)
y1 = Radiobutton(window, text='100', value=100, variable=yCord)
y2 = Radiobutton(window, text='200', value=200, variable=yCord)
yLabel.grid(row = 3, column = 0)
y0.grid(row = 3, column = 1)
y1.grid(row = 3, column = 2)
y2.grid(row = 3, column = 3)
yCord.set(0)

''' Create the button and label for the overlap image creation '''
createButton = Button(window, text = "Create Overlap Image", command = formImage)
createButton.grid(row = 4, column = 0)
overlapImage = Label(window)
overlapImage.grid(row = 6, column = 0)

mainloop()


