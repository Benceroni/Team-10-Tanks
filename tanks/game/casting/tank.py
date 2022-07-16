import constants
from game.casting.missile import Missile
from game.casting.actor import Actor
from game.shared.point import Point
from game.shared.image import Image


class Tank(Actor):
    """
    An old-school tank that leaves a solid beam of light as it's trail.
    
    The responsibility of tank is to move itself.

    Attributes:
        _player_number (int): Identifies which player the tank instance belongs to.
        _num_rounds (int): The number of active missiles on the screen from this player.
        _color (Color): The color that the light wall should be rendered.
        _wall_active (bool): Whether or not new wall segments are being drawn from this tank.
        _facing (Point): Is really the last velocity that the tank moved that is not (0,0) which defines which
                         direction it is facing.
    
        All other attributes and methods inherited from Actor.
    """
    def __init__(self, player_number=0):
        """Creates a new instance of a tank. 
        
        Args:
            player_number: (Int) - A number referring to which player this will belong.
        """
        super().__init__()
        self._player_number = player_number
        self._is_alive = True
        self._color = constants.PLAYER_COLORS[player_number]['ready']
        self._text = constants.TANK_SHAPE
        self._reloading = False
        self.set_image(Image(constants.TANK_IMAGES[player_number]["animation1"]))
        x = int(constants.CELL_SIZE * constants.PLAYER_START[self._player_number].get_x())
        y = int(constants.CELL_SIZE * constants.PLAYER_START[self._player_number].get_y())
        self._position = Point(x, y)
        self._fire_delay = constants.TANK_REPEAT_RATE
        self._reload_gun()
        self._facing = Point(0, -1) # Set the initial facing direction to UP.

    def set_facing(self, velocity):
        """Sets the _facing attribute to point the Tank in different directions. The velocity data is
        reduced to a simple pair of X,Y velocities represented by -1, 0, or 1 to identify facing 
        direction, e.g. (-1, 0) would be facing left, (1, 1) would be facing diagonal down right.
        
        Args:
            velocity (Point): defines a facing direction based on the last direction moved.
        """
        new_x = velocity.get_x() 
        new_y = velocity.get_y()
        
        if new_x != 0:
            new_x = new_x / abs(new_x)
        if new_y != 0:
            new_y = new_y / abs(new_y)

        self._facing = Point(new_x, new_y)

    def rotate_tank(self):
        """Rotates the image depending in the direction its facing the tank has.
        """
        x = self._facing.get_x()
        y = self._facing.get_y()

        # Up
        if x == 0 and y <= -0.1: 
            self._image.set_rotation(0)

        #Up-Right
        elif x >= 0.1 and y <= -0.1:
            self._image.set_rotation(45)

        #Right
        elif x >= 0.1 and y == 0:
            self._image.set_rotation(90)
        
        #Down-Right
        elif x >= 0.1 and y >= 0:
            self._image.set_rotation(135)

        #Down
        elif x == 0 and y >= 0.1:
            self._image.set_rotation(180)

        #Down-Left
        elif x <= 0.1 and y >= 0.1:
            self._image.set_rotation(225)

        #Left
        elif x <= 0.1 and y == 0:
            self._image.set_rotation(270)

        #Up-Left
        elif x <= 0.1 and y <= -0.1:
            self._image.set_rotation(315)

    def _reload_gun(self):
        """Reloads the player's gun with ammunition and resets the reload timer.
        """
        self._num_rounds = constants.TANK_AMMO_ROUNDS
        self._reload_time = round(constants.TANK_RELOAD_RATE * constants.FRAME_RATE)


    def _do_fire_delay(self):
        """Handle the delay between firing consectutive rounds.
        """
        if self._fire_delay < constants.TANK_REPEAT_RATE:
            self._fire_delay += 1


    def _do_reload_delay(self):
        """If out of rounds, start timer to reload a set of rounds, 
        then activate actual reload
        """
        if self._num_rounds < 1:
            self.set_color(constants.PLAYER_COLORS[self._player_number]['wait'])
            self.get_image().set_tint(constants.PLAYER_COLORS[self._player_number]['wait'].to_tuple())
            self._reload_time -= 1
            if self._reload_time == 0:
                self._reload_gun()
                self.set_color(constants.PLAYER_COLORS[self._player_number]['ready'])
                self.get_image().set_tint(constants.WHITE.to_tuple())


    def move_next(self):
        """Performs all of the move_next actions of the parent, plus updating the gun status
        and gun timers as needed.
        """
        super().move_next()
        self.rotate_tank()
        self._image.set_position(self._position)
        self._do_fire_delay()
        self._do_reload_delay()        

    def fire_missile(self, cast):
        """Creates a missile actor (fires a missile or projectile) and sets its velocity. The 
        starting position is the same as the tank's position.
        
        Args:
            cast (Cast): A list of Actors in acting groups that we will add the missile to. 
            velocity (Point): The initial Vx, Vy velocity of the missile. 
        """
        if self._is_alive and self._num_rounds > 0 and self._fire_delay == constants.TANK_REPEAT_RATE:
            velocity = self._facing.scale(constants.MISSILE_SPEED * constants.CELL_SIZE)
            missile = Missile(self._player_number, self._position, velocity, self._color)
            cast.add_actor(f"missiles{self._player_number}", missile)
            self._num_rounds -= 1
            self._fire_delay = 0

    def get_reloading(self):
        """Sees if the tanks is reloading or not

        Returns:
            reloading (boolean)
        """
        return self._reloading

        # Tanks explode too.
    def explode(self, cast):
        """Explodes this tank.
        Args:
            cast (Cast): The cast of actors within which the new missiles will be spawned.
        """
        
        for vector in constants.MISSILE_EXPLOSION_VELOCITIES:
            self.set_velocity(Point(0,0))
            shrapnel = Missile(self._player_number, self._position, vector, constants.YELLOW)
            shrapnel.set_range(constants.MISSILE_BLAST_RANGE * 2)
            shrapnel.set_phase(0)
            self._is_alive = False
            cast.add_actor(f"missiles{self._player_number}", shrapnel)
