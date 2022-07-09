import constants
from game.casting.actor import Actor
from game.shared.point import Point



class Missile(Actor):
    """Attributes: 
            _player (int): identifies which player it belongs to.
            _range (int): Maximum distance traveled. 
            _phase (int): The phase level for this missile which determines if this missile explodes or not. 
                            If set to 0 then there will be no further explosions. (1 should be enough.)
    """
    # Construct a missile with an initial position and velocity
    def __init__(self, player, position, velocity, color):
        """Constructs a missile with an initial position and velocity.
        
        Args:
            position: (Point) a given X, Y location on the game board.
            vector: (Point) a given Vx, Vy velocity that defines the direction and speed.
            
        """
        super().__init__()
        self._phase = 1
        self.set_text("*")
        self.set_position(position)
        self.set_velocity(velocity)
        self.set_color(color)
        self._player = player
        self.set_range(constants.MISSILE_RANGE)


    def set_phase(self, level):
        """Sets the phase level for this missile, usually from a previous missile that exploded.
        
        Args:
            level (int): The level to set the phase value to. (Usually something less than 
                            the previous missile that spawned this one.)
        """
        self._phase = level


    def get_player_num(self):
        return self._player


    def get_range(self):
        return self._range


    def set_range(self, range_value):
        """Sets the range of this missile.
        
        Args:
            range_value (int): The range is actually the number of frame draws that 
                the missile will be alive for. Once the counter reaches zero, the 
                missile should be destroyed.
        """
        self._range = range_value



    def move_next(self):
        super().move_next()
        # print(f"Range to live: {self._range}")
        self._range -= 1
        


    def explode(self, cast):
        """Explodes this missile by spawning several new short-range missiles, but only if this
        missile is in the right phase to do so.
        
        Args:
            cast (Cast): The cast of actors.
        """
        if self._phase > 0:
            for vector in constants.MISSILE_EXPLOSION_VELOCITIES:
                self.set_velocity(Point(0,0))
                flak = Missile(self._player, self._position, vector, constants.YELLOW)
                flak.set_range(5)
                flak.set_phase(self._phase - 1)
                cast.add_actor(f"missiles{self._player}", flak)
                # Can I do this?
                
            # cast.remove_actor(f"missiles{self._player}", self)



    ## For now all other methods inherited from Actor remain the same.



    