import constants
from game.scripting.action import Action
from game.shared.image import Image

class DrawActorsAction(Action):
    """
    An output action that draws all the actors.
    
    The responsibility of DrawActorsAction is to draw all the actors.

    Attributes:
        _video_service (VideoService): An instance of VideoService.
    """

    def __init__(self, video_service):
        """Constructs a new DrawActorsAction using the specified VideoService.
        
        Args:
            video_service (VideoService): An instance of VideoService.
        """
        self._video_service = video_service

    def execute(self, cast, script):
        """Executes the draw actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        tanks = cast.get_actors("tanks")
        walls = cast.get_actors("walls")
        missiles = cast.get_actors("missiles1")
        missiles.extend(cast.get_actors("missiles2"))
        healths = cast.get_actors("healths")

        background = Image(constants.BACKGROUND[constants.BACKGROUND_KEY])
        self._video_service.clear_buffer(background)
        
        for missile in missiles:
            self._video_service.draw_actor(missile)
            self._video_service.draw_missile(missile.get_image(), missile.get_position(), missile.get_text())
        
        for tank in tanks:
            self._video_service.draw_image(tank.get_image(), tank.get_image().get_position())

        for health in healths:
            self._video_service.draw_actor(health)

        for wall in walls:
            self._video_service.draw_image(wall.get_image(), wall.get_position())


        # Banners are last to have topmost priority
        # over all other items.
        self._video_service.draw_banners(banners, True)

        self._video_service.flush_buffer()