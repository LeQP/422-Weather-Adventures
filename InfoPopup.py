"""
GraphGen.py
--------
Authors: Joey Le
Created: 3/3/2023
Last Modified: 3/3/2023
Purpose: This file creates the additional pop-up windows for when a user wants to learn more about a particular area's weather
and outdoor activities.

Revision History (Date | Author | Modifications)
----------------------------------------------
3/3/2023 | Joey Le | Created initial file
3/3/2023 | Joey Le | Created imageAppender()
3/4/2023 | Joey Le | Created createPopup()
3/4/2023 | Joey Le | Further developed createPopup() for a basic format
3/6/2023 | Joey Le | Added more detailed weather and wind descriptions in pop-up by creating createWeatherDesc() and createWindDesc()
3/7/2023 | Joey Le | Added further documentation for createWeatherDesc() and createWindDesc()
3/7/2023 | Joey Le | Added display for outdoor activitites into createPopup


"""

''' Module needed to form Windows '''
# Import tkinter module to create windows
import tkinter
import tkinter.ttk as tkTtk
# For setting text fonts
import tkinter.font as tkFont 
# Import os Access current working directory
import os
# Manipulate images
from PIL import Image   # Open images
# Import weather.py to gather weather data
import weather
from PIL import ImageTk # Have images available for Tkinter
import webbrowser
#########################################################################################################################################
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
def imageAppender(pathLarge:str, pathSmall:str, sizeLarge:tuple, sizeSmall:tuple):
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
    imageLarge = Image.open(pathLarge)
    # Open the small image to use
    imageSmall = Image.open(pathSmall)
    # Resize the large image with the provided dimension tuple
    imageLarge = imageLarge.resize(sizeLarge)
    # Resize the small image with the provided dimension tuple
    imageSmall = imageSmall.resize(sizeSmall)
    # Put the small image on the large image
    imageLarge.paste(imageSmall, (positionX,positionY), mask = imageSmall)
    # Return the large image with the appended small image
    return imageLarge

'''
createWeatherDesc(): a helper function to create the descriptive text to describe the weather on the window pop-up

Parameters:
    WeatherStr: a string that provides the description of the weather provided by the openweathermap API
    temp: an int that represents the temperature (without considering the unit)
    imperial: a bool to define whether the temperature measurement is in fahrenheit (True) or celsius (False)

Return:
    resStr: a string that displays the exact description for the weather of the window pop-up
'''
def createWeatherDesc(weatherStr:str, temp:int, imperial:bool):
    ''' Initialize variables to use for creating the descripition text '''
    descVal = ""    # Describes the weather condition and may be the same as weatherStr
    unit = ""       # The unit to describe the temperature
    ''' Some descriptions need a slight grammar adjustment so check for specific descriptions that would require it '''
    # Applicable descrpitions that would need an adjustment to the begging: clear sky, thunderstorm, drizzle, and tornado
    if (weatherStr.find("clear sky") or weatherStr.find("thunderstorm") or weatherStr.find("drizzle") or weatherStr.find("tornado")):
        # Adjust these descriptions by appending "a" to the beginning
        descVal = "a " + weatherStr
    # Some descriptions don't need adjustment (ex. rain, snow)
    else:
        # Keep the description as is then
        descVal = weatherStr

    ''' Declare the unit variable to store the unit (fahrenhei or celsius) '''
    # If the user specified imperial
    if (imperial):
        # Then let the temperature be in fahrenheit
        unit = " fahrenheit."
    # Otherwise the user wanted celsius
    else:
        # Then let the temperature be in celsius
        unit = " celsius."
    '''
    After any description grammar adjustment has been made and the units has been specififed, form the description to be displayed.
    If it is too long to display on the pop-up window on one line, then break it down to two lines.
    '''
    # Form the description string to return
    resStr = "This area is currently experiencing " + descVal + " at " + str(temp) + " degrees" + unit
    # Acquire its length
    strLen = len(resStr)
    # Find the first space character past the 50th character
    if (strLen > 50):
        # Find the first space character past the 50th character
        index = resStr.find(" ", 50, strLen)
        # If found, then replace the space with a new line. If it cannot be found, 
        # the current word is the last word on the line and no space is needed
        if (index != -1):
            # Replace the space with a new line.
            resStr = resStr[:index] + "\n" + resStr[index + 1:]
        # Return the string that describes the wind
    return resStr

'''
createWindDesc(): a helper function to create the descriptive text to describe the wind on the window pop-up

Parameters:
    windDir: an int that provides the degree of the wind from 0 to 345 going clockwise
    windSpeec: an int that represents the wind speed without considering the unit
    imperial: a bool to define whether the wind speed measurement is in miles (True) or kilometers (False) per hour

Return:
    resStr: a string that displays the exact description for the wind of the window pop-up
'''
def createWindDesc(windDir:int, windSpeed:int, imperial:bool):
    '''
    This forms a dicitionary to convert the wind direction degree to understandable english terms for the wind description.
    '''
    dict = {
        0 : "north",
        15: "north and slightly towards the northeast",
        30: "northeast and slightly towards the north",
        45: "northeast",
        60: "northeast and slightly towards the east",
        75: "east and slightly towards the northeast",
        90: "east",
        105: "east and slightly towards the southeast",
        120: "southeast and slightly towards the east",
        135: "southeast",
        150: "southeast and slightly towards the south",
        165: "south and slightly towards the southeast",
        180: "south",
        195: "south and slightly towards the southwest",
        210: "southwest and slightly towards the south",
        225: "southwest",
        240: "southwest and slightly towards the west",
        255: "west and slightly towards the southwest",
        270: "west",
        285: "west and slightly towards the northwest",
        300: "northwest and slightly towards the west",
        315: "northwest",
        330: "northwest and slightly towards the north",
        345: "north and slightly towards the northwest"
    }
    '''
    Provide the specific the unit based on imperial or metric unit specified by the user.
    '''
    # Declare the unit variable to store the unit (miles per hour or kilometers per hour)
    unit = ""
    # If the user specified imperial
    if (imperial):
        # Set units to be miles per hour
        unit = " miles per hour."
    # Otherwise, the user wanted metric units
    else:
        # Then Set units to be kilometers per hour
        unit = " kilometers per hour."
    '''
    After both the wind direction has been translated and the units has been specififed, form the description to be displayed.
    If it is too long to display on the pop-up window on one line, then break it down to two lines.
    '''
    # Form the description string to return
    resStr = "The wind is blowing " + dict[windDir] + " at " + str(windSpeed) + unit
    # Acquire its length
    strLen = len(resStr)
    # If the length is too long to be on one line (over 50 characters), break it up to two lines
    if (strLen > 50):
        # Find the first space character past the 50th character
        index = resStr.find(" ", 50, strLen)
        # If found, then replace the space with a new line. If it cannot be found, 
        # the current word is the last word on the line and no space is needed
        if (index != -1):
            # Replace the space with a new line.
            resStr = resStr[:index] + "\n" + resStr[index + 1:]
        # Return the string that describes the wind
    return resStr
'''
createPopup(): a function that creates a small tkinter pop-up window when a user wishes to know more
               about a specific region on the grid 

Parameters:
    title: a string to display at the top of the pop up as a title
    apiInfo: a list that provides all the weather information collected for area under the specific region
    imperial: a bool for if the user wants to see the temperature in fahrenheit and wind direction in miles (True) 
              or temperature in celsius and wind direction in kilometers (False)

Return:
    A tkinter window to view additional weather information and outdoor activitites
'''

def openWebsite(url:str):
    webbrowser.open_new_tab(url)
    
def getActivityDisplay(activity:dict):
    nameStr = "Name: " + activity["name"] + "\n"
    descStr = activity["description"] + "\n"
    diffStr = "Difficulty: " + activity["difficulty"] + "\n"
    locationStr = "Location: " + activity["address"] + "\n"
    websiteStr = "Learn More: " + activity["source"]
    #displayList = [nameStr, descStr, diffStr, locationStr, websiteStr]

    return nameStr + descStr + diffStr + locationStr + websiteStr

def createPopup(title:str, apiInfo:list, imperial:bool, activityList:list):
    '''
    Set up the Tkinter Window for the pop-up
    '''
    # Initialize the window
    window = tkinter.Tk()
    # Initialize the window's dimensions
    window.geometry("1300x650")
    # Set the window's title
    window.title(title)

    weatherIconPath = apiInfo[0]
    windDirIconPath = apiInfo[1]
    weatherDesc = apiInfo[2]
    temp = apiInfo[3]
    windSpeed = apiInfo[4]
    windDir = apiInfo[5]
    vis = apiInfo[6]
    humid = apiInfo[7]
    
    ''' Open the different images and make them compatable with Tkinter windows'''
    # Open the weather image for use
    imageWeather = Image.open(weatherIconPath)
    # Open the wind direction image for use
    imageWind = Image.open(windDirIconPath)
    # Reformat the weather iamge to an appropiate size for the pop-up
    imageWeather = imageWeather.resize((150, 150))
    # Reformat the wind direction iamge to an appropiate size for the pop-up
    imageWind = imageWind.resize((150, 150))
    # Allow the weather image to be placed in a Tkinter window for the pop-up
    imageWeather = ImageTk.PhotoImage(imageWeather)
    # Allow the wind direction image to be placed in a Tkinter window for the pop-up
    imageWind = ImageTk.PhotoImage(imageWind)

    ''' Create the text to go alongside the images '''
    # Create the different fonts to use between the heading and body text
    fontStyleHeading = tkFont.Font(family="Arial", size=32) # Heading font font: Arial font of Size 36
    fontStyleBody = tkFont.Font(family="Arial", size=12)    # Body text font: Arial font of size 18
    
    ''' 
    Use frames to organize the weather and wind information into their own distinct groups; 
    also include a frame for the pop-up heading.
    After putting in the applicable images and text, put those frames into the window for viewing.
    '''
    frameWeatherHeading = tkinter.Frame(window)    # Heading
    frameActivityHeading = tkinter.Frame(window)    # Heading
    frameWeather = tkinter.Frame(window)    # Weather Information
    frameWind = tkinter.Frame(window)       # Wind direction image
    
    ''' Put the images into labels to apply to the frames'''
    # Create the label for the weather image
    labelWeatherImage = tkinter.Label(frameWeather, image = imageWeather) 
    # Create the label for the wind direction image
    labelWindImage = tkinter.Label(frameWind, image = imageWind) 

    ''' Create the different labels that incorporate the text to put into each frame '''
    # Start by creating the appropiate text for the weather and wind information
    weatherText = createWeatherDesc(weatherDesc, temp, imperial)    # Appropiate weather text
    windText = createWindDesc(windDir, windSpeed, imperial)         # Appropriate wind text
    # Then create the labels
    labelWeatherHeading = tkinter.Label(frameWeatherHeading, text = "Weather", justify='center', font = fontStyleHeading)              # Heading for Weather information     
    labelActivityHeading = tkinter.Label(frameActivityHeading, text = "Outdoor Activities", justify='left', font = fontStyleHeading) # Heading for Outdoor activities
    labelWeatherText = tkinter.Label(frameWeather, text = weatherText, justify = "left", font = fontStyleBody) # Descriptive text to go alongside weather iamge
    labelWindText = tkinter.Label(frameWind, text = windText, justify = "left", font = fontStyleBody)          # Descriptive text to go alongside wind direction iamge

    ''' Place the heading, weather information, and wind direction information into their respective frames'''
    # Place the header text into the Heading Frame
    labelWeatherHeading.pack(side = "top")
    labelActivityHeading.pack(side = "top")

    # The Weather Frame
    labelWeatherImage.pack(side = "left")   # Place the image into the frame first
    labelWeatherText.pack(side = "left")    # Place the text into the frame second

    # The Wind Frame
    labelWindImage.pack(side = "left")  # Place the image into the frame first
    labelWindText.pack(side = "left")   # Place the text into the frame second
    

    '''
    Work on Displaying the Outdoor activitites
    '''
    frameActivityList = []
    print(len(activityList))
    for i in range(len(activityList)):
        print(activityList)
        frameActivityListNew = tkinter.Frame(window)
        textList = getActivityDisplay(activityList[i])
        #for i in range(5):
            #tkinter.Label(frameActivityListNew, text = textList[i], justify="left").pack(side = "top")
        tkinter.Label(frameActivityListNew, text = textList, justify="left", font=fontStyleBody).pack(side = "top") 
        frameActivityList.append(frameActivityListNew)


    ''' Finally, put the frames onto the tkinter window'''
    vertLine = tkTtk.Separator(window, orient="vertical")
    frameWeatherHeading.grid(row = 0, column = 0)           # Weather Heading goes first
    frameWeather.grid(row = 1, column = 0, sticky = "W")    # Followed by the weather information
    frameWind.grid(row = 2, column = 0, sticky = "W")       # Then finish the window with the wind information
    vertLine.grid(row = 0, column = 1, sticky = "ns", rowspan = 9)  # Add a vertical line to seperate the weather from outdoor activities
    frameActivityHeading.grid(row = 0, column = 2, sticky = "W")          # Then start with the outdoor activitites

    for i in range(len(frameActivityList)):
        frameActivityList[i].grid(row = i + 1, column = 2, sticky = "W")

    # Run the window
    window.mainloop()


''' Run the program on it is own for debugging purposes'''
if __name__ == "__main__":
    # Get the current working directory
    cwd = os.getcwd()
    #cwd = os.path.dirname(os.path.abspath(__file__))
    ''' Feel free to change the paths and tuple sizes to test other images and sizes '''
    # The large image 
    pathL = cwd + "/images/mapImages/Eugene2x2/1.png"
    # The small image 
    pathS = cwd + "/images/weatherSymbols/misc.png"
    # The large image dimension
    tupleL = (300, 250)
    # The large image dimension
    tupleS = (50, 78)
    # Run the function
    imageRet = imageAppender(pathL, pathS, tupleL, tupleS)
    # Display the image; comment out if you only see want to see the sample popup
    #imageRet.show()
    # Variable that can be changed to view in imperial or metric for sample popup
    viewImperial = True
    # Display sample popup
    '''
    Below, each letter corresponds to the index of a list (a = 0th, b = 1th, c = 2nd, etc.) and the number
    corresponds to which list it belongs (sampleList1, sampleList2, sampleList3). Any of these can be changed to
    test out different values.
    '''
    # Path to weather icon image
    a1 = cwd + "/images/weatherSymbols/rain.png"
    a2= cwd + "/images/weatherSymbols/clear.png"
    a3 = cwd + "/images/weatherSymbols/snow.png"
    # Path to wind direction image
    b1 = cwd + "/images/weatherSymbols/w195.png"
    b2 = cwd + "/images/weatherSymbols/w225.png"
    b3 = cwd + "/images/weatherSymbols/w345.png"
    # Description of weather
    c1 = "thunderstorm with rain"   
    c2 = "clear sky"
    c3 = "heavy shower snow"
    # Temperature of the weather
    d1 = 30
    d2 = 50
    d3 = 70
    # Wind Speed
    e1 = 5
    e2 = 10
    e3 = 15
    # Wind Direction
    f1 = 195
    f2 = 225
    f3 = 345
    # Visibility
    g1 = 10000
    g2 = 9000
    g3 = 8000
    # Humidity
    h1 = 70
    h2 = 65
    h3 = 60
    '''
    These are the sample lists that would be returned when calling the OpenWeatherMap API for debugging purposes
    '''
    sampleList1 = [a1, b1, c1, d1, e1, f1, g1, h1]
    sampleList2 = [a2, b2, c2, d2, e2, f2, g2, h2]
    sampleList3 = [a3, b3, c3, d3, e3, f3, g3, h3]

    dict1 = {
        "name": "Bird Watching at Mt. Pisgah",
        "description": "Bring your binoculars and enjoy a lovely, relaxing walk here at Mt. Pisgah. This activity requires a $5 pass so please keep that in mind.",
        "difficulty": "Easy", 
        "isWind": "Yes",
        "isClear": "Yes",
        "isRain": "Yes, although it might be a little chilly or wet, as long as you're comfortable in a rain jacket this will be a great activity for you.",
        "isSnoworIce": "No",
        "address":"34639 Frank Parrish Rd, Eugene, OR 97405",
        "coordinates":"44.01497597816823, -122.98278078659796",    
        "source": "https://www.eugenecascadescoast.org/listing/buford-park-%26-mt-pisgah-birding-%26-water-trails/13437/"
    }

    dict2 = {
        "name": "Rock Climbing",
        "description": "Head over to the University of Oregon Rec Center for this one. It's cold, it's raining, maybe it's snowing... all we know is that we are looking for a non-outdoor activity today, and we've got one for you! Head over the the rec center rock wall to spend some time bouldering. Luckily for you (if you're a student) this wall is totally free and you can even rent shoes there. All you need to bring is your student id and yourself. Enjoy some heart racing moments!",
        "difficulty": "Moderate", 
        "isWind": "Yes",
        "isClear": "No",
        "isRain": "Yes",
        "isSnoworIce": "Yes",
        "address":"1320 E 15th Ave, Eugene, OR 97403",
        "coordinates":"44.042594927661476, -123.0734221019393",    
        "source": "interviewee reccomendation"
    }

    dict3 = {
        "name": "Alton Baker",
        "description": "Spend the day leisurely walking or biking through the vast park that is Alton Baker, which spans from Eugene, Springfield, Coburg, and the Valley River areas. The paths in Alton Baker include paved bike paths as well as running and walking paths.",
        "difficulty": "Easy", 
        "isWind": "Yes",
        "isClear": "Yes",
        "isRain": "Yes",
        "isSnoworIce": "No",
        "address":"100 Day Island Rd, Eugene, OR 97401",
        "coordinates":"44.05298827336223, -123.06722865961001",    
        "source": "https://www.eugenecascadescoast.org/listing/alton-baker-park/3303/"
    }
    dictList = [dict1, dict2, dict3]
    # Run the pop-up function; change the sampleList to test a different set
    createPopup("Sample Title", sampleList1, viewImperial, dictList)


