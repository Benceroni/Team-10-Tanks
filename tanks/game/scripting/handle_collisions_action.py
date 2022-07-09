import constants
from game.casting.banner import Banner
from game.scripting.action import Action
from game.shared.point import Point
from game.shared.color import Color

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
            self._handle_item_collision(cast)
            self._handle_missile_collision(cast)
            self._handle_game_over(cast)

    # It looks like Dallas used the "items" category for the walls, so we may implement this.
    def _handle_item_collision(self, cast):
        """Unused right now, but could allow for possibility of picking up bonuses,
        power-ups, other obstacles, etc...?
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        items = cast.get_actors("items")
        tank1 = cast.get_actor("tanks", 0)
        tank2 = cast.get_actor("tanks", 1)
        
        for item in items:
            if tank1.get_position().equals(item.get_position()):
                print("Player 1 is touching a wall!")
            if tank2.get_position().equals(item.get_position()):
                print("Player 2 is touching a wall!")
        

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


    def _check_possible_collision(self, thing_1, thing_2):
        """Check if a thing has collided with another thing.
        
        Returns: (boolean) True if collision would occur.
        """
        x = (thing_1.get_position().get_x() + thing_1.get_velocity().get_x()) % constants.MAX_X
        y = (thing_1.get_position().get_y() + thing_1.get_velocity().get_y()) % constants.MAX_Y
        x_collides = False
        y_collides = False

        if x >= thing_2.get_position().get_x() - 8 and x <= thing_2.get_position().get_x() + 8:
            x_collides = True

        if y >= thing_2.get_position().get_y() - 8 and y <= thing_2.get_position().get_y() + 8:
            y_collides = True

        if x_collides == True and y_collides == True:
            return True


    def handle_tank_collision(self, cast, tank, opposite_tank):
        """Blocks the movement of tanks when they collide with a wall

        Args:
            cast (Cast): The cast of Actors in the game.

        Returns: (boolean) True if collision would occur.
        """
        walls = cast.get_actors("items")

        #Checks the collisions
        for wall in walls:
            if self._check_possible_collision(tank, wall):
                return True
            
            elif self._check_possible_collision(tank, opposite_tank):
                return True

        return False


    def _handle_missile_collision(self, cast):
        """Sets the game over flag if the tank collides with one of its segments.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        tanks = cast.get_actors("tanks")
        missiles = cast.get_actors("missiles")
        
        tank1 = tanks[0]
        tank2 = tanks[1]
        
        for missile in missiles:
            if self._check_possible_collision(tank1, missile):
                # tank1.apply_damage(points)
                self._is_game_over = True
                self._set_winner(2)

            if self._check_possible_collision(tank2, missile):
                # tank2.apply_damage(points)
                self._is_game_over = True
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
                

                