import constants
from game.casting.wall import Wall
from game.shared.point import Point

class Cast:
    """A collection of actors.

    The responsibility of a cast is to keep track of a collection of actors. It has methods for 
    adding, removing and getting them by a group name.

    Attributes:
        _actors (dict): A dictionary of actors { key: group_name, value: a list of actors }
    """

    def __init__(self):
        """Constructs a new Actor."""
        self._actors = {}
        
    def add_actor(self, group, actor):
        """Adds an actor to the given group.
        
        Args:
            group (string): The name of the group.
            actor (Actor): The actor to add.
        """
        if not group in self._actors.keys():
            self._actors[group] = []
            
        if not actor in self._actors[group]:
            self._actors[group].append(actor)

    def get_actors(self, group):
        """Gets the actors in the given group.
        
        Args:
            group (string): The name of the group.

        Returns:
            List: The actors in the group.
        """
        results = []
        if group in self._actors.keys():
            results = self._actors[group].copy()
        return results
    
    def get_all_actors(self):
        """Gets all of the actors in the cast.
        
        Returns:
            List: All of the actors in the cast.
        """
        results = []
        for group in self._actors:
            results.extend(self._actors[group])
        return results

    def get_actor(self, group, actor_index):
        """Gets the actor located at the given index in the given group.
        
        Args:
            group (string): The name of the group.
            
        Returns:
            Object: The actor located at actor_index position in the group.
        """
        result = None
        if group in self._actors.keys():
            if len(self._actors[group])-1 >= actor_index:
                result = self._actors[group][actor_index]
        return result

    def get_first_actor(self, group):
        """Gets the first actor in the given group.
        
        Args:
            group (string): The name of the group.
            
        Returns:
            Object: The first actor in the group.
        """
        return self.get_actor(group, 0)

    def remove_actor(self, group, actor):
        """Removes an actor from the given group.
        
        Args:
            group (string): The name of the group.
            actor (Actor): The actor to remove.
        """
        if group in self._actors:
            self._actors[group].remove(actor)
    
    # TODO: Needs to be moved to a Level or Stage class. Actors should be added to a group called "walls". 
    def set_stage(self, choice):
        """Based on the choice argument, this draws a calculated playfield for the players.

        Args:
            choice (int): A number specifyiing which level map to draw.
        """
        if choice == 0:
            # Nothing... Open field.
            pass

        elif choice == 1:
            # Screen borders... No wrapping.
            x1 = 20
            x2 = (constants.COLUMNS - 2) * constants.CELL_SIZE
            y1 = 20
            y2 = (constants.ROWS -2) * constants.CELL_SIZE

            for i in range(1, constants.COLUMNS-1):
                x = constants.CELL_SIZE * i
                wall = Wall(Point(x, y1), "O")
                self.add_actor("walls", wall)
                wall = Wall(Point(x, y2), "O")
                self.add_actor("walls", wall)

            for j in range(1, constants.ROWS-1):
                y = constants.CELL_SIZE * j
                wall = Wall(Point(x1, y), "O")
                self.add_actor("walls", wall)
                wall = Wall(Point(x2, y), "O")
                self.add_actor("walls", wall)

        elif choice == 2:
            # Symetrically staggered vertical walls
            start_x = 10
            start_y = 5
            for i in range(start_y, start_y + 10):
                x = start_x * constants.CELL_SIZE
                y = i * constants.CELL_SIZE
                wall = Wall(Point(x, y), "O")
                self.add_actor("walls", wall)

            start_y = 25
            for i in range(start_y, start_y + 10):
                x = start_x * constants.CELL_SIZE
                y = i * constants.CELL_SIZE
                wall = Wall(Point(x, y), "O")
                self.add_actor("walls", wall)

            start_x = 30
            start_y = 15
            for i in range(start_y, start_y + 10):
                x = start_x * constants.CELL_SIZE
                y = i * constants.CELL_SIZE
                wall = Wall(Point(x, y), "O")
                self.add_actor("walls", wall)

            start_x = 50
            start_y = 5
            for i in range(start_y, start_y + 10):
                x = start_x * constants.CELL_SIZE
                y = i * constants.CELL_SIZE
                wall = Wall(Point(x, y), "O")
                self.add_actor("walls", wall)

            start_y = 25
            for i in range(start_y, start_y + 10):
                x = start_x * constants.CELL_SIZE
                y = i * constants.CELL_SIZE
                wall = Wall(Point(x, y), "O")
                self.add_actor("walls", wall)

        elif choice == 3:
            # Diagonal Walls
            start_x = 5
            start_y = 15
            for i in range(10):
                x = (start_x + i) * constants.CELL_SIZE
                y = (start_y - i) * constants.CELL_SIZE
                wall = Wall(Point(x, y), "/")
                self.add_actor("walls", wall)

            start_x = 5
            start_y = 26
            for i in range(10):
                x = (start_x + i) * constants.CELL_SIZE
                y = (start_y + i) * constants.CELL_SIZE
                wall = Wall(Point(x, y), "\\")
                self.add_actor("walls", wall)

            start_x = constants.COLUMNS - 5
            start_y = 15
            for i in range(10):
                x = (start_x - i) * constants.CELL_SIZE
                y = (start_y - i) * constants.CELL_SIZE
                wall = Wall(Point(x, y), "\\")
                self.add_actor("walls", wall)

            start_x = constants.COLUMNS - 5
            start_y = 26
            for i in range(10):
                x = (start_x - i) * constants.CELL_SIZE
                y = (start_y + i) * constants.CELL_SIZE
                wall = Wall(Point(x, y), "/")
                self.add_actor("walls", wall)

            start_x1 = 30-5
            start_y1 = 20-5
            start_x2 = 30-5
            start_y2 = 20+5
            for i in range(11):
                x1 = (start_x1 + i) * constants.CELL_SIZE
                y1 = (start_y1 + i) * constants.CELL_SIZE
                x2 = (start_x2 + i) * constants.CELL_SIZE
                y2 = (start_y2 - i) * constants.CELL_SIZE
                wall = Wall(Point(x1, y1), "\\")
                self.add_actor("walls", wall)
                wall = Wall(Point(x2, y2), "/")
                self.add_actor("walls", wall)