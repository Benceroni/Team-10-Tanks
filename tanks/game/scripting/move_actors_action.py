from game.scripting.action import Action


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
        missiles = cast.get_actors("missiles")

        if collision_checker.handle_tank_collision(cast, tanks[0], tanks[1]):
            tanks[0].set_velocity(Point(0, 0))
        tanks[0].move_next()

        if collision_checker.handle_tank_collision(cast, tanks[1], tanks[0]):
            tanks[1].set_velocity(Point(0, 0))
        tanks[1].move_next()

        for missile in missiles:
            missile.move_next()

        # Clean up dead missiles
        missiles = cast.get_actors("missiles")

        for missile in missiles:
            if missile.get_range() <= 0:
                cast.remove_actor("missiles", missile)


        # tanks = cast.get_actors("tanks")
        # for tank in tanks:
        #     tank.grow_tail(1)
