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
        #Gets the tanks
        tank1 = cast.get_actors("tanks")[0]
        tank2 = cast.get_actors("tanks")[1]

        tank1_x = 0
        tank1_y = 0
        tank2_x = 0
        tank2_y = 0
        

        #Sets the movement of the first tank
        # left
        if self._keyboard_service.is_key_down('a'):
            tank1_x = round(constants.TANK_SPEED * -constants.CELL_SIZE)
            tank1.set_facing(Point(tank1_x, tank1_y))
        
        # right
        if self._keyboard_service.is_key_down('d'):
            tank1_x = round(constants.TANK_SPEED * constants.CELL_SIZE) 
            tank1.set_facing(Point(tank1_x, tank1_y))
        
        # up
        if self._keyboard_service.is_key_down('w'):
            tank1_y = round(constants.TANK_SPEED * -constants.CELL_SIZE)
            tank1.set_facing(Point(tank1_x, tank1_y))

        # down
        if self._keyboard_service.is_key_down('s'):
            tank1_y = round(constants.TANK_SPEED * constants.CELL_SIZE)
            tank1.set_facing(Point(tank1_x, tank1_y))

        # fire
        if self._keyboard_service.is_key_down('l_ctrl') or self._keyboard_service.is_key_down('l_alt'):
            tank1.fire_missile(cast)

        tank1.set_velocity(Point(tank1_x, tank1_y))

        #Sets the movement of the second tank
        # left
        if self._keyboard_service.is_key_down('j'):
            tank2_x = round(constants.TANK_SPEED * -constants.CELL_SIZE)
            tank2.set_facing(Point(tank2_x, tank2_y))

        # right
        if self._keyboard_service.is_key_down('l'):
            tank2_x = round(constants.TANK_SPEED * constants.CELL_SIZE)
            tank2.set_facing(Point(tank2_x, tank2_y))

        # up
        if self._keyboard_service.is_key_down('i'):
            tank2_y = round(constants.TANK_SPEED * -constants.CELL_SIZE)
            tank2.set_facing(Point(tank2_x, tank2_y))

        # down
        if self._keyboard_service.is_key_down('k'):
            tank2_y = round(constants.TANK_SPEED * constants.CELL_SIZE)           
            tank2.set_facing(Point(tank2_x, tank2_y))        

        # fire
        if self._keyboard_service.is_key_down('r_ctrl') or self._keyboard_service.is_key_down('r_alt'):
            tank2.fire_missile(cast)

        tank2.set_velocity(Point(tank2_x, tank2_y))

        if self._keyboard_service.is_key_down('pause'):
            breakpoint = True
