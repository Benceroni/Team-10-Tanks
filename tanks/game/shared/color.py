class Color:
    """A color.

    The responsibility of Color is to hold and provide information about itself. Color has a few 
    convenience methods for comparing them and converting to a tuple.

    Attributes:
        _red (int): The red value.
        _green (int): The green value.
        _blue (int): The blue value.
        _alpha (int): The alpha or opacity.
    """
    
    def __init__(self, red, green, blue, alpha = 255):
        """Constructs a new Color using the specified red, green, blue and alpha values. The alpha 
        value is the color's opacity.
        
        Args:
            red (int): A red value.
            green (int): A green value.
            blue (int): A blue value.
            alpha (int): An alpha or opacity.
        """
        self._red = red
        self._green = green
        self._blue = blue 
        self._alpha = alpha

    def to_tuple(self):
        """Gets the color as a tuple of four values (red, green, blue, alpha).

        Returns:
            Tuple(int, int, int, int): The color as a tuple.
        """
        return (self._red, self._green, self._blue, self._alpha)   


    def set_alpha(self, value):
        """Allows the alpha channel to be adjusted as needed.
        
        Args:
            value (int): A number between 0 and 255 to change opacity.
        """
        self._alpha = value


    def copy(self, alpha = -1):
        """Returns a new copy of itself, optionally with a different alpha.
        
        Args:
            alpha (int): A number between 0 and 255 to set a new opacity. If out of bounds,
                         use existing alpha in new copy.
        
        Returns: (Color) object.
        """
        if alpha < 0 or alpha > 255:
            alpha = self._alpha

        new_color = Color(self._red, self._green, self._blue, alpha)
        return new_color