'''
Author: Alexa Roskowski

This is the file that will be run by the user, and acts as the intermediary between all the files
'''

#import all the other files
import ButtonMaps
import Activity_Reccomender
import weather
import InfoPopup

#import the other libraries we need
import os
from PIL import Image



#####  GLOBALS   #####
WEATHER_INFO = {}  #store the weather infomation per button, so we as few as possible API calls)

# store the coordinates in a list to make it easier to reference
EUGENE_COORD_NAMES = [ButtonMaps.COORDINATES_EUG_1, ButtonMaps.COORDINATES_EUG_2,
                       ButtonMaps.COORDINATES_EUG_3, ButtonMaps.COORDINATES_EUG_4]

LANE_COORD_NAMES = [ButtonMaps.COORDINATES_LANE_1, ButtonMaps.COORDINATES_LANE_2, ButtonMaps.COORDINATES_LANE_3,
                     ButtonMaps.COORDINATES_LANE_4, ButtonMaps.COORDINATES_LANE_5, ButtonMaps.COORDINATES_LANE_6,
                     ButtonMaps.COORDINATES_LANE_7, ButtonMaps.COORDINATES_LANE_8, ButtonMaps.COORDINATES_LANE_9,
                     ButtonMaps.COORDINATES_LANE_10, ButtonMaps.COORDINATES_LANE_11, ButtonMaps.COORDINATES_LANE_12,
                     ButtonMaps.COORDINATES_LANE_13, ButtonMaps.COORDINATES_LANE_14, ButtonMaps.COORDINATES_LANE_15]



# REMEBER TO DELETE THIS AND USE THE ONE IN INFOpOPUP WHEN ITS DONE


'''
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
    # Open the large image to use
    #imageLarge = Image.open(pathLarge)
    # Open the small image to use
    #imageSmall = Image.open(pathSmall)
    # Resize the large image with the provided dimension tuple
    imgLarge = imgLarge.resize(sizeLarge)
    # Resize the small image with the provided dimension tuple
    imgSmall = imgSmall.resize(sizeSmall)
    # Put the small image on the large image
    imgLarge.paste(imgSmall, (positionX,positionY), mask = imgSmall)
    # Return the large image with the appended small image
    return imgLarge






def main():
    '''
    This function will intialize all the jpgs for the tkinter window to display on the buttons. It will
    automatically be called when the user runs the file

    * this takes a little bit of time, so to prove to the user things are working there are command line 
    outputs.
    '''
    print()
    print("Welcome to Weather Adventures!")

    print("We are initiallizing the maps. This will take a moment. Thank you for your patience! ")

    #call the map tkinter window to use the initialized images

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


    # loop through the photos for the Eugene map
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
    
    print("Map is initalized!  Opening the application now.")
    print()

    ButtonMaps.main()
    #call the tkinter and make it use the new initialized images





def more_info(zoom: int, button_num: int):
    '''
    This function is called by the tkinter window when a button is pressed
    '''
    #print(WEATHER_INFO)
    if zoom == 1:
        # we are looking at the eugene map
        InfoPopup.createPopup("Eugene Recommendation", WEATHER_INFO["E" + str(button_num)], True)
    elif zoom == 2:
        # we are looking at the lane map
        InfoPopup.createPopup( "Lane County Recommendation", WEATHER_INFO["E" + str(button_num)], True)
    


    # get the weather information for this specific button location from WEATHER_INFO
    # call Activity reccommender based on specified weather and zoom level

    # format the string to pass to the pop-up creater

    # call the pop-creater with more weather info and the recommended activities. 
    




if __name__ == "__main__":
    main()

    more_info(1, 1)
