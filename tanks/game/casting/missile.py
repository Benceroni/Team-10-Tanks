import constants
import random
from game.casting.actor import Actor
from game.shared.point import Point


class Missile(Actor):
    """A missile is anything that is propelled in a certain direction for a certain distance or amount
    of time. Common use of a Missile is to be bullets or other projectiles hurled at the other player. 
    This also left the option open to make explosions, which would be a collection of several missile
    objects (e.g. shrapnel) 
    
    Attributes: 
        _player (int):  identifies which player it belongs to.
        _range (int):   Maximum distance traveled. 
        _phase (int):   The phase level for this missile which determines if this missile explodes or not. 
                        If set to 0 then there will be no further explosions. (1 should be enough.)
    """
    
    def __init__(self, player, position, velocity, color):
        """Constructs a missile with an initial position (usually the same position as the thing that
        fired the missile) and velocity.
        
        Args:
            position (Point):   a given X, Y location on the game board.
            vector (Point):     a given Vx, Vy velocity that defines the direction and speed.
            color (Color):      an (initial) color for the missile itself.
        """
        super().__init__()
        self._phase = 1
        self.set_text(constants.MISSILE_SHAPES[1])
        self.set_position(position)
        self.set_velocity(velocity)
        self.set_color(color)
        self._player_num = player
        self.set_range(constants.MISSILE_RANGE)


    def set_phase(self, level):
        """Sets the phase level for this missile, usually from a previous missile that exploded.
        
        Args:
            level (int): The level to set the phase value to. (Usually something less than 
                            the previous missile that spawned this one.)
        """
        self._phase = level


    def get_player_num(self):
        """Returns the player number assigned to this missile.
        
        Returns: (Int) _player_num - The number of the player who fired this missile.
        """
        return self._player_num


    def get_range(self):
        """Returns the remaining range left for this missile.

        Returns: (Int) _range - The remaining range value of this missile.
        """
        return self._range


    def set_range(self, range_value):
        """Sets the range of this missile.
        
        Args:
            range_value (int): The range is actually the number of frames drawn that 
                the missile will be alive for. Once the counter reaches zero, the 
                missile should be destroyed.
        """
        self._range = range_value


    def _set_random_text(self):
        """Changes the image of the shrapnel to a random character from a
        predefined list.

        Args: 
            None - The text character is generated randomly.
        """
        max = len(constants.MISSILE_EXPLOSION_SHAPES)-1
        new_text = constants.MISSILE_EXPLOSION_SHAPES[random.randint(0,max)]
        self.set_text(new_text)


    def move_next(self):
        """Does normal Actor move_next() activities, and also decrements the range
        remaining for this missile. 
        """
        super().move_next()
        self._range -= 1
        if self._phase < 1:
            self._set_random_text()
        


    def explode(self, cast):
        """Explodes this missile by spawning several new short-range missiles as shrapnel, 
        but only if this missile is in the right phase to do so. (This method leaves the option
        open to create various multi-phased missiles like MIRV weapons. The phase of the missile
        could be used as an index to different blast trajectory patterns.) 
        
        Args:
            cast (Cast): The cast of actors within which the new missiles will be spawned.
        """
        if self._phase > 0:
            for vector in constants.MISSILE_EXPLOSION_VELOCITIES:
                self.set_velocity(Point(0,0))
                shrapnel = Missile(self._player_num, self._position, vector, constants.YELLOW)
                shrapnel.set_range(constants.MISSILE_BLAST_RANGE)
                shrapnel.set_phase(self._phase - 1)
                cast.add_actor(f"missiles{self._player_num}", shrapnel)

    ## For now all other methods inherited from Actor remain the same.   