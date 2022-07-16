import pyray
from constants import *
from game.shared.point import Point

class Image:
    """An image."""
    
    def __init__(self, filename, scale = 1, rotation = 0):
        """Constructs a new Image."""
        self._filename = filename
        self._scale = scale
        self._rotation = rotation
        self._position = Point(0, 0)
        self._tint = pyray.WHITE
        
    def get_filename(self):
        """Gets the name of the image file.
        
        Returns:
            A string containing the name of the image file.
        """
        return self._filename

    def get_rotation(self):
        """Gets the degrees the image should be rotation.

        Returns:
            A float representhing the degrees the image should be rotated.
        """
        return self._rotation

    def get_scale(self):
        """Gets the scaling factor for the image.

        Returns:
            A float representhing the scaling factor for the image.
        """
        return self._scale

    def get_position(self):
        """Gets the position factor for the image.

        Returns:
            A point representing the position of the image
        """ 
        return self._position

    def set_rotation(self, rotation):
        """Sets the image's rotation to the given value.

        Args:
            rotation: A float representing the degree of rotation (clockwise).
        """
        self._rotation = rotation

    def set_scale(self, scale):
        """Sets the image's scale to the given value.

        Args:
            scale: A float representing how much the image should be scaled.
        """
        self._scale = scale

    def set_position(self, position):
        """Sets the image's position to the given value.

        Args:
            position: A point representing the position of the image.
        """
        self._position = position

        #Up
        if self._rotation == 0:
            pass
        
        #Up-Right
        elif self._rotation == 45:
            self._position = self._position.add(Point(CELL_SIZE * self._scale * 0.6, -CELL_SIZE * self._scale / 4))

        #Right
        elif self._rotation == 90:
            self._position = self._position.add(Point(CELL_SIZE * self._scale, 0))

        #Down-Right
        elif self._rotation == 135:
            self._position = self._position.add(Point(CELL_SIZE * self._scale / 0.75, CELL_SIZE * self._scale * 0.6))

        #Down
        elif self._rotation == 180:
            self._position = self._position.add(Point(CELL_SIZE * self._scale, CELL_SIZE * self._scale))

        #Down-Left
        elif self._rotation == 225:
            self._position = self._position.add(Point(CELL_SIZE * self._scale * 0.4, CELL_SIZE * self._scale / 0.8))

        #Left
        elif self._rotation == 270:
            self._position = self._position.add(Point(0, CELL_SIZE * self._scale))

        #Up-Left
        elif self._rotation == 315:
            self._position = self._position.add(Point(-CELL_SIZE * self._scale * 0.25, CELL_SIZE * self._scale * 0.4))

    
    
    def set_tint(self, color):
            """Sets the tinting color for the image when drawn.
            
            Args:
                color (Color): A valid color instance.
            """
            self._tint = color

    
    def get_tint(self):
            """Returns the current tint color for the image.
            """
            return self._tint
            
