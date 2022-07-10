from game.scripting.action import Action
from game.shared.point import Point
from game.scripting.handle_collisions_action import HandleCollisionsAction

class MoveActorsAction(Action):
    """
    An update action that moves all the actors.
    
    The responsibility of MoveActorsAction is to move all the actors that have a velocity greater
    than zero.
    """

    def execute(self, cast, script):
        """Executes the move actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        collision_checker = HandleCollisionsAction()

        tanks = cast.get_actors("tanks")
        walls = cast.get_actors("items")
        missiles = cast.get_actors("missiles1")
        missiles.extend(cast.get_actors("missiles2"))

        if collision_checker.handle_tank_collision(cast, tanks[0], tanks[1]):
            tanks[0].set_velocity(Point(0, 0))
        tanks[0].move_next()

        if collision_checker.handle_tank_collision(cast, tanks[1], tanks[0]):
            tanks[1].set_velocity(Point(0, 0))
        tanks[1].move_next()

        for missile in missiles:
            missile.move_next()

        # Clean up dead missiles
        missiles1 = cast.get_actors("missiles1")
        missiles2 = cast.get_actors("missiles2")

        for missile in missiles1:
            if missile.get_range() <= 0:
                # When missiles die, they explode.
                missile.explode(cast)
                cast.remove_actor("missiles1", missile)

        for missile in missiles2:
            if missile.get_range() <= 0:
                missile.explode(cast)
                cast.remove_actor("missiles2", missile)
