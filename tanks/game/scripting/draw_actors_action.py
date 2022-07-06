from game.scripting.action import Action


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
        score = cast.get_first_actor("scores")
        tanks = cast.get_actors("tanks")
        
        banners = cast.get_actors("banners")
        bullets = cast.get_actors("bullets")

        self._video_service.clear_buffer()
        for tank in tanks:
            self._video_service.draw_actor(tank)

        for bullet in bullets:
            self._video_service.draw_bullet(bullet)

        # Banners are last to have topmost priority
        # over all other items.
        self._video_service.draw_banners(banners, True)
        self._video_service.flush_buffer()