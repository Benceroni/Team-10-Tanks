import os
import random
from game.shared.color import Color
from game.shared.point import Point

########## COLORS #########
#
WHITE =         Color(255, 255, 255)
RED =           Color(255, 0, 0)
YELLOW =        Color(255, 255, 0)
ORANGE =        Color(255, 180, 0)
GREEN =         Color(0, 255, 0)
CYAN =          Color(0, 255, 255)
BLUE =          Color(100, 100, 255)
MAGENTA =       Color(255, 0, 255)

DK_RED =        Color(140, 0 ,0)
DK_ORANGE =     Color(140, 80, 0)
DK_GREEN =      Color(0, 140, 0)
DK_CYAN =       Color(0, 140, 140)
DK_BLUE =       Color(60, 60, 140)
DK_MAGENTA =    Color(140, 0, 140)

GREY =          Color(140, 140, 140)
DK_GREY =       Color(80, 80, 80)



########## SCREEN / BOARD / VIDEO DEFINITIONS ##########
#
# Size of a cell in pixels.
CELL_SIZE = 16
FONT_SIZE = CELL_SIZE

# Number of cells across.
COLUMNS = 60

# number of cells tall.
ROWS = 40

# Overall size of window in pixels (calculated).
MAX_X = CELL_SIZE * COLUMNS
MAX_Y = CELL_SIZE * ROWS

# Game speed / redraw frame rate. (Target, not guaranteed.) 
FRAME_RATE = 30 

# Window title
CAPTION = "Tanks"

#Directory
ABSOLUTE_PATH = os.path.dirname(__file__)
DIRECTORY = os.path.join(ABSOLUTE_PATH, "assets")
BACKGROUND_KEY = "1"
BACKGROUND = {
    "1": (os.path.join(ABSOLUTE_PATH, "assets/grass.png")),
    "2": (os.path.join(ABSOLUTE_PATH, "assets/sand.png")),
    "3": (os.path.join(ABSOLUTE_PATH, "assets/futuristic.png"))
    }

# Health point positions.
HEALTH_POINT_POSITION = [
    Point(1, 0),
    Point(50, 0)
]


########## WALL DEFINITIONS ##########
#
# Buffer size of a wall object in pixels.
WALL_BUFFER = -1

# Calculated overall wall object boundary.
WALL_BUBBLE = CELL_SIZE + WALL_BUFFER

# Wall color(s).
WALL_COLOR = GREY

#Wall Image(s).
WALL_IMAGES = {
    "square": (os.path.join(ABSOLUTE_PATH, "assets/wall_segment_01.png"))
}



########## MISSILE DEFINITIONS ##########
#
# Missile shapes used for flying missile animation
MISSILE_SHAPES = ["*", chr(164), "X"]

# MISSILE SPEED measured as percentage of cell size.
MISSILE_SPEED = 0.5

# Missile range is number of frame steps a missile will travel before exploding.
MISSILE_RANGE = 50

# Explosion factor adjusts the following vector table to fine tune overall speed
# of explosion shrapnel.
MISSILE_EXPLOSION_SCALE = 3

# Vectors that define starting vectors for explosion shrapnel.
MISSILE_EXPLOSION_VECTORS = [
    [ 0.00, -2.00], # N
    [ 0.75, -1.75], # NNE
    [ 2.00, -2.00], # NE
    [ 1.75, -0.75], # ENE
    [ 2.00,  0.00], # E
    [ 1.75,  0.75], # ESE
    [ 2.00,  2.00], # SE
    [ 0.75,  1.75], # SSE
    [ 0.00,  2.00], # S
    [-0.75,  1.75], # SSW
    [-2.00,  2.00], # SW
    [-1.75,  0.75], # WSW
    [-2.00,  0.00], # W
    [-1.75, -0.75], # WNW
    [-2.00, -2.00], # NW
    [-0.75, -1.75]  # NNW
]

MISSILE_EXPLOSION_SHAPES = []
for i in range(33, 48):
    MISSILE_EXPLOSION_SHAPES.append(chr(i))
for i in range(91, 97):
    MISSILE_EXPLOSION_SHAPES.append(chr(i))
for i in range(123, 127):
    MISSILE_EXPLOSION_SHAPES.append(chr(i))
for i in range(161, 192):
    MISSILE_EXPLOSION_SHAPES.append(chr(i))
MISSILE_EXPLOSION_SHAPES.append(chr(215))
MISSILE_EXPLOSION_SHAPES.append(chr(216))
MISSILE_EXPLOSION_SHAPES.append(chr(239))
MISSILE_EXPLOSION_SHAPES.append(chr(247))
MISSILE_EXPLOSION_SHAPES.append(chr(248))
MISSILE_EXPLOSION_SHAPES.append(chr(254))

# Defines how big of a blast is created when the missile explodes.
MISSILE_BLAST_RANGE = 5

# Builds an adjusted list of velocities calculated with the explosion factor.
MISSILE_EXPLOSION_VELOCITIES = []
for vect in MISSILE_EXPLOSION_VECTORS:
    v_x = round(vect[0] * CELL_SIZE / MISSILE_EXPLOSION_SCALE)
    v_y = round(vect[1] * CELL_SIZE / MISSILE_EXPLOSION_SCALE)
    MISSILE_EXPLOSION_VELOCITIES.append(Point(v_x, v_y))



######## TANK DEFINITIONS ##########
#
# Character defining the shape of the tank for a text-drawn game.
TANK_SHAPE = chr(169) # Copyright symbol (C)

# TANK SPEED measured in percentage of cell size.
TANK_SPEED = 0.25

# Number of ammunition rounds to be fired before reload.
TANK_AMMO_ROUNDS = 5

# Number of frames between consecutive rounds.
TANK_REPEAT_RATE = 5

# Number of seconds it takes to reload a new set of rounds.
TANK_RELOAD_RATE = 3

# The buffer measuremment applied to a tank (in pixels).
TANK_BUFFER = -10

# The overall bubble boundary around a tank (in pixels).
TANK_BUBBLE = CELL_SIZE + TANK_BUFFER

# Tank images

TANK_IMAGES = [
    {
        "animation1": "",
        "animation2": ""
    },
    {
        "animation1": (os.path.join(ABSOLUTE_PATH, "assets/blue_tank_walk_01.png")),
        "animation2": (os.path.join(ABSOLUTE_PATH, "assets/blue_tank_walk_02.png"))
    },

    {
        "animation1": (os.path.join(ABSOLUTE_PATH, "assets/green_tank_walk_01.png")),
        "animation2": (os.path.join(ABSOLUTE_PATH, "assets/green_tank_walk_02.png"))
    }
]

########## PLAYER DEFINITIONS ##########
#
# Player start positions. Player 0 is not used and can be any Point value.
PLAYER_START = [
    Point(30, 20),
    Point(15, 10),
    Point(45, 30)
]

# Player Tank Colors is a list of dictionary items. The 'wait' color is 
# used when the player is out of ammo and waiting for reload.
PLAYER_COLORS = [
    {
        'wait': DK_GREY,
        'ready': GREY,
        'winner': DK_GREY
    },
    {
        'wait': DK_BLUE,
        'ready': BLUE,
        'winner': DK_BLUE,
    },
    {
        'wait': DK_GREEN,
        'ready': GREEN,
        'winner': DK_GREEN,
    }
]