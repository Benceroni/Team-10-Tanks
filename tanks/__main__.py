import constants

from game.casting.cast import Cast
from game.casting.actor import Actor
from game.casting.score import Score
from game.casting.tank import Tank
from game.casting.health import Health

from game.scripting.script import Script
from game.scripting.control_actors_action import ControlActorsAction
from game.scripting.move_actors_action import MoveActorsAction
from game.scripting.handle_collisions_action import HandleCollisionsAction
from game.scripting.draw_actors_action import DrawActorsAction
from game.directing.director import Director
from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService
from game.shared.color import Color
from game.shared.point import Point
from game.casting.banner import Banner


def main():
    
    # create the cast
    cast = Cast()
    # cast.add_actor("items", Item())
    cast.add_actor("tanks", Tank(1))
    cast.add_actor("tanks", Tank(2))
    cast.add_actor("scores", Score())
    cast.add_actor("scores", Score())
    cast.add_actor("healths", Health(1))
    cast.add_actor("healths", Health(2))
    # TODO: set_stage() needs to be moved to a Level class or Stage class
    # Prompt for a stage 
    print("""
TANKS - Map Choice
-------------------------------------------
0. No Map
1. Closed Screen Borders
2. Symmetrically Staggered Vertical Walls
3. Diagonal Walls
""")
    user_choice = int(input("Your choice: "))
    if user_choice < 0 or user_choice > 3:
        user_choice = 0   
    cast.set_stage(user_choice)

    print("""
TANKS - Background choice
-------------------------------------------
1. Grass
2. Sand
3. Futuristic
4. Dark Grass
5. Dark Sand
6. Dark Futuristic
""")
    user_background = input("Your choice: ")
    if int(user_background) < 1 or int(user_choice) > 3:
        user_background = 1
    constants.BACKGROUND_KEY = user_background

    # start the game
    keyboard_service = KeyboardService()
    video_service = VideoService()

    title_banner = Banner("T", Color(0,0,0), 20, 4)
    title_banner.set_position(Point(400, 640))
    title_banner.set_text("Tanks by Team10")
    cast.add_actor("banners", title_banner)

    script = Script()
    script.add_action("input", ControlActorsAction(keyboard_service))
    script.add_action("update", MoveActorsAction())
    script.add_action("update", HandleCollisionsAction())
    script.add_action("output", DrawActorsAction(video_service))
    
    director = Director(video_service)
    director.start_game(cast, script)


if __name__ == "__main__":
    main()
