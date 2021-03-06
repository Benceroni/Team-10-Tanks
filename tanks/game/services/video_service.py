import pyray
import constants
import pathlib
import os
from game.shared.point import Point
from game.casting.banner import Banner

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

    def draw_image(self, image, position, color = pyray.WHITE):
        """Draws the image that is passed
        
        Args:
            image (Image): An instance of image to be drawn.
            position (Point): An instance of point to represent position.
            color (Color): An instance of color to represent tint.
        """
        filepath = image.get_filename()
        filepath = str(pathlib.Path(filepath))
        texture = self._textures[filepath]
        x = position.get_x()
        y = position.get_y()
        raylib_position = pyray.Vector2(x, y)
        tint = color
        scale = image.get_scale()
        rotation = image.get_rotation()
        tint = image.get_tint()
        pyray.draw_texture_ex(texture, raylib_position, rotation, scale, tint)

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
        pyray.init_window(constants.WINDOW_MAX_X, constants.WINDOW_MAX_Y, constants.CAPTION)
        pyray.set_target_fps(constants.FRAME_RATE)

    def _draw_grid(self):
        """Draws a grid on the screen."""
        for y in range(0, constants.GAME_MAX_Y, constants.CELL_SIZE):
            pyray.draw_line(0, y, constants.GAME_MAX_X, y, pyray.GRAY)
            
        for x in range(0, constants.GAME_MAX_X, constants.CELL_SIZE):
            pyray.draw_line(x, 0, x, constants.GAME_MAX_Y, pyray.GRAY)


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

    def draw_tank(self, image, position, reloading = False):
        """Checks if the tank is reloading or not and changes the tint.

        Args:
            image (Image): The image to draw.
            position (Point): The position of the image.
            reloading (Boolean): Defines if the tank is recharging or not.
        """
        if reloading:
            self.draw_image(image, position, pyray.GRAY)

        elif not reloading:
            self.draw_image(image, position)

    def _get_x_offset(self, text, font_size):
        width = pyray.measure_text(text, font_size)
        return int(width / 2)


    def draw_status(self, status):
        """Utilizes a banner object to draw and update the health status on the screen.
        
        Args:
            health (Health): An instance of Health.
        """
        player_num = status.get_player_num()
        bk_color = constants.PLAYER_COLORS[player_num]['wait']
        text = status.get_text()
        status_banner = Banner(text, bk_color, 20, 1)
        text_color = constants.RED
        if status.get_health_points() > 60:
            text_color = constants.GREEN
        elif status.get_health_points() > 40:
            text_color = constants.YELLOW
        elif status.get_health_points() > 20:
            text_color = constants.ORANGE
        
        status_banner.set_color(text_color)
        status_banner.set_position(status.get_position())
        
        self.draw_banner(status_banner, False)

      
    def draw_banner(self, banner, centered=False):
        """Draws the given banner's text on the screen with the appropriate background.

        Args:
            actor (Actor): The actor to draw.
        """ 
        text = banner.get_text()
        pad = banner.get_padding()
        x = banner.get_position().get_x()
        y = banner.get_position().get_y()
        w = banner.get_width() 
        h = banner.get_height()
        
        if centered:
            # width = pyray.measure_text(text, font_size)
            offset = int(w / 2)
            x -= offset

        text_x = x + pad
        text_y = y + pad
        bkg = banner.get_bkg_color().to_tuple()
        font_size = banner.get_font_size()
        color = banner.get_color().to_tuple()

        pyray.draw_rectangle(x, y, w, h, bkg)
        pyray.draw_text(text, text_x, text_y, font_size, color)



    def draw_banners(self, banners, centered=False):
        """Draws the text for the given list of actors on the screen.

        Args:
            actors (list): A list of actors to draw.
        """ 
        for banner in banners:
            self.draw_banner(banner, centered)