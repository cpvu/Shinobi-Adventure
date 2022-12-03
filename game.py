"""
Calvin Vu
A01291758

Hanxiao Mao
A01293003

Contains main game file and functions.
"""
import time
from generate_game_board import generate_game_board
from battle import generate_monster, execute_battle_protocol, generate_elite_monster, generate_boss_monster
from game_events import generate_game_events, execute_open_sacred_scroll
from character_creation import make_character
from character_location import describe_current_location, get_user_choice, validate_move, move_character
from level_up import character_has_leveled, execute_character_glow_up, assign_experience, assign_stats
from health_room import execute_health_room


def game_introduction():
    """
    Print a message introducing the story of the game.

    :post-condition: Print out the storyline of the Shinobi World
    """
    print(" ____ _  _ _ _  _ ____ ___  _ \n", " [__  |__| | |\\ | |  | |__] | \n", " ___] |  | | | \\| |__| |__] | \n")
    time.sleep(0.5)
    print("Welcome to the world of Shinobi, the land of ninjas and ninjitsu.")
    time.sleep(0.5)
    print("Chakra is the core of the power of ninjitsu and using powerful jutsus.")
    time.sleep(0.5)
    print("You're not from this world?")
    time.sleep(0.5)
    print("This world is a little bit different from where you came from...")
    time.sleep(0.5)
    print("The world needs your help to defeat Madara Uchiha.")
    time.sleep(0.5)
    print("Madara Uchiha is trying to put the world of Shinobi into an infinite dream state called "
          "the Infinite Tsukuyomi.")
    time.sleep(0.5)
    print("I sense you have immense chakra, but you must first traverse through this land to "
          "gain more power and jutsus.\n")
    time.sleep(0.5)


def game_over(character: dict):
    """
    Return True if the character's HP is below 0 or below.

    :param character: a dictionary object
    :pre-condition: character must be a dictionary object containing key values: "Name" containing a string, X", "Y",
                   "Level", "XP", "XPToLevelUp", "HP", "Chakra", "Max Chakra", "Attack", "Magic", "Luck"
                   containing integer values, "Goal achieved" containing a boolean, and "Jutsu" containing
                   a dictionary object.
    :post-condition: Evaluate the integer value for key "HP" in the dictionary object character and return True if
                     it is less than or equal to 0.
    return: a boolean value, True if the value of key "HP" in the argument dictioanry is less than or equal to 0
    """
    if character["HP"] <= 0:
        print("You have died...")
        print("Game over, please try again")
        return True
    return False


def check_for_event(board: dict, character: dict) -> str:
    """
    Evaluate the character's current board coordinates to execute the corresponding event on the game board.

    :param board: a dictionary object
    :param character: a dictionary object
    :pre-condition: character must be a dictionary object that represents the character of the game, specifically
                    containing a key value pair with a key value of "X" and "Y" each with integer values
    :pre-condition: board must be a dictionary object that represents the game board containing key value pairs, where
                    the key is a tuple that contains 2 integer values representing the board coordinate, and contains
                    a string value that represents the room type.
    :post-condition: Compare the values stored in the X and Y keys in the character dictionary to the corresponding
                     key tuples in the board object to return a string value representing the event on the coordinate
    :return: a string value, representing the event type stored on the board coordinate
    """
    if board[(character["X"], character["Y"])] == "Game Event":
        return "GameEvent"
    elif board[(character["X"], character["Y"])] == "Monster Battle":
        return "Battle"
    elif board[(character["X"], character["Y"])] == "Health room":
        return "Health"
    elif board[(character["X"], character["Y"])] == "Boss room":
        return "Boss"
    elif board[(character["X"], character["Y"])] == "Elite room":
        return "Elite"
    else:
        return "Empty Room"


def display_final_boss_ascii_art():
    print(""" ⠀⠀⠀⠀⣀⣀⣀⣀⣀⣀⣤⣤⣤⣤⣤⣤⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠻⠋⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠉⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠙⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣬⣍⣒⡢⡤⢀⡀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡶⠟⠓
    ⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠿⠓⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⢀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠋⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠙⠋⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⢀⣄⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⢀⡴⠙⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡄⡀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⣿⣿⡿⠟⠛⢉⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣤⠔⠈⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡜⢆⠀⠀⠀⠀⠀
    ⠀⠀⠈⠉⠀⠀⢀⣠⣾⣿⣿⣿⠟⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠀⠘⡄⠀⠀⠀⢸⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡌⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣣⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⣠⠴⠛⠙⢦⠀⣀⡼⠟⣿⣿⣿⣿⣿⣿⣿⣿⣿⢋⣿⣿⠈⠻⣿⣿⡄⠀⠀⠀⠀
    ⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠀⠀⠀⢀⣠⡾⣿⣿⣗⡲⣿⣿⣿⣿⣿⣿⣿⡿⣡⣼⣿⣿⣦⣤⣌⣙⣷⡄⠀⠀⠀
    ⠀⠀⠀⢠⣿⣿⣿⣿⣿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢏⡇⠀⣠⣴⣿⣿⣿⣿⣿⣟⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⠀⠀⠉⢻⣿⣄⠀⠀
    ⠀⠀⢠⣿⣿⣿⡟⠉⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣼⣿⣿⣿⠈⣧⣻⣿⣿⣿⣿⣿⣿⡿⢿⡿⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⣤⡾⠃⡏⡇⠀
    ⠀⠀⢸⣿⣿⠇⠳⣄⡀⢀⣾⣿⣿⣏⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⣸⣿⣿⣯⡛⢋⣿⣯⠤⠬⣙⣲⠤⠔⢦⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠖⠋⠀⠀⣿⡇⠀
    ⠀⢠⣿⡿⢻⠀⠀⠀⠉⠛⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢃⢦⣿⡿⠉⠉⠉⠙⠛⠃⠒⠒⠚⠢⢄⡀⢈⡇⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀⢠⡇⠀⠀
    ⢀⡾⠋⢀⡾⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣏⡞⢸⣿⠃⠀⠀⠀⠀⠀⠈⠙⠲⣄⡀⠀⠉⢾⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⣸⡇⠀⠀
    ⠀⠀⠀⣸⡇⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢸⣿⢸⡏⠀⢲⣄⠀⣠⣶⠂⠀⠀⠀⣹⡄⠀⡿⢹⣿⣿⣿⣿⣿⣿⣿⣿⣴⣿⣿⡿⠀⠀⠀⠀⢨⠿⠃⠀⠀
    ⠀⠀⠀⣿⡇⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠋⠻⢦⣤⣄⣹⡿⣟⣁⣀⣀⡴⠋⠙⢀⣞⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡷⠤⣄⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⣿⠛⣄⢠⠀⠀⠀⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀⠀⠀⣍⡁⠀⠀⠛⠛⠛⡉⠀⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠘⡆⠀⠀⠀⡂⠀⠀
    ⠀⠀⠀⠛⠀⠈⢳⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣄⠀⠀⠠⢍⡉⠉⣉⠉⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⢇⢀⣴⡆⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⢸⣄⠀⠀⢸⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⡀⠀⢹⡏⢀⣠⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⢀⣼⣋⠞⠀⠀⠀⠀""")


def display_final_boss_dialogue():
    """
       Print the final boss dialogue.

       :post-condition: print out the final boss's dialogue.
    """
    print("You've arrived to the the Uchiha Clan's dominion. He emits his powerful chakra and suddenly everything "
          "around him craters.")
    print("So.. you are the one. I heard of an unknown shinobi who travelled across this great land in hopes to defeat "
          "me.")
    print("I am Madara Uchiha and you will not stop me from casting this eternal dream state.")


def validate_boss_fight(character: dict):
    """
    Validate if the character dictionary object is Level 3


    :param character: a dictionary object
    :pre-condition: character must be a dictionary object containing key values: "Name" containing a string, X", "Y",
                    "Level", "XP", "XPToLevelUp", "HP", "Chakra", "Max Chakra", "Attack", "Magic", "Luck"
                    containing integer values, "Goal achieved" containing a boolean, and "Jutsu" containing
                    a dictionary object.
    :post-condition: return a boolean value, True if the character key "Level" value is equal to 3.
    :post-condition: print a statement to indicate the character has not met the condition and return a boolean value,
                     False
    :return: a boolean value, True if the character key "Level" is equal to 3
    """
    if character["Level"] == 3:
        return True
    else:
        print("You've arrived at the Uchiha Dominion, but you are not strong enough yet.. Return here "
              "once you have reached Level 3!")
        return False


def elite_monster_dialogue():
    """
    Print the elite monster room dialogue.

    :post-condition: print out the elite monster's dialogue.
    """
    print("You arrive at a path with a vast forest ahead. Stepping forward, you suddenly hear the sounds of hissing.")
    print("Suddenly, snakes appear to be falling from the trees. A dark figure emerges out of the forest.")
    print("Orochimaru: Hsss I am Orochimaru the legendary snake sannin. Your chakra smells very fruitful...")
    print("You've heard stories of this before in the village you visted, it looks like you have to defeat Orochimaru!")


def elite_monster_defeat():
    """
    Print the elite monster room dialogue for defeat.

    :post-condition: print out the elite monster's defeat dialogue.
    """
    print("This cant be.... I've been defeated..")
    print("Orochimarus body dissipates, leaving behind a scroll.")


def execute_event_protocol(character: dict, event: str):
    """
    Execute the game event that corresponds to the character's board location.

    :param character: a dictionary object
    :param event: a string value
    :pre-condition: character must be a dictionary object containing key pair values relevant to the character's
                   in-game stats
    :pre-condition: event must be a string that represents the event type to be executed
    :post-condition: Evaluate and execute the corresponding functions for the argument event string.
    :post-condition: Return None if the user enters an empty room
    :return: Return None if the user enters an empty room
    """
    if event == "Battle":
        monster = generate_monster(character)
        print(f"A {monster['name']} has appeared before you!")
        execute_battle_protocol(character, monster)
    elif event == "GameEvent":
        generate_game_events(character)
    elif event == "Health":
        execute_health_room(character)
    elif event == "Boss":
        if validate_boss_fight(character):
            display_final_boss_ascii_art()
            display_final_boss_dialogue()
            execute_battle_protocol(character, generate_boss_monster())
            character["Goal Achieved"] = True
    elif event == "Elite":
        elite_monster_dialogue()
        execute_battle_protocol(character, generate_elite_monster())
        elite_monster_defeat()
        execute_open_sacred_scroll(character)
    else:
        print("You've entered an empty room. There appears to be nothing in here..")
        return


def execute_victory():
    """
    Print the game victory dialogue.

    :post-condition: print the end game victory message
    """
    print("Its all over... I can't believe I did it.")
    print("Roars of victory yell out as the world witnessed your conquer.")
    print("It seems as though you are fading away and now its time to go back to your world...")


def check_if_goal_attained(character: dict) -> bool:
    """
    :param character: a dictionary object
    :pre-condition: character must be a dictionary object containing key values: "Name" containing a string, X", "Y",
                    "Level", "XP", "XPToLevelUp", "HP", "Chakra", "Max Chakra", "Attack", "Magic", "Luck"
                    containing integer values, "Goal achieved" containing a boolean, and "Jutsu" containing
                    a dictionary object.
    :post-condition: Evaluate if the key "Goal Achieved" in the character dictionary object contains a boolean value,
                     True
    :return: a boolean value, True if the argument character dictionary object key "Goal Achieved" contains a boolean
             value of True
    """
    if character["Goal Achieved"]:
        return True


def game():
    """
        Drive the game.
    """
    rows = 10
    columns = 10
    board = generate_game_board(rows, columns)
    game_introduction()
    character = make_character(input("What is your name fellow shinobi?\n"))
    describe_current_location(character)
    achieved_goal = False
    while not achieved_goal:
        direction = get_user_choice()
        valid_move = validate_move(board, character, direction)
        if valid_move:
            move_character(character, direction)
            describe_current_location(character)
            execute_event_protocol(character, check_for_event(board, character))
            if game_over(character):
                break
            if character_has_leveled(character):
                assign_experience(character)
                assign_stats(character)
                execute_character_glow_up(character)
            achieved_goal = check_if_goal_attained(character)
    execute_victory()



def main():
    game()


if __name__ == '__main__':
    main()
