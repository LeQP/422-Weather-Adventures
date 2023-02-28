'''
Author: Alexa Roskowski
Created: 1/21/23

1/21 --> intial protype
1/23 --> moved away from google Maps API
1/28 --> image and zoom function created

'''

import matplotlib.pyplot as plt #used for  showing images using matplots if you want
import matplotlib.image as mpimg


import cv2 #used for showing images using opencv-python

#####
# if we would rather use matplots to diplay images i can do that
# it is currently commented out 

def zoom(level):
    '''
    the function zoom will return one of three images depending on the level of zoom

    level relates to the amount of zoom : 1 is the least and 3 the most  

    1 will be the least amount of zoom, and will return an image of all of oregon
    2 will return lane country (the default level of zoom)
    3 will return the a .jpg of just Eugene
    '''
    #check that the level of zoom is within the expected parameters
    if level > 3 or level < 1:
        #we are out of the bounds allowed for the level of zoom
        #throw an error and return nothing
        print("Bad input")
        return
    if level == 1:
        #use oregon image

        #img = mpimg.imread('map_oregon.jpg')

        img = cv2.imread('images/mapImages/map_oregon.jpg')
    elif level == 2:
        #use lane county image

        #img = mpimg.imread('map_lane_county.jpg')

        img = cv2.imread('images/mapImages/map_lane_county.jpg')
    elif level == 3:
        #use eugene image

        #img = mpimg.imread('map_eugene.jpg')

        img = cv2.imread('images/mapImages/map_eugene.jpg')

    #img is the image depending on the desired zoom
    #now we display the image

    #imgplot = plt.imshow(img)
    #plt.show()

    cv2.imshow('map', img)
    cv2.waitKey()
    cv2.destroyAllWindows()


zoom(1)
zoom(2)
zoom(3)










