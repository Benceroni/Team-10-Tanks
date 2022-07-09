from game.casting.item import Item
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
    
    def set_stage(self, choice):
        if choice == 1:
            x = 200
            y = 50
            count = 0
            while count < 825:
                if count == 75:
                    y = 250
                if count == 150:
                    y = 450
                if count == 225:
                    y = 1
                    x = 450
                if count == 300:
                    y = 200
                if count == 475:
                    y = 500
                if count == 600:
                    x = 700
                    y = 50
                if count == 675:
                    y = 250
                if count == 750:
                    y = 450
                item = Item()
                item.set_position(Point(x, y))
                self.add_actor("items", item)
                count += 1
                y += 1
        elif choice == 2:
            x = 200
            y = 100
            count = 0
            while count < 500:
                if count == 100:
                    y = 350
                    x = 200
                if count == 250:
                    y = 100
                    x = 550
                if count == 400:
                    y = 400
                    x = 550
                item = Item()
                item.set_position(Point(x, y))
                self.add_actor("items", item)
                count += 1
                y += 1
                x += 1