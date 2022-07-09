import random
import constants
from game.casting.actor import Actor
from game.shared.point import Point


class Item(Actor):
    """
    A item that the tanks can potentially pick up.
    
    The responsibility of Item is to select a random position and points that it's worth.

    Attributes:
        _points (int): The number of points the item is worth.
    """
    def __init__(self, position = False, text = "O", color = constants.GREY):
        "Constructs a new Item."
        super().__init__()
        self._points = 0
        if not position:
            position = Point(0,0)
        self.set_position(position)
        self.set_text(text)
        self.set_color(color)
        # self.reset()
        
    def reset(self):
        """Selects a random position and points that the item is worth."""
        # self._points = random.randint(1, 8)
        # x = random.randint(1, constants.COLUMNS - 1)
        # y = random.randint(1, constants.ROWS - 1)
        # position = Point(x, y)
        # position = position.scale(constants.CELL_SIZE)
        # self.set_position(position)
        pass
        
    def get_points(self):
        """Gets the points the item is worth.
        
        Returns:
            points (int): The points the item is worth.
        """
        return self._points