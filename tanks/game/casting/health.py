import constants
from game.casting.actor import Actor
from game.shared.point import Point

class Health(Actor):
    """
    A record of current health points.
    
    The responsibility of Health is to keep track of health points.
    
    Attributes:
        health_points (int): The number of health points remaining.    
    """

    def __init__(self, player_number=0):
        """Creates a new instance of Health. 
        
        Args:
            player_number: (Int) - A number referring to which player this will belong.
        """
        super().__init__()
        self._player_number = player_number
        self.set_color(constants.PLAYER_COLORS[player_number]['ready'])
        x = int(constants.CELL_SIZE * constants.HEALTH_POINT_POSITION[self._player_number-1].get_x())
        y = int(constants.CELL_SIZE * constants.HEALTH_POINT_POSITION[self._player_number-1].get_y())
        updated_position = Point(x, y)
        self.set_position(updated_position)
        self.health_points = 100
        self.set_text(f"  Health Points: {self.health_points}  ")

    def apply_damage(self, damage_points):
        """Subtracts damage_points from self.health_points.
        
        Args:
            damage_points (int): The amount of health points to subtract from self.health_points.
        """
        self.health_points -= damage_points
        self.set_text(f"  Health Points: {self.health_points}  ")


    def get_health_points(self):
        """Gets the actor's health points.
        
        Returns:
            Int: The actor's current number of health points.
        """
        return self.health_points


    def get_player_num(self):
        """Returns the value of the player_number attribute.
        """
        return self._player_number


    # Shouldn't move next... Should be static.

    def move_next(self):
        """Do nothing.
        """
        pass

    # def get_text_length(self):
    #     """Determines how long the instance of Health is.

    #     Returns:
    #         Int: The length of the instance of Health measured by characters.
    #     """
    #     return len(self._text)
