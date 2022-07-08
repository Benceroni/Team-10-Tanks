import constants
from game.casting.missile import Missile
from game.casting.actor import Actor
from game.shared.point import Point


class Tank(Actor):
    """
    An old-school tank that leaves a solid beam of light as it's trail.
    
    The responsibility of tank is to move itself.

    Attributes:
        _player_number (int): Identifies which player the tank instance belongs to.
        _num_rounds (int): The number of active missiles on the screen from this player.
        _color (Color): The color that the light wall should be rendered.
        _wall_active (bool): Whether or not new wall segments are being drawn from this tank.
        _facing (Point): Is really the last velocity that the tank moved that is not (0,0) which defines which
                         direction it is facing.
    
        All other attributes and methods inherited from Actor.
    """
    def __init__(self, color, player_number=0):
        super().__init__()
        self._player_number = player_number
        self._color = color
        # self._wall_active = True
        self._text = constants.TANK_SHAPE
        x = int(constants.CELL_SIZE * constants.PLAYER_START[self._player_number].get_x())
        y = int(constants.CELL_SIZE * constants.PLAYER_START[self._player_number].get_y())
        self._position = Point(x, y)
        self._reload_gun()
        self._facing = Point(0, -1 * constants.CELL_SIZE) # Set the initial facing direction to UP.


    def _reload_gun(self):
        self._num_rounds = 6
        self._reload_time = 2 * (constants.FRAME_RATE)


    def set_facing(self, velocity):
        """Sets the _facing attribute to point the Tank in different directions.
        
        Args:
            velocity (Point): defines a facing direction based on the last direction moved.
        """
        self._facing = velocity


    def move_next(self):
        super().move_next()
        if self._num_rounds < 1:
            print(f"Time to reload player {self._player_number}: {self._reload_time} ticks.")
            self._reload_time -= 1
            if self._reload_time == 0:
                self._reload_gun()
   
        


    def fire_missile(self, cast):
        """Creates a missile actor (fires a missile or projectile) and sets its velocity. The 
        starting position is the same as the tank's position.
        
        Args:
            cast (Cast): A list of Actors in acting groups that we will add the missile to. 
            velocity (Point): The initial Vx, Vy velocity of the missile. 
        """
        if self._num_rounds > 0:
            velocity = self._facing
            missile = Missile(self._player_number, self._position, velocity, self._color)
            cast.add_actor("missiles", missile)
            self._num_rounds -= 1
            print(f"Rounds left for player {self._player_number}: {self._num_rounds}")
            # print(f"Missile fired by player {self._player_number}")
            # print(f"    FROM: {self._position.get_x()},{self._position.get_y()}")
            # print(f"     DIR: {velocity.get_x()},{velocity.get_y()}")





            
    
        
        
           
           
           
        
        

        