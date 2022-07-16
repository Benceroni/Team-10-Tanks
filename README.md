# Tanks
_I aimed my pebble, but myself_  
_Was all the one that fell._  
_Was it Goliath was too large,_  
_Or only I too small?_  

~ From "The Duel" by Emily Dickenson 

## Overview
Tanks is a game where two players attempt to annihilate each other by shooting exploding shells.

## Rules
Tank is played according to the following rules:

### Keyboard Commands
Players can control their tanks with the following keyboard commands:

| Command | Player 1  | Player 2 |
| :---    |   :---:   |   :---:  |
| Up      |     **W**     |     **I**    |
| Down    |     **S**     |     **K**    |
| Left    |     **A**     |     **J**    |
| Right   |     **D**     |     **L**    |
| Fire    | **Left-Alt**, or **Left-Ctrl** | **Right-Alt**, or **Right-Ctrl** |

Some maps have open borders. Going off the edge of the screen will wrap around to the opposite side.

### Health
Each player has 100 health points. This status is indicated at the bottom of the screen. When a player runs out of health points, their tank goes ***KA-BLOOEY!*** and he or she loses the game.

### Shooting
Each player's tank has a cannon that will shoot five rounds at a time. After five rounds have been fired, the tank will need to reload and the player is unable to shoot. This is indicated when the tank goes dark. The reload process takes only a couple of seconds. The tank is ready to shoot when it lights up again.

The cannon can shoot a fairly decent range. Rounds will explode on contact with the other tank, any barriers, or the ground when they have reached their range limit. Explosions will hurt, even if it is not a direct hit. 

## Getting Started
Make sure you have Python 3.8.0 or newer installed and running on your machine. Open a terminal and browse to the project's root folder. Start the program by running the following command.

`python3 tanks` or `py tanks`

You will be prompted in the console or terminal which map you would like to play. After selecting a map, the game window will open and the game will commence.

You can also run the program from an IDE like Visual Studio Code. Start your IDE and open the project folder. Select the main module inside the `tanks` folder and click the **Run** button.

## Project Structure
The project files and folders are organized as follows:
```
root                    (project root folder)
+-- tanks               (source code for game)
  +-- assets            (image assets for the game)
  +-- game              (specific classes)
    +-- casting         (classes who are used to make the interactable objects in the game)
    +-- directing       (classes who direct the sequence of actions in the play)
    +-- scripting       (classes who manage the specific actions used in the game)
    +-- services        (classes that provide input and output from monitor and keyboard)
    +-- shared          (classes who are used to manage attributes in other classes)
  +-- __main__.py       (program entry point)
+-- README.md           (this file, general info)
```

## Required Technologies
Python 3.8.0 or greater.

## Authors
- Spencer Bell (bel21032@byui.edu)
- Dallas Eaton (deaton879@byui.edu)
- David Kikiani (davidkikiani@mail.com)
- Julian Hernandez (hernandezjuliang44@gmail.com)
- Mike Lewis (wyoming.c64@gmail.com)
- Jaden McCarrey (jadenmccarrey@gmail.com)

Pixel art by Julian Hernandez.
