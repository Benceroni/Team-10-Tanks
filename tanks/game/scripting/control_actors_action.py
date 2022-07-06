import constants
from game.scripting.action import Action
from game.shared.point import Point


class ControlActorsAction(Action):
    """
    An input action that controls the tank.
    
    The responsibility of ControlActorsAction is to get the direction and move the tank's head.

    Attributes:
        _keyboard_service (KeyboardService): An instance of KeyboardService.
    """

    def __init__(self, keyboard_service):
        """Constructs a new ControlActorsAction using the specified KeyboardService.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
        """
        self._keyboard_service = keyboard_service
        # self._direction1 = Point(constants.CELL_SIZE, 0)
        # self._direction2 = Point(constants.CELL_SIZE, 0)

    def execute(self, cast, script):
        """Executes the control actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        tank1 = cast.get_actors("tanks")[0]
        tank2 = cast.get_actors("tanks")[1]

        current_dir1 = Point(0, 0)
        current_dir2 = Point(0, 0)

        # left
        if self._keyboard_service.is_key_down('a'):
            current_dir1 = Point(-constants.CELL_SIZE, 0)
        
        # right
        if self._keyboard_service.is_key_down('d'):
            current_dir1 = Point(constants.CELL_SIZE, 0)
        
        # up
        if self._keyboard_service.is_key_down('w'):
            current_dir1 = Point(0, -constants.CELL_SIZE)
        
        # down
        if self._keyboard_service.is_key_down('s'):
            current_dir1 = Point(0, constants.CELL_SIZE)

        # fire
        if self._keyboard_service.is_key_down('l_ctrl') or self._keyboard_service.is_key_down('l_alt'):
            tank1.fire_bullet(current_dir1)
        
        tank1.set_velocity(current_dir1)

        # left
        if self._keyboard_service.is_key_down('j'):
            current_dir2 = Point(-constants.CELL_SIZE, 0)
        
        # right
        if self._keyboard_service.is_key_down('l'):
            current_dir2 = Point(constants.CELL_SIZE, 0)
        
        # up
        if self._keyboard_service.is_key_down('i'):
            current_dir2 = Point(0, -constants.CELL_SIZE)
        
        # down
        if self._keyboard_service.is_key_down('k'):
            current_dir2 = Point(0, constants.CELL_SIZE)

        # fire
        if self._keyboard_service.is_key_down('r_ctrl') or self._keyboard_service.is_key_down('r_alt'):
            tank2.fire_bullet(current_dir2)
        
        tank2.set_velocity(current_dir2)