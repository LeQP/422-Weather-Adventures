'''
Author: Alexa Roskowski

This is the file that will be run by the user, and acts as the intermediary between all the files LIES

03/06 --> made the file and protype of image_initializer
03/07 --> added more_info and updated the image_initializer
03/09 --> worked on combining with Activcity Recommender and InfoPopup
03/10 --> finished interaction between InfoPopup and Activity Recommender
'''

#import all the other files
import ButtonMaps
import weather
import InfoPopup
import Activity_Reccomender

#import the other libraries we need
import os
from PIL import Image



#####  GLOBALS   #####
WEATHER_INFO = {}  #store the weather infomation per button, so we make as few as possible API calls)

# store the coordinates in a list to make it easier to reference
EUGENE_COORD_NAMES = [(44.081303, -123.146928), (44.083770, -123.046695),
                        (44.019559, -123.143883), (44.015600, -123.047490)]
            
            # each coord is a tuple st (lat, long)

LANE_COORD_NAMES = [(44.169810, -123.959655) ,(44.140252, -123.489990), (44.199846, -122.998352),
                    (44.178182, -122.492981), (44.191969, -122.006836), (44.140252, -123.489990),
                    (43.830482, -123.487243), (43.856234, -123.006592), (43.850292, -122.471008), 
                    (43.842369, -121.987610), (43.540004, -123.995361), (43.541001, -123.486545), 
                    (43.528811, -122.955678), (43.549707, -122.463245), (43.523586, -122.040473)]





'''
Author: Joey Le
imageAppender(): this function allows a large image to have a smaller image placed on of it

Parameters:
    pathLarge: a string that provides the path to access the image file for the large image
    pathSmall: a string that provides the path to access the image file for the small image
    sizeLarge: a tuple containing the dimensions for the large image (length, width)
    sizeSmall: a tuple containing the dimensions for the Small image (length, width)

Return
    imageLarge: the large image with the small image placed in the middle of it
'''
def imageAppender(imgLarge:str, imgSmall:str, sizeLarge:tuple, sizeSmall:tuple):
    ''' Calculate the position to place the small image in the center of the large image'''
    # Need the length midpoint of the large image
    midpointLargeX = sizeLarge[0] / 2
    # Need the length midpoint of the small image
    midpointSmallX = sizeSmall[0] / 2
    # Need the width midpoint of the large image
    midpointLargeY = sizeLarge[1] / 2
    # Need the width midpoint of the small image
    midpointSmallY = sizeSmall[1] / 2
    # Calculate the length position to place the image
    positionX = midpointLargeX - midpointSmallX
    # Calculate the width position to place the image
    positionY = midpointLargeY - midpointSmallY
    # Convert the length position to an int since paste() won't accept floats
    positionX = int(positionX)
    # Convert the width position to an int since paste() won't accept floats
    positionY = int(positionY)

    imgLarge = imgLarge.resize(sizeLarge)
    # Resize the small image with the provided dimension tuple
    imgSmall = imgSmall.resize(sizeSmall)
    # Put the small image on the large image
    imgLarge.paste(imgSmall, (positionX,positionY), mask = imgSmall)
    # Return the large image with the appended small image
    return imgLarge





'''
image_initializer(): this function will intialize all the jpgs for the tkinter window to display on the buttons. It will
automatically be called when the user runs the file before the GUI window is displayed

Parameters: none

* this takes a little bit of time, so to prove to the user things are working there are command line 
outputs.
'''
def image_initializer():
    '''
    This function will intialize all the jpgs for the tkinter window to display on the buttons. It will
    automatically be called when the user runs the file

    * this takes a little bit of time, so to prove to the user things are working there are command line 
    outputs.
    '''

    #print statements to prove that their call actually mad things start up
    print()
    print("Welcome to Weather Adventures!")

    print("We are initiallizing the maps. This will take a moment. Thank you for your patience! ")




    cwd = os.getcwd()  # current working directory




    #####  CREATE NEW IMAGES FOR EUGENE #####

    #get the location for the original images
    eugene_path = cwd + "/images/mapImages/Eugene2x2/"
    #set the location for where the new images will be saved
    e_save_path = cwd + "/images/mapImages_symbols/Eugene2x2/"


    # loop through the photos for the Eugene map
    for i in range(1, 5):
        # open and resize the map image
        m_img = Image.open(eugene_path.strip() +  str(i) + ".png").resize((350, 350))

        #get the weather for the button and store it in the global variable WEATHER_INFO
        WEATHER_INFO["E" + str(i)] = weather.getWeatherInfo(str(EUGENE_COORD_NAMES[i-1][0]), str(EUGENE_COORD_NAMES[i-1][1]), "imperial")

        # open and resize the icon image for the particular weather and wind direction
        weather_img = Image.open(cwd + WEATHER_INFO["E" + str(i)][0]).resize((60, 78))
        wind_img = Image.open(cwd + WEATHER_INFO["E" + str(i)][1]).resize((60, 78))

        # call the imageAppender from InfoPopup.py to add the weather icon to the map button image
        new_img_weather = imageAppender(m_img, weather_img, (350, 350), (60, 78))
        #save the image
        new_img_weather.save(e_save_path + str(i) + ".png")

        # call the imageAppender from InfoPopup.py to add the wind icon to the map button image
        new_img_wind = imageAppender(m_img, wind_img, (350, 350), (60, 78))
        #save the image
        new_img_wind.save(e_save_path + str(i) + "_w" + ".png")
    



    ##### CREATE THE IMAGES FOR LANE COUNTY #####
    
   #get the location for the original images
    lane_path = cwd + "/images/mapImages/LaneCounty5x3/"
    #set the location for where the new images will be saved
    l_save_path = cwd + "/images/mapImages_symbols/LaneCounty5x3/"


    # loop through the photos for the Lane County map
    for i in range(1, 16):
        # open and resize the map image
        m_img = Image.open(lane_path.strip() +  str(i) + ".png").resize((160, 160))

        #get the weather for the button and store it in the global variable WEATHER_INFO
        WEATHER_INFO["L" + str(i)] = weather.getWeatherInfo(str(LANE_COORD_NAMES[i-1][0]), str(LANE_COORD_NAMES[i-1][1]), "imperial")

        # open and resize the icon image for the particular weather and wind direction
        weather_img = Image.open(cwd + WEATHER_INFO["L" + str(i)][0]).resize((40, 44))
        wind_img = Image.open(cwd + WEATHER_INFO["L" + str(i)][1]).resize((40, 44))

        # call the imageAppender from InfoPopup.py to add the weather icon to the map button image
        new_img_weather = imageAppender(m_img, weather_img, (160, 160), (40, 44))
        #save the image
        new_img_weather.save(l_save_path + str(i) + ".png")

        # call the imageAppender from InfoPopup.py to add the wind icon to the map button image
        new_img_wind = imageAppender(m_img, wind_img, (160, 160), (40, 44))
        #save the image
        new_img_wind.save(l_save_path + str(i) + "_w" + ".png")
    

    # maps are intialized let the user know through the command prompt
    print("Map is initalized!  Opening the application now.")
    print()
    
 







'''
more_info(): this function is called by the tkinter window when a button is pressed and will call the activity recommender
based on the weather of selected button

Parameter:
    zoom: this is an int and indicated which map we are looking at
    button_num: indicates which button was selected

Returns a popup with weather information and activity recommendations 
'''
def more_info(zoom: int, button_num: int):
    #get the information specialized per map
    if zoom == 1:
        # we are looking at the eugene map
        w = WEATHER_INFO["E" + str(button_num)] # weather of the button pressed
        coords = EUGENE_COORD_NAMES[button_num - 1] #the coordinates of the button pressed
        title  = "Eugene Recommendation"
    elif zoom == 2:
        # we are looking at the lane map
        w = WEATHER_INFO["L" + str(button_num)] # weather of the button pressed
        coords = LANE_COORD_NAMES[button_num - 1] #the coordinates of the button pressed
        title = "Lane County Recommendation"
    else:
        #zoom was not one of the expected outcomes
        print("BAD INPUT : ( ")
        return # return so it breaks here in a controlled manner instead of throwing errors later


    #the logic is the same for both maps after this:

    weather_string = "" #initialize the weather string, for the activity recommender

    isWind = "No" #initially set isWind to No
    if w[4] >= 15:
        # it is windy, set isWind to Yes
        isWind = "Yes"

    #Check the weather to pass to the Activivy recommender
    if "rain" in w[2] or "cloud" in w[2]:
        #it is raining  or cloudy set the the string to indicate
        weather_string += "isRain"
    elif "snow" in w[2] or "ice" in w[2] or "icy" in w[2]:
        #it is snowing / icy set weather_string to indicate
        weather_string += "isSnoworIce"
    else:
        #since it is not raining or snowing it is then
        weather_string += "isClear"

    
    #get the recommendations depending on the weather
    act_recomendations = Activity_Reccomender.zoom(zoom, weather_string, isWind, coords)
    #call the pop up creater to make a popup based on the weather and activities
    InfoPopup.createPopup(title, w, True, act_recomendations)
    
    

