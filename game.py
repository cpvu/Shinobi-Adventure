"""
Calvin Vu
A01291758

Hanxiao Mao
A01293003
"""
import time
from makeboard import make_board
from battle import generate_monster, execute_battle_protocol
from treasureroom import execute_treasure_event
from character_creation import make_character
from character_location import describe_current_location, get_user_choice, validate_move, move_character
from level_up import character_has_leveled, execute_character_glow_up, assign_experience, assign_stats

def game_introduction():
    print(" ____ _  _ _ _  _ ____ ___  _ \n"
          " [__  |__| | |\ | |  | |__] | \n"
          " ___] |  | | | \| |__| |__] | \n")
    time.sleep(2)
    print("Welcome to the world of Shinobi, the land of ninjas and ninjitsu.")
    time.sleep(2)
    print("Chakra is the core of the power of ninjitsu and using powerful jutsus.")
    time.sleep(2)
    print("You're not from this world?")
    time.sleep(2)
    print("This world is a little bit different from where you came from...")
    time.sleep(2)
    print("The world needs your help to defeat Madara Uchiha.")
    time.sleep(2)
    print("Madara Uchiha is trying to put the world of Shinobi into an infinite dream state called "
          "the Infinite Tsukuyomi.")
    time.sleep(2)
    print("I sense you have immense chakra, but you must first traverse through this land to "
          "gain more power and jutsus.\n")
    time.sleep(2)


def game_over(character):
    if character["HP"] < 0:
        print("You have died...")
        print("Game over, please try again")
        return True
    return False


def check_for_event(board, character):
    if board[(character["X"], character["Y"])] == "Treasure Room":
        return "Treasure"
    elif board[(character["X"], character["Y"])] == "Monster Room":
        return "Battle"
    elif board[(character["X"], character["Y"])] == "Health room":
        return "Health room"
    else:
        return "Empty Room"


def execute_event_protocol(character, event):
    if event == "Battle":
        monster = generate_monster(character)
        print(f"A {monster['name']} has appeared before you!")
        execute_battle_protocol(character, monster)
    elif event == "Treasure":
        execute_treasure_event(character)
    elif event == "Health Room":
        execute_treasure_event(character)
    else:
        print("You've entered an empty room. There appears to be nothing in here..")
        return


def check_if_goal_attained(board, character):
    pass


def game():
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
            achieved_goal = check_if_goal_attained(board, character)
        else:
            # do something here if the move is not valid
            pass


def main():
    game()


if __name__ == '__main__':
    main()
