import constants
from game.casting.banner import Banner
from game.scripting.action import Action
from game.shared.point import Point
from game.shared.color import Color
from game.casting.missile import Missile

class HandleCollisionsAction(Action):
    """
    An update action that handles interactions between the actors.
    
    The responsibility of HandleCollisionsAction is to handle the situation when the tank collides
    with the items, or the tank collides with its segments, or the game is over.

    Attributes:
        _is_game_over (boolean): Whether or not the game is over.
    """

    def __init__(self):
        """Constructs a new HandleCollisionsAction."""
        self._is_game_over = False
        self._winner = ""
        self._winning_color = constants.GREY_80PCT

    def execute(self, cast, script):
        """Executes the handle collisions action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        if not self._is_game_over:
            # self._handle_item_collision(cast)
            self._handle_missile_tank_collision(cast)
            self._handle_missile_wall_collision(cast)
            self._handle_game_over(cast)

    # It looks like Dallas used the "items" category for the walls...
    def _handle_item_collision(self, cast):
        # """Unused right now, but could allow for possibility of picking up bonuses,
        # power-ups, other obstacles, etc...?
        
        # Args:
        #     cast (Cast): The cast of Actors in the game.
        # """
        # items = cast.get_actors("items")
        # tank1 = cast.get_actor("tanks", 0)
        # tank2 = cast.get_actor("tanks", 1)
        
        # for item in items:
        #     if tank1.get_position().equals(item.get_position()):
        #         print("Player 1 is touching a wall!")
        #     if tank2.get_position().equals(item.get_position()):
        #         print("Player 2 is touching a wall!")
        pass

    def _check_collision(self, thing_1, thing_2):
        """Check if two things has collided either one segment or another.
        
        Returns: (boolean) True is collision occurred.
        """
        return thing_1.get_position().equals(thing_2.get_position())

    def _set_winner(self, player_num = 0):
        """Sets the winner to the appropriate player:
            1 : Player 1
            2 : Player 2
            All other numbers = Nobody.
            
        Args:
            player_num (int): Either 1, or 2 depending on who won.
        """
        if player_num == 1:
            self._winner = "Player 1"
            self._winning_color = constants.GREEN_80PCT
        elif player_num == 2:
            self._winner = "Player 2"
            self._winning_color = constants.RED_80PCT
        else:
            self._winner = "Nobody"
            self._winning_color = constants.GREY_80PCT


    def _check_possible_collision(self, moving_thing, other_thing, tolerance):
        """Check if a moving thing might collide with another thing.

        Args:
            moving_thing (Actor): A thing that is actively about to move and has a velocity.
            other_thing (Actor): A thing that might be moving or not, but is considered 
                                 stationary for the purpose of this evaluation.
            tolerance (int): A pixel amount of padding (or not) that will make a collision
                             more (or less) likely.
        
        Returns: (boolean) True if collision would occur.
        """
        ## What if we simply subtract the two points and see if the difference is within a certain tolerance?
        mov_position = moving_thing.get_position()
        mov_velocity = moving_thing.get_velocity()
        new_pos = mov_position.add(mov_velocity)

        other_position = other_thing.get_position()
        distance = new_pos.abs_sub(other_position)

        is_impact = (distance.get_x() <= tolerance) and (distance.get_y() <= tolerance)

        return is_impact

        # ## Old code in case I need to refer to it.
        # x = (moving_thing.get_position().get_x() + moving_thing.get_velocity().get_x()) % constants.MAX_X
        # y = (moving_thing.get_position().get_y() + moving_thing.get_velocity().get_y()) % constants.MAX_Y
        # x_collides = False
        # y_collides = False

        # if x >= other_thing.get_position().get_x() - constants.CELL_BUFFER and x <= other_thing.get_position().get_x() + constants.CELL_BUFFER:
        #     x_collides = True

        # if y >= other_thing.get_position().get_y() - constants.CELL_BUFFER and y <= other_thing.get_position().get_y() + constants.CELL_BUFFER:
        #     y_collides = True

        # if x_collides == True and y_collides == True:
        #     return True


    def handle_tank_collision(self, cast, tank, opposite_tank):
        """Blocks the movement of tanks when they collide with a wall

        Args:
            cast (Cast): The cast of Actors in the game.

        Returns: (boolean) True if collision would occur.
        """
        walls = cast.get_actors("items")

        #Checks the collisions
        for wall in walls:
            if self._check_possible_collision(tank, wall, constants.WALL_BUBBLE):
                return True
            
            elif self._check_possible_collision(tank, opposite_tank, constants.WALL_BUBBLE):
                return True

        return False


    def _collides_with_wall(self, wall_list, thing):
        """Checks to see if our thing has collides with any member of wall_list.
        Returns True as soon as possible, or False if no collision.
        
        Args:
            wall_list list(Actors): All of the wall objects in a list to be checked against.
            thing (Any Actor): The thing that we think might have made collision.
        """
        for wall in wall_list:
            if self._check_possible_collision(thing, wall, constants.WALL_BUBBLE):
                return True

        return False


    def _handle_missile_wall_collision(self, cast):
        """Sets the game over flag if the tank collides with one of its segments.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        walls = cast.get_actors("items")
        missiles1 = cast.get_actors("missiles1")
        missiles2 = cast.get_actors("missiles2")

        for missile in missiles1:        
            if self._collides_with_wall(walls, missile):
                missile.explode(cast)
                cast.remove_actor("missiles1", missile)

        for missile in missiles2:        
            if self._collides_with_wall(walls, missile):
                missile.explode(cast)
                cast.remove_actor("missiles2", missile)
    
    
    def _handle_missile_tank_collision(self, cast):
        """Sets the game over flag if the tank collides with one of its segments.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        tanks = cast.get_actors("tanks")
        missiles1 = cast.get_actors("missiles1")
        missiles2 = cast.get_actors("missiles2")
        
        tank1 = tanks[0]
        tank2 = tanks[1]

        for missile in missiles2:
            if self._check_possible_collision(tank1, missile, constants.TANK_BUBBLE):
                # tank1.apply_damage(points)
                missile.explode(cast)
                cast.remove_actor("missiles2", missile)
                self._is_game_over = True
                self._set_winner(2)

        for missile in missiles1:
            if self._check_possible_collision(tank2, missile, constants.TANK_BUBBLE):
                # tank2.apply_damage(points)
                self._is_game_over = True
                missile.explode(cast)
                cast.remove_actor("missiles1", missile)
                # Check if both players triggered collision within the exact same frame...
                if self._winner == "":
                    self._set_winner(1)
                else:
                    self._set_winner(0)

          
    def _handle_game_over(self, cast):
        """Shows the 'game over' message and turns the tank and any items 
        white if the game is over.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        if self._is_game_over:
            tanks = cast.get_actors("tanks")
            bkg_color = self._winning_color
            text = "Game Over".center(21) + "\n" + f"{self._winner} Wins!".center(21)
            message = Banner(text, bkg_color, 40, 15)
            message.screen_center()
            
            cast.add_actor("banners", message)

            for tank in tanks:
                tank.set_color(constants.WHITE)
                

                