import pyray
import constants
import pathlib
import os
from game.shared.point import Point

class VideoService:
    """Outputs the game state. The responsibility of the class of objects is to draw the game state 
    on the screen. 
    """

    def __init__(self, debug = False):
        """Constructs a new VideoService using the specified debug mode.
        
        Args:
            debug (bool): whether or not to draw in debug mode.
        """
        self._debug = debug
        self._textures = {}

    def close_window(self):
        """Closes the window and releases all computing resources."""
        pyray.close_window()

    def clear_buffer(self, image):
        """Clears the buffer in preparation for the next rendering. This method should be called at
        the beginning of the game's output phase.
        """
        pyray.begin_drawing()
        pyray.clear_background(pyray.BLACK)
        self.draw_image(image, Point(0, 0))
        if self._debug == True:
            self._draw_grid()

    def draw_image(self, image, position):
        filepath = image.get_filename()
        filepath = str(pathlib.Path(filepath))
        texture = self._textures[filepath]
        x = position.get_x()
        y = position.get_y()
        raylib_position = pyray.Vector2(x, y)
        scale = image.get_scale()
        rotation = image.get_rotation()
        pyray.draw_texture_ex(texture, raylib_position, rotation, scale, pyray.WHITE)

    def draw_actor(self, actor, centered=False):
        """Draws the given actor's text on the screen.

        Args:
            actor (Actor): The actor to draw.
        """ 
        text = actor.get_text()
        if text == constants.MISSILE_SHAPES[1]:
            pass
        else:
            x = actor.get_position().get_x()
            y = actor.get_position().get_y()
            font_size = actor.get_font_size()
            color = actor.get_color().to_tuple()

            if centered:
                width = pyray.measure_text(text, font_size)
                offset = int(width / 2)
                x -= offset
                
            pyray.draw_text(text, x, y, font_size, color)
        
    def draw_actors(self, actors, centered=False):
        """Draws the text for the given list of actors on the screen.

        Args:
            actors (list): A list of actors to draw.
        """ 
        for actor in actors:
            self.draw_actor(actor, centered)
    
    def flush_buffer(self):
        """Copies the buffer contents to the screen. This method should be called at the end of
        the game's output phase.
        """ 
        pyray.end_drawing()

    def is_window_open(self):
        """Whether or not the window was closed by the user.

        Returns:
            bool: True if the window is closing; false if otherwise.
        """
        return not pyray.window_should_close()

    def open_window(self):
        """Opens a new window with the provided title.

        Args:
            title (string): The title of the window.
        """
        pyray.init_window(constants.MAX_X, constants.MAX_Y, constants.CAPTION)
        pyray.set_target_fps(constants.FRAME_RATE)

    def _draw_grid(self):
        """Draws a grid on the screen."""
        for y in range(0, constants.MAX_Y, constants.CELL_SIZE):
            pyray.draw_line(0, y, constants.MAX_X, y, pyray.GRAY)
            
        for x in range(0, constants.MAX_X, constants.CELL_SIZE):
            pyray.draw_line(x, 0, x, constants.MAX_Y, pyray.GRAY)


    def unload_images(self):
        for texture in self._textures.values():
            pyray.unload_texture(texture)
        self._textures.clear()

    def load_images(self, directory):
        filepaths = self._get_filepaths(directory, [".png", ".gif", ".jpg", ".jpeg", ".bmp"])
        for filepath in filepaths:
            if filepath not in self._textures.keys():
                texture = pyray.load_texture(filepath)
                self._textures[filepath] = texture

    def _get_filepaths(self, directory, filter):
        filepaths = []
        for file in os.listdir(directory):
            filename = os.path.join(directory, file)
            extension = pathlib.Path(filename).suffix.lower()
            if extension in filter:
                filename = str(pathlib.Path(filename))
                filepaths.append(filename)
        return filepaths

    def draw_missile(self, image, position, text):
        """Difirentiates missiles from explosions and draws the missiles

        Args:
            image (Image): The image to draw if the check is passed.
            position (Position): The position of the image.
            text (str): The text to check if the missile is not a explosion.
        """
        if text == constants.MISSILE_SHAPES[1]:
            self.draw_image(image, position)

    def _get_x_offset(self, text, font_size):
        width = pyray.measure_text(text, font_size)
        return int(width / 2)