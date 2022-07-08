import constants
from game.casting.actor import Actor
from game.shared.point import Point

class Missile(Actor):
    """Attributes: 
            _player (int): identifies which player it belongs to.
            _range (int): Maximum distance traveled. 
    """
    # Construct a missile with an initial position and velocity
    def __init__(self, player, position, velocity, color):
        """Constructs a missile with an initial position and velocity.
        
        Args:
            position: (Point) a given X, Y location on the game board.
            vector: (Point) a given Vx, Vy velocity that defines the direction and speed.
            
        """
        super().__init__()
        self.set_text("*")
        self.set_position(position)
        self.set_velocity(velocity)
        self.set_color(color)
        self._player = player
        self._range = 30


    def get_range(self):
        return self._range


    def move_next(self):
        super().move_next()
        # print(f"Range to live: {self._range}")
        self._range -= 1

    ## For now all other methods inherited from Actor remain the same.



    