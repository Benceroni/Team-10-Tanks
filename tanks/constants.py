from game.shared.color import Color
from game.shared.point import Point

COLUMNS = 60
ROWS = 40
CELL_SIZE = 16
MAX_X = 900
MAX_Y = 600
FRAME_RATE = 16
FONT_SIZE = 16
CAPTION = "Tanks"


# Textual bullet shapes are defined for two directions:
#   0: left/right
#   1: up/down
# and consist of a series of three shapes: 
#   0: head
#   1: mid
#   2: tail
MISSILE_SHAPES = [
    ["*", chr(164), "-"],
    ["*", chr(164), "|"],
]
MISSILE_SPEED = 0.5
MISSILE_RANGE = 50

TANK_SHAPE = chr(169) # Copyright symbol (C)
TANK_LENGTH = 1
TANK_SPEED = 0.25

PLAYER_START = [
    Point(30, 20),
    Point(15, 10),
    Point(45, 30)
]

# Colors
WHITE = Color(255, 255, 255)
RED = Color(255, 0, 0)
YELLOW = Color(255, 255, 0)
GREEN = Color(0, 255, 0)
GREY_80PCT = Color(100, 100, 100, 200) 
RED_80PCT = Color(128, 0, 0, 200)
GREEN_80PCT = Color(0, 128, 0, 200)
