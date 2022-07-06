import constants
from game.casting.actor import Actor
from game.shared.point import Point


class Tank(Actor):
    """
    An old-school tank that leaves a solid beam of light as it's trail.
    
    The responsibility of tank is to move itself.

    Attributes:
        _player_number (int): Identifies which player the tank instance belongs to.
        _bullets (list[Actor]): The list of Actors representing bullets fired at the other player.
        _color (Color): The color that the light wall should be rendered.
        _wall_active (bool): Whether or not new wall segments are being drawn from this tank.
    
        All other attributes inherited from Actor.
    """
    def __init__(self, color, player_number=0):
        super().__init__()
        self._bullets = []
        self._player_number = player_number
        self._color = color
        # self._wall_active = True
        self._text = constants.TANK_SHAPE
        x = int(constants.CELL_SIZE * constants.PLAYER_START[self._player_number].get_x())
        y = int(constants.CELL_SIZE * constants.PLAYER_START[self._player_number].get_y())
        self._position = Point(x, y)


    def move_next(self):
        """Moves the actor to its next position according to its velocity. Will wrap the position 
        from one side of the screen to the other when it reaches the given maximum x and y values.

        Args:
            max_x (int): The maximum x value.
            max_y (int): The maximum y value.
        """
        x = (self._position.get_x() + self._velocity.get_x()) % constants.MAX_X
        y = (self._position.get_y() + self._velocity.get_y()) % constants.MAX_Y
        self._position = Point(x, y)


            
    
        
        
           
           
           
        
        

        