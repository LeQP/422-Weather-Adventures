# 422-Weather Adventures

# Description
This system is intended to assist in the planning and execution of outdoor recreation activities in the Oregon area. Upon application startup, a map is displayed with several overlay options. The map can show wind direction or weather status symbols. Multiple view zoom levels can be selected: Eugene, Lane County, and Oregon state. The user can click a map grid square to bring up a secondary window with additional information. This information includes detailed weather description and recommended outdoor activities based on weather status and distance from the selected grid square. 

# Authors
Joey Le, Peter Nelson, Melodie Collins, Angela Pelky, Alexa Roskowski

# Date Created
3/9/23

# Modified
3/10/23

# Project Motivation
The community of Oregon outdoor activity enthusiasts will benefit from the use of this system. Our system's creation was motivated by a lack of cohesion in outdoor information services. In the state of the application space, there was no single service that delivered both weather data and outdoor activiy guides. As a solution, our system uses up-to-date weather information to generate lists of activities suitable for the current conditions. The user no longer needs to cross-reference weather data and guides from different sources.

# How to compile and run the application
1. Download and extract the file directory. Will create a folder in your working directory called 422-Weather-Adventures.
2. Create a terminal session in the working directory (Powershell/CMD on Windows, Terminal on Mac/Linux).
3. Download and install dependencies with "pip" command (list of dependencies below)
4. To run the program, type “python3 weather_adventures.py”.

# Dependencies
1. Python Libraries: Tkinter, Pillow, Requests, OS, JSON, WebBrowser
2. API: openweathermap

# Directory Structure
1. All program files contained in "422-Weather-Adventures" 
2. "422-Weather-Adventures" subdirectory "images" contains all required source image files 
3. "images" subdirectory "mapImages" contains all map image files 
4. "images" subdirectory "weatherSymbols" contains all weather symbol image files

