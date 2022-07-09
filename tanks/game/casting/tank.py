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
        self._text = constants.TANK_SHAPE
        x = int(constants.CELL_SIZE * constants.PLAYER_START[self._player_number].get_x())
        y = int(constants.CELL_SIZE * constants.PLAYER_START[self._player_number].get_y())
        self._position = Point(x, y)
        self._recoil = constants.TANK_RECOIL_RATE
        self._reload_gun()
        self._facing = Point(0, -1) # Set the initial facing direction to UP.


    def _reload_gun(self):
        """Reloads the player's gun with ammunition and resets the reload timer.
        """
        self._num_rounds = constants.TANK_AMMO_ROUNDS
        self._reload_time = 2 * (constants.FRAME_RATE)


    def set_facing(self, velocity):
        """Sets the _facing attribute to point the Tank in different directions. The velocity data is
        reduced to a simple pair of X,Y velocities represented by -1, 0, or 1 to identify facing 
        direction, e.g. (-1, 0) would be facing left, (1, 1) would be facing diagonal down right.
        
        Args:
            velocity (Point): defines a facing direction based on the last direction moved.
        """
        
        new_x = velocity.get_x() 
        new_y = velocity.get_y()
        
        if new_x != 0:
            new_x = new_x / abs(new_x)
        if new_y != 0:
            new_y = new_y / abs(new_y)

        self._facing = Point(new_x, new_y)


    def move_next(self):
        """Performs all of the move_next actions of the parent, plus updating the gun status
        and gun timers as needed.
        """
        super().move_next()
        if self._recoil < constants.TANK_RECOIL_RATE:
            self._recoil += 1
        if self._num_rounds < 1:

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
        if self._num_rounds > 0 and self._recoil == constants.TANK_RECOIL_RATE:
            velocity = self._facing.scale(constants.MISSILE_SPEED * constants.CELL_SIZE)
            missile = Missile(self._player_number, self._position, velocity, self._color)
            cast.add_actor(f"missiles{self._player_number}", missile)
            self._num_rounds -= 1
            self._recoil = 0
            # print(f"Rounds left for player {self._player_number}: {self._num_rounds}")
            # print(f"Missile fired by player {self._player_number}")
            # print(f"    FROM: {self._position.get_x()},{self._position.get_y()}")
            # print(f"     DIR: {velocity.get_x()},{velocity.get_y()}")





            
    
        
        
           
           
           
        
        

        