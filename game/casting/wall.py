import constants
from game.casting.actor import Actor
from game.shared.point import Point


class Wall(Actor):
    """
    A wall that serves as an obstacle to tanks and missiles.
    
    The responsibility of Wall is to serve as an obstacle.

    Attributes:
        _points (int): The number of points the item is worth.
    """
    def __init__(self, image, position = False, text = "O", color = constants.WALL_COLOR):
        "Constructs a new Item."
        super().__init__()
        self._points = 0
        if not position:
            position = Point(0,0)
        self.set_image(image)
        self.set_position(position)
        self.set_text(text)
        self.set_color(color)
        
    def get_points(self):
        """Gets the points the item is worth.
        
        Returns:
            points (int): The points the item is worth.
        """
        return self._points