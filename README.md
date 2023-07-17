# To run in your local machine

create a virtual environment inside the folder

```bash
python3 -m venv venv
```

Activate the virtual environment

```bash
    source venv/bin/activate
```

Install requirements

```bash
    pip3 install -r requirements.txt
```

create a file env.py with:

```bash
import os
os.environ['SECRET_KEY'] = "Key"
os.environ['CLOUDINARY_KEY'] = "AdH_AuJkA7GU0CfjrrilM_Q2E6c"
os.environ['DEVELOPMENT'] = "0"

```

Run the server

```bash
    python3 manage.py runserver
```

The project is deployed and can be accessed at [link](https://suns-goods-1564630265ef.herokuapp.com/).

# Your Outdoors
Mock-up img

Live Website 

-------------------------------------------------------------------------

## Introduction

Your Outdoors is an interactive location based game designed to encourage people to go outdoors and explore their local area. It offers the user challenges in the form of a photograph, displaying a distinctive landmark or feature in their area. To complete the challenge they have to locate the feature and identify the spot the photograph was taken from. Users are awarded points when they complete challenges and can compare their progress with other users.

It's easy to explore the world through photographs on our phone without experiencing the places we're looking at first hand. This means we don't get the benefits provided by being in green/blue spaces, from the physical activity of walking, and vitamin D from being out on summer days. With Your Outdoors, you can find beautiful and interesting places in your neighbourhood with the added motivation of upping your position on the leaderboard, helping to motivate users to enjoy what they see in photographs in person. 

## User Stories

1. As a user, I want to explore different locations and discover landmarks and features in the images to engage in an interactive and enjoyable game experience.
2. As a user, I want to earn points and track my progress as I successfully find items and complete challenges, giving me a sense of achievement and competitiveness.
3. As a user, I want to be challenged with various tasks like taking photos or answering quiz questions related to the location, enhancing my knowledge and engagement with the surroundings.
4. As a user, I want to check in using my mobile device to validate my findings and showcase my accomplishments within the game.
5. As a user, I want to see a leaderboard that displays the top scores of other players, motivating me to improve my performance and compete with others.

## Features

### Landing Page

image

The first page seen on loading the application. The landing page introduces the game with a tag-line and gives the user options to help them navigate and understand the game.
- Play - takes the user to the 'locations' page which allows them to select an area for their challenges to be based around.
- Rules - takes the user to the 'rules' page and explains how to play.
- Leaderboard - takes the user to the 'leaderboard' page and allows the user to compare their progress with other users.

### Navbar
Appears on all pages other than landing page.
- hamburger menu
	- Help
	- Register
	- Login
	- Leaderboard
- Game brand
	- Provides a link to return to the landing page.

### Play
#### Location
- The location page allows the user to select a city in which they'd like to take on challenges. 
- Contains option to go 'back' to previous page.
#### Challenge
- When a location is chosen the user is given a challenge in the form of a photograph.
- They are then given options:
	- 'Take the Quiz' - Navigates user to a page which offers questions 
	- 'Found it!' - allows them to use the browser location function to show they have completed the challenge.
	- 'Skip' - allows the user to skip onto a new challenge but this deducts a point from their score.
	- 'Back' - to return to previous 

### Rules
- Step-by-step details of how to play the game.
-  Contains option to go 'back' to previous page.


### Leaderboard
- Lists scores of other players in descending order.


#### Future Features
- Users can upload challenges as well as complete them.
- The challenge is timed for the opportunity to gain more points.
- User can choose the difficulty of a challenge; points correlate.
- A location 'search' function.
- 'All time' leader board which shows total cumulative points without the daily reset. 

## Figma Prototypes



## Tech
In the tech section, we provide information about the technology stack, dependencies, and any technical details related to the project.

## Languages 

- HTML
- CSS
- JavaScript
- Python
- Django

## Credits

## Image Credits