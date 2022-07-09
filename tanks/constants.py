from game.shared.color import Color
from game.shared.point import Point

COLUMNS = 60
ROWS = 40
CELL_SIZE = 20
WALL_BUFFER = 1
WALL_BUBBLE = CELL_SIZE + WALL_BUFFER
MAX_X = CELL_SIZE * COLUMNS
MAX_Y = CELL_SIZE * ROWS
FRAME_RATE = 30  # May need to go higher since we are processing more....
FONT_SIZE = 20
CAPTION = "Tanks"

# Textual bullet shapes are defined for two directions:
#   0: left/right
#   1: up/down
# and consist of a series of three shapes: 
#   0: head
#   1: mid
#   2: tail
MISSILE_SHAPES = [
    ["*", chr(164), "X"],
]
MISSILE_SPEED = 0.5
MISSILE_RANGE = 40
MISSILE_EXPLOSION_POWER = 2
MISSILE_EXPLOSION_VECTORS = [
    [ 0.00, -2.00], # N
   # [ 0.75, -1.75], # NNE
    [ 2.00, -2.00], # NE
   # [ 1.75, -0.75], # ENE
    [ 2.00,  0.00], # E
   # [ 1.75,  0.75], # ESE
    [ 2.00,  2.00], # SE
   # [ 0.75,  1.75], # SSE
    [ 0.00,  2.00], # S
   # [-0.75,  1.75], # SSW
    [-2.00,  2.00], # SW
   # [-1.75,  0.75], # WSW
    [-2.00,  0.00], # W
   # [-1.75, -0.75], # WNW
    [-2.00, -2.00], # NW
   # [-0.75, -1.75]  # NNW
]
MISSILE_EXPLOSION_VELOCITIES = []
for vect in MISSILE_EXPLOSION_VECTORS:
    v_x = round(vect[0] * CELL_SIZE / 2)
    v_y = round(vect[1] * CELL_SIZE / 2)
    MISSILE_EXPLOSION_VELOCITIES.append(Point(v_x, v_y))

TANK_SHAPE = chr(169) # Copyright symbol (C)
TANK_LENGTH = 1
TANK_SPEED = 0.25
TANK_AMMO_ROUNDS = 4
TANK_RECOIL_RATE = 5
TANK_BUFFER = -10
TANK_BUBBLE = CELL_SIZE + TANK_BUFFER

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
GREY = Color(128, 128, 128)
GREY_80PCT = Color(100, 100, 100, 200) 

RED_80PCT = Color(128, 0, 0, 200)
GREEN_80PCT = Color(0, 128, 0, 200)
