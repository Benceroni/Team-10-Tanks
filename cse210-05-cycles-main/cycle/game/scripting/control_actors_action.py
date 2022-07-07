import constants
from game.scripting.action import Action
from game.shared.point import Point


class ControlActorsAction(Action):
    """
    An input action that controls both tanks.
    
    The responsibility of ControlActorsAction is to get the direction and move the tanks.

    Attributes:
        _keyboard_service (KeyboardService): An instance of KeyboardService.
    """

    def __init__(self, keyboard_service):
        """Constructs a new ControlActorsAction using the specified KeyboardService.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
        """
        self._keyboard_service = keyboard_service

    def execute(self, cast, script):
        """Executes the control actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        tank1 = cast.get_actors("cycles")[0]
        tank2 = cast.get_actors("cycles")[1]

        #Movement for the first tank:
        # left
        if self._keyboard_service.is_key_down('a'):
            tank1.turn_head(Point(round(0.25 * -constants.CELL_SIZE), 0))
        
        # right
        if self._keyboard_service.is_key_down('d'):
            tank1.turn_head(Point(round(0.25 * constants.CELL_SIZE), 0))
        
        # up
        if self._keyboard_service.is_key_down('w'):
            tank1.turn_head(Point(0, round(0.25 * -constants.CELL_SIZE)))
        
        # down
        if self._keyboard_service.is_key_down('s'):
            tank1.turn_head(Point(0, round(0.25 * constants.CELL_SIZE)))
        

        #Movement for the second tank:
        # left
        if self._keyboard_service.is_key_down('j'):
            tank2.turn_head(Point(round(0.25 * -constants.CELL_SIZE), 0))
        
        # right
        if self._keyboard_service.is_key_down('l'):
            tank2.turn_head(Point(round(0.25 * constants.CELL_SIZE), 0))
        
        # up
        if self._keyboard_service.is_key_down('i'):
            tank2.turn_head(Point(0, round(0.25 * -constants.CELL_SIZE)))
        
        # down
        if self._keyboard_service.is_key_down('k'):
            tank2.turn_head(Point(0, round(0.25 * constants.CELL_SIZE)))