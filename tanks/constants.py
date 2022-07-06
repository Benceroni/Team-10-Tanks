from game.shared.color import Color
from game.shared.point import Point

COLUMNS = 60
ROWS = 40
CELL_SIZE = 15
MAX_X = 900
MAX_Y = 600
FRAME_RATE = 15
FONT_SIZE = 15
CAPTION = "Tanks"
# TAIL_SHAPES = [" ","/","\\"]

# Textual bullet shapes are defined for two directions:
#   0: left/right
#   1: up/down
# and consist of a series of three shapes: 
#   0: head
#   1: mid
#   2: tail
BULLET_SHAPES = [
    ["*", chr(164), "-"],
    ["*", chr(164), "|"],
]
TANK_SHAPE = chr(169) # Copyright symbol (C)
TANK_LENGTH = 2
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
