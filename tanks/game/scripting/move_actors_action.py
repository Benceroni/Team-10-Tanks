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
        actors = cast.get_all_actors()
        for actor in actors:
            actor.move_next()
            

        # Clean up dead missiles
        missiles = cast.get_actors("missiles")

        for missile in missiles:
            if missile.get_range() <= 0:
                cast.remove_actor("missiles", missile)


        # tanks = cast.get_actors("tanks")
        # for tank in tanks:
        #     tank.grow_tail(1)