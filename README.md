# cse210-05-tanks

__tank__  
_The best rides are the ones where you_  
_bite off much more than you can chew,_  
_and live through it._  
_- Doug Bradbury -_

## Overview
tank is a game where the players try to cut each other off using tanks that leave a trail behind them.

## Rules
tank is played according to the following rules.

- Players can move up, down, left and right...
    - Player one moves using the W, S, A and D keys.
    - Player two moves using the I, K, J and L keys.

- Players can press alt or ctrl on their side of the keyboard to shoot in the direction they are facing.
- Missiles will explode on walls, other tanks, or after a set distance has been reached.
- Player will lose the ability to shoot missiles for a short while after multiple shots have been fired. 
- The first tank to be shot loses.


## Getting Started
Make sure you have Python 3.8.0 or newer installed and running on your machine. Open a terminal and browse to the project's root folder. Start the program by running the following command.

python3 tank or py tank

You can also run the program from an IDE like Visual Studio Code. Start your IDE and open the project folder. Select the main module inside the dice folder and click the "run" button.

## Project Structure
The project files and folders are organized as follows:
```
root                    (project root folder)
+-- tank               (source code for game)
  +-- game              (specific classes)
    +-- casting         (classes who are used to make the interactable objects in the game)
    +-- directing       (classes who direct the sequence of actions in the play)
    +-- scripting       (classes who manage the specific actions used in the game)
    +-- services        (classes that provide input and output from monitor and keyboard)
    +-- shared          (classes who are used to manage attributes in other classes)
  +-- __main__.py       (program entry point)
+-- README.md           (general info)
```

## Required Technologies
Python 3.8.0

## Authors
- Spencer Bell (bel21032@byui.edu)
- Dallas Eaton (deaton879@byui.edu)
- David Kikiani (davidkikiani@mail.com)
- Julian Hernandez (hernandezjuliang44@gmail.com)
- Mike Lewis (wyoming.c64@gmail.com)
- Jaden McCarrey (jadenmccarrey@gmail.com)
