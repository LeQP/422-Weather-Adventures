"""
GraphGen.py
--------
Authors: Joey Le
Created: 3/3/2023
Last Modified: 3/10/2023
Purpose: This file creates the additional pop-up windows for when a user wants to learn more about a particular area's weather
and outdoor activities.

Revision History (Date | Author | Modifications)
----------------------------------------------
3/03/2023 | Joey Le | Created initial file
3/03/2023 | Joey Le | Created imageAppender()
3/04/2023 | Joey Le | Created createPopup()
3/04/2023 | Joey Le | Further developed createPopup() for a basic format
3/06/2023 | Joey Le | Added more detailed weather and wind descriptions in pop-up by creating createWeatherDesc() and createWindDesc()
3/07/2023 | Joey Le | Added further documentation for createWeatherDesc() and createWindDesc()
3/07/2023 | Joey Le | Added display for outdoor activitites into createPopup()
3/08/2023 | Joey Le | Removed imageAppender() as it is used in weather_adventures.py instead
3/08/2023 | Joey Le | Reorganized information displayed for each outdoor activity with bullet points and a button to view website
3/08/2023 | Joey Le | Added Visibility and Humidity to the Pop-up window
3/08/2023 | Joey Le | Addded comments to document recent adjustments
3/10/2023 | Joey Le | Updated createPopUp() by having it access image paths by also accessing the current working directory as well
                      and other minor adjustments have been made
"""

''' Module needed to form Windows '''
# Import tkinter module to create windows
import tkinter
# Import .ttk from Tkinter to form a vertical line
import tkinter.ttk as tkTtk
# Import .font from Tkinter for setting text fonts
import tkinter.font as tkFont 
# Import os to access current working directory
import os
# Import Image from Pillow Module for manipulating images
from PIL import Image
# Import ImageTk from Pillow Module for displaying images on Tkinter Window
from PIL import ImageTk
# Import Webbrowser module to open URL links of outdoor activitites
import webbrowser

'''
addNewLines(): a helper function for adding new lines within strings to be displayed on the Tkinter pop-up window;
               This is used by other helper functions and createPopUp().

Parameters:
    longStr: a string that involves the display text potentially considered too long to display on the pop-up window on one line,
             so it needs to be broken down to multiple lines.
    limitEst: an int to provide a general character limit for each line; this function will add a new line to the first white space
              after the character found at the limitEst-th character in longStr.
    bulletPoint: a bool to determine if the function is working with outdoor activity-related text which uses bullet points. This function
                 performs an additional step to adjust spacing for text that involve a bullet point.

Return:
    retStr: the string to return that stores the newly formated string that comes with newlines to allow it to spread across more than one line.

'''
def addNewLine(longStr:str, limitEst:int, bulletPoint:bool):
    ''' Initialize variables to use for this function'''
    # currStr represents the string or string subset of longStr to use when breaking it into multiple lines
    currStr = longStr
    # retStr represents the return variable in which the function will return a string
    retStr = longStr 
    # strLen represents the length of currStr and an initial value is taken to begin a loop regarding the string's length
    strLen = len(currStr)
    # collection represents the amount of indices and additions of spaces and new lines 
    # already covered when addressing the need for incorporating new lines
    # This is used to calculate the current position alongside to place the new line
    collection = 0

    '''
    The function handles the inclusion of new lines by searching through currStr which is a subset of the string that needs
    to be checked and adjusted if needed. With each iteration, around limitEst characters will be accounted for. This results in 
    currStr decreasing in size by becoming a smaller string composing of all remaining characters past the recent new line addition.
    '''
    # The loop will continue until the remaining characters can all fit on the current line by being under the character limit established by limitEst
    while(len(currStr) > limitEst):
        # Find the first space character past the limitEst index
        index = currStr.find(" ", limitEst, len(currStr))
        # If found, then replace the space with a new line.
        if (index != -1):
            # Replace the space with a new line.
            retStr = retStr[:collection + index] + "\n" + retStr[collection + index + 1:]
            # Check if the string involves bullet points
            if (bulletPoint == False):
                # With no bullet points, another iteration can occur
                currStr = currStr[index + 1:strLen]
                collection = collection + index + 1
            else:
                # With bullet points, lines after the first one have to have three spaces to align with the bullet point's placement
                retStr = retStr[:collection + index + 1] + "   " + retStr[collection + index + 1:]
                # Update currStr to contain only the remaining subset of longStr
                currStr = currStr[index + 1:strLen]
                # Update collection to include the addition of the newline character and spaces
                collection = collection + index + 4
        # Otherwise, the string is sufficient as a white space can't be found since a character in the last word would result in index = -1
        else:
            # In that case, the loop can stop
            break
    # Return the newly formated string
    return retStr

#########################################################################################################################################

'''
createWeatherDesc(): a helper function to create the descriptive text to describe the weather on the window pop-up

Parameters:
    WeatherStr: a string that provides the description of the weather provided by the openweathermap API
    temp: an int that represents the temperature (without considering the unit)
    imperial: a bool to define whether the temperature measurement is in fahrenheit (True) or celsius (False)

Return:
    retStr: a string that displays the exact description for the weather of the window pop-up
'''
def createWeatherDesc(weatherStr:str, temp:int, imperial:bool):
    ''' Initialize variables to use for creating the descripition text '''
    # descVal describes the weather condition and may be the same as weatherStr
    # Unit describes the temperature
    descVal = ""    
    unit = ""  

    ''' Some descriptions need a slight grammar adjustment so check for specific descriptions that would require it '''
    # Applicable descrpitions that would need an adjustment to the begging: clear sky, thunderstorm, drizzle, and tornado
    if (weatherStr.find("clear sky") != -1 or weatherStr.find("thunderstorm") != -1 or weatherStr.find("drizzle") != -1 or weatherStr.find("tornado") != -1):
        # Adjust these descriptions by appending "a" to the beginning
        print(weatherStr)
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
    retStr = "This area is currently experiencing " + descVal + " at " + str(temp) + " degrees" + unit
    # Break the line apart if it is too long for the pop-up window
    retStr = addNewLine(retStr, 50, False)
    # Return the string after assessing and modifying the lines if needed
    return retStr
#########################################################################################################################################

'''
createWindDesc(): a helper function to create the descriptive text to describe the wind on the window pop-up

Parameters:
    windDir: an int that provides the degree of the wind from 0 to 345 going clockwise
    windSpeec: an int that represents the wind speed without considering the unit
    imperial: a bool to define whether the wind speed measurement is in miles (True) or kilometers (False) per hour

Return:
    retStr: a string that displays the exact description for the wind of the window pop-up
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
    retStr = "The wind is blowing " + dict[windDir] + " at " + str(windSpeed) + unit
     # Break the line apart if it is too long for the pop-up window
    retStr = addNewLine(retStr, 50, False)
    # Return the string after assessing and modifying the lines if needed
    return retStr
#########################################################################################################################################
'''
createVisAndHumText(): a helper function to form the text that describes the weather's visibility and humidity on the pop-up window

Parameters:
    vis: an int representing one's visibility, or the ability to view a certain amount of distance accurately, within an area.
    hum: an int representing the percent of the humididty
    imperial: a bool to check for a request for the visibility in feet (True) or in kilometers (False)

Return:
    retStr: a string to contain the text to display on the pop-up window regarding the visibility and humididty
'''

def createVisAndHumText(vis:int, hum:int, imperial:bool):
    # Declare the unit variable to store the unit (feet or kilometers)
    unit = ""

    # Check for the imperial measurement (i.e if the request is for feet)
    if (imperial):
        # Specify that the unit is to represent feet
        unit = "feet"
    # Otherwise, the measurment is supposed to be in metric (i.e kilometers)
    else:
        # Specify that the unit is to represent kilometers
        unit = "kilometers"
    # Form the string to return by compiling the text to describe the visibility and humidity
    retStr = "Humidity = " + str(hum) + "%\tVisbility = " + str(vis) + " " + unit
    # Afterwards, return the string 
    return retStr 
#########################################################################################################################################
'''
openWebsite(): a button function that would open up the request Outdoor Activity's website when clicked on

Paramters:
    url: a string that represents the website link to access.

Return:
    a webpage opened up in the user's web browser representing the outdoor activity that the button is associated with.

'''
def openWebsite(url:str):
    # Use the webbrowser module to help open the website
    webbrowser.open_new_tab(url)
#########################################################################################################################################

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
def createPopup(title:str, apiInfo:list, imperial:bool, activityList:list):
    '''
    Set up the Tkinter Window for the pop-up
    '''
    # Initialize the window
    window = tkinter.Toplevel()
    # Initialize the window's dimensions
    window.geometry("1450x700")
    # Set the window's title
    window.title(title)

    '''
    Acquire all the API weather information into intuitive variables
    '''
    # Get the current working directory to access image files
    path = os.getcwd()
    # 0th Index represents the image string path to the weather icon to display
    weatherIconPath = path + apiInfo[0]
    # 1st Index represents the image string path to the wind direction icon to display
    windDirIconPath = path + apiInfo[1]
    # 2nd Index represents the string description describing the weather
    weatherDesc = apiInfo[2]
    # 3rd Index represents an int regarding the temperature
    temp = apiInfo[3]
    # 4th Index represents a float regarding the wind speed
    windSpeed = apiInfo[4]
    # 5th Index represents an int regarding the degree of the wind direction
    windDir = apiInfo[5]
    # 6th Index represents an int regarding the visibility range
    vis = apiInfo[6]
    # 7th Index represents the humidity of the weather
    humid = apiInfo[7]

    '''
    Afterwards, the rest of the functions serves to create the pop-up window by breaking it down to multiple frames, or chunks, to
    display the information on the Tkinter function. Each frame would have its own parts that organized within that frame, then the frames
    are organized within the window
    '''
    
    ''' 
    Use frames to organize the weather, wind, visibility and humidity information into their own distinct groups; 
    also include a frame for the pop-up heading. After putting in the applicable images and text, put those frames 
    into the window for viewing.
    '''
    frameWeatherHeading = tkinter.Frame(window)    # Heading for the Weather Section
    frameActivityHeading = tkinter.Frame(window)    # Heading for the Outdoor Activities Section
    frameWeather = tkinter.Frame(window)    # Weather Information (condition and wind direction)
    frameVisAndHum = tkinter.Frame(window)  # Weather Information (visibility and humidity)
    frameWind = tkinter.Frame(window)       # Wind direction information
    frameActivityList = []                  # A list that stores all the frames for each outdoor activity option to display

    ''' Create the fonts to use through the different frames '''
    fontStyleHeading = tkFont.Font(family="Arial", size=32) # Heading font for the weather and outdoor activity sections
    fontStyleBody = tkFont.Font(family="Arial", size=12)    # Body font for the text describing the weather and outdoor options
    fontStyleActivity = tkFont.Font(family="Arial", size=18, underline=True) # Sub-heading font used for the different outdoor activities on display
    fontStyleVisAndHum = tkFont.Font(family="Arial", size=18) # Body font for the text describing the visibility and humidity

    '''
    Start by developing the frames for the entire weather section including the header and the informatio gathered from the API.
    '''

    ''' Open the different images and make them compatable with Tkinter windows. '''
    # Open the weather image for use
    imageWeather = Image.open(weatherIconPath)
    # Open the wind direction image for use
    imageWind = Image.open(windDirIconPath)
    # Reformat the weather image to an appropiate size for the pop-up
    imageWeather = imageWeather.resize((150, 150))
    # Reformat the wind direction iamge to an appropiate size for the pop-up
    imageWind = imageWind.resize((150, 150))
    # Allow the weather image to be placed in a Tkinter window for the pop-up
    imageWeather = ImageTk.PhotoImage(imageWeather)
    # Allow the wind direction image to be placed in a Tkinter window for the pop-up
    imageWind = ImageTk.PhotoImage(imageWind)

    ''' Put the images into labels to apply to the appropiate frames'''
    # Create the label for the weather image
    labelWeatherImage = tkinter.Label(frameWeather, image = imageWeather) 
    # Create the label for the wind direction image
    labelWindImage = tkinter.Label(frameWind, image = imageWind) 

    '''
    Next, create the different labels that incorporate the text to put into each frame.  
    '''

    ''' Use the helper functions to form text to display for each weather information section '''
    weatherText = createWeatherDesc(weatherDesc, temp, imperial)    # Appropiate weather text
    windText = createWindDesc(windDir, windSpeed, imperial)         # Appropriate wind text
    visAndHumText = createVisAndHumText(vis, humid, imperial)       # Appropriate visbility and humidity text

    ''' Then create the labels'''
    # Form the label for the weather heading
    labelWeatherHeading = tkinter.Label(frameWeatherHeading, text = "Weather", justify='center', font = fontStyleHeading)    
    # Form the label for the type of weather and temperature
    labelWeatherText = tkinter.Label(frameWeather, text = weatherText, justify = "left", font = fontStyleBody)
    # Form the label for the wind direction and speed
    labelWindText = tkinter.Label(frameWind, text = windText, justify = "left", font = fontStyleBody)
    # Form the label for the visibility and humidity information
    labelVisAndHum = tkinter.Label(frameVisAndHum, text = visAndHumText, justify="center", font=fontStyleVisAndHum)
    

    ''' Place the heading, weather information, and wind direction information into their respective frames'''
    # Place the header text into the Heading Frame
    labelWeatherHeading.pack(side = "top")      # Weather Heading
    

    # The Weather Frame
    labelWeatherImage.pack(side = "left")   # Place the image into the frame first
    labelWeatherText.pack(side = "left")    # Place the text into the frame second

    # The Wind Frame
    labelWindImage.pack(side = "left")  # Place the image into the frame first
    labelWindText.pack(side = "left")   # Place the text into the frame second

    # The Visibility and Humidity Frame
    labelVisAndHum.pack(side="top") # There is only one item to insert, so insert just the label

    '''
    After the weather section frames have been established, begin establishing the frames for the Outdoor Activitites section.
    '''

    ''' Start by creating the header frame for outdoor activitites'''
    # Form the label for the activity heading
    labelActivityHeading = tkinter.Label(frameActivityHeading, text = "Outdoor Activities", justify='center', font = fontStyleHeading) # Heading for Outdoor activities
    # Then place the heading into the frame
    labelActivityHeading.pack(side = "top") 

    ''' 
    Afterwards, use a for-loop to go through each activity provided in the activity list (activityList).
    Each activity gets its own frame containing all relevant information regarding that activity;
    these will be placed below the Outdoor Activity heading frame. 
    '''
    # Each loop iteration is on a different activity found in activityList
    for i in range(len(activityList)):
        # Form the new frame containing the activity in this loop iteration
        newAlFrame = tkinter.Frame(window)
        # Form a label to provide the activity's name
        nameLabel = tkinter.Label(newAlFrame, text = activityList[i]["name"], font=fontStyleActivity)
        # Form a label to provide a description of the activity
        # It may be too long, so use addNewLine() to break it down into multiple lines
        infoLabelText = addNewLine("• " + activityList[i]["description"], 105, True)
        # After reformattting the text, put it into the label
        infoLabel = tkinter.Label(newAlFrame, text = infoLabelText, font=fontStyleBody, justify="left")
        # Form a label describing the activity's difficulty
        diffLabel = tkinter.Label(newAlFrame, text = "• Difficulty: " + activityList[i]["difficulty"], font=fontStyleBody, justify = "left")
        # Form a label describing the address of the activity
        locLabel = tkinter.Label(newAlFrame, text = addNewLine("• Location: " + activityList[i]["address"], 105, True), font=fontStyleBody, justify = "left")
        # Create a button to allow users to learn more about the activity by clicking the button to be take to a website
        webButton = tkinter.Button(newAlFrame, text = "Click to View Website", font = fontStyleBody, bg='white', fg = "dark green", command=lambda i=i: openWebsite(activityList[i]["source"]))
        ''' Place each label onto the frame then place the frame into the list. '''
        # Add the name label first
        nameLabel.grid(row = 0, column = 0, sticky = "W")
        # Add the info label second
        infoLabel.grid(row = 1, column = 0, sticky = "W")
        # Add the difficulty label third
        diffLabel.grid(row = 2, column = 0, sticky = "W")
        # Add the location label fourth
        locLabel.grid(row = 3, column = 0, sticky = "W")
        # Add the button at the end of all the information
        webButton.grid(row = 4, column = 0, sticky = "W")
        # Add the compiled frame into the list of activity frames to place
        frameActivityList.append(newAlFrame)

    
    ''' Finally, put the assembled frames onto the tkinter window'''
    # Start by creating a vertical line that would seperate the weather section to the outdoor activitites
    vertLine = tkTtk.Separator(window, orient="vertical")
    # Add the vertical line into the pop-up window
    vertLine.grid(row = 0, column = 1, sticky = "ns", rowspan = 9, padx=20)  

    ''' Weather Section '''
    # Weather Heading goes first
    frameWeatherHeading.grid(row = 0, column = 0)
    # Followed by the weather information regarding the condition and temperature           
    frameWeather.grid(row = 1, column = 0, sticky = "W")    
    # Followed by the wind information regarding speed and direction
    frameWind.grid(row = 2, column = 0, sticky = "W")       
    # Then lastly, add the visibility and humidity information at the bottom
    frameVisAndHum.grid(row = 3, column = 0)

    ''' Outdoor Activity Section '''
    # Place the heading first
    frameActivityHeading.grid(row = 0, column = 2)
    # Afterwards, place each activity frame below the heading and below the most recent addition to the window
    for i in range(len(frameActivityList)):
        # Use the loop to access the different activitites found in the list
        frameActivityList[i].grid(row = i + 1, column = 2, sticky = "W", pady = 10)

    # Run the window
    window.mainloop()
#########################################################################################################################################

''' Run the program on it is own for debugging purposes; this is not considered a part of the main system'''
if __name__ == "__main__":
    # Variable that can be changed to view in imperial or metric for sample popup
    viewImperial = True
    # Display sample popup
    '''
    Below, each letter corresponds to the index of a list (a = 0th, b = 1th, c = 2nd, etc.) and the number
    corresponds to which list it belongs (sampleList1, sampleList2, sampleList3). Any of these can be changed to
    test out different values.
    '''
    # Path to weather icon image
    a1 = "/images/weatherSymbols/rain.png"    # 0th index for sampleList1
    a2= "/images/weatherSymbols/clear.png"    # 0th index for sampleList2
    a3 = "/images/weatherSymbols/snow.png"    # 0th index for sampleList3
    # Path to wind direction image
    b1 = "/images/weatherSymbols/w195.png"    # 1st index for sampleList1
    b2 = "/images/weatherSymbols/w225.png"    # 1st index for sampleList2
    b3 = "/images/weatherSymbols/w345.png"    # 1st index for sampleList3
    # Description of weather
    c1 = "thunderstorm with rain"                   # 2nd index for sampleList1   
    c2 = "clear sky"                                # 2nd index for sampleList2
    c3 = "heavy shower snow"                        # 2nd index for sampleList3
    # Temperature of the weather
    d1 = 30                                         # 3rd index for sampleList1
    d2 = 50                                         # 3rd index for sampleList2
    d3 = 70                                         # 3rd index for sampleList3
    # Wind Speed
    e1 = 5                                          # 4th index for sampleList1
    e2 = 10                                         # 4th index for sampleList2
    e3 = 15                                         # 4th index for sampleList3
    # Wind Direction
    f1 = 195                                        # 4th index for sampleList1
    f2 = 225                                        # 4th index for sampleList2
    f3 = 345                                        # 4th index for sampleList3
    # Visibility
    g1 = 10000                                      # 5th index for sampleList1
    g2 = 9000                                       # 5th index for sampleList2
    g3 = 8000                                       # 5th index for sampleList3
    # Humidity
    h1 = 70                                         # 6th index for sampleList1
    h2 = 65                                         # 6th index for sampleList2
    h3 = 60                                         # 6th index for sampleList2
    '''
    These are the sample lists that would be provided
    '''
    # sampleList1 uses all the values that include 1 in their name
    sampleList1 = [a1, b1, c1, d1, e1, f1, g1, h1]
    # sampleList2 uses all the values that include 2 in their name
    sampleList2 = [a2, b2, c2, d2, e2, f2, g2, h2]
    # sampleList3 uses all the values that include 3 in their name
    sampleList3 = [a3, b3, c3, d3, e3, f3, g3, h3]

    '''
    These are the sample outdoor activity information that would be provided
    '''
    # Dictionary 1
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
    # Dictionary 2
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
    # Dictionary 3
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
    # Form the list containing each activity represented as a dictionary
    dictList = [dict1, dict2, dict3]

    # Run the pop-up function; change the sampleList to test a different set
    createPopup("Sample Title", sampleList3, viewImperial, dictList)


