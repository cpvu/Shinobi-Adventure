"""
Calvin Vu
A01291758

Hanxiao Mao
A01293003
"""
import time
from makeboard import make_board
from battle import generate_monster, execute_battle_protocol, generate_boss, generate_elite
from treasureroom import execute_treasure_event
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
    time.sleep(0.2)
    print("Chakra is the core of the power of ninjitsu and using powerful jutsus.")
    time.sleep(0.2)
    print("You're not from this world?")
    time.sleep(0.2)
    print("This world is a little bit different from where you came from...")
    time.sleep(0.2)
    print("The world needs your help to defeat Madara Uchiha.")
    time.sleep(0.2)
    print("Madara Uchiha is trying to put the world of Shinobi into an infinite dream state called "
          "the Infinite Tsukuyomi.")
    time.sleep(0.2)
    print("I sense you have immense chakra, but you must first traverse through this land to "
          "gain more power and jutsus.\n")
    time.sleep(0.2)


def game_over(character):
    """
    Return True if the character's HP is below 0 or below.

    :param character: a dictionary object
    :pre-condition: character must be a dictionary object that represents the character of the game, specifically
                    containing a key value pair with a key of "HP" and value of integer.
    :post-condition: Evaluate the integer value for key "HP" in the dictionary object character and return True if
                     it is less than or equal to 0.
    return: a boolean value, True if the value of key "HP" in the argument dictioanry is less than or equal to 0
    """
    if character["HP"] <= 0:
        print("You have died...")
        print("Game over, please try again")
        return True
    return False


def check_for_event(board, character):
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
    if board[(character["X"], character["Y"])] == "Treasure Room":
        return "Treasure"
    elif board[(character["X"], character["Y"])] == "Monster Room":
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
    print("You've arrived to the the Uchiha Clan's dominion. He emits his powerful chakra and suddenly everything "
          "around him craters.")
    print("So.. you are the one. I heard of an unknown shinobi who travelled across this great land in hopes to defeat "
          "me.")
    print("I am Madara Uchiha and you will not stop me from casting this eternal dream state.")


def execute_event_protocol(character, event):
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
    elif event == "Treasure":
        execute_treasure_event(character)
    elif event == "Health":
        execute_health_room(character)
    elif event == "Boss":
        boss = generate_boss(character)
        if boss:
            display_final_boss_dialogue()
            execute_battle_protocol(character, boss)
            character["Goal Achieved"] = True
    elif event == "Elite":
        elite = generate_elite()
        print("Orochimaru is ready to fight you! No escape for boss fight!")
        execute_battle_protocol(character, elite)
    else:
        print("You've entered an empty room. There appears to be nothing in here..")
        return


def execute_victory():
    print("Its all over... I can't believe I did it.")
    print("Roars of victory yell out as the world witnessed your conquer.")
    print("It seems as though you are fading away and now its time to go back to your world...")

def check_if_goal_attained(character):
    if character["Goal Achieved"]:
        return True


def game():
    """
        Drive the game.
    """
    rows = 10
    columns = 10
    board = make_board(rows, columns)
    game_introduction()
    character = make_character(input("What is your name fellow shinobi?\n"))
    describe_current_location(character)
    achieved_goal = False
    while not achieved_goal:
        # prompt the current location
        # describe_current_location(board, character)
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
                execute_character_glow_up()
            achieved_goal = check_if_goal_attained(character)
        # else:
        #     # do something here if the move is not valid
        #     pass


def main():
    game()


if __name__ == '__main__':
    main()
