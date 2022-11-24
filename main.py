"""
Calvin Vu
A01291758

Hanxiao Mao
A01293003
"""
import random

from makeboard import make_board


def make_character(character_name: str):
    character = {"Name": character_name, "X": 0, "Y": 0, "Level": 1, "XP": 0, "Current HP": 10, "Max HP": 100,
                 "Attack": 10, "Luck": 0}
    return character


def describe_current_location(board, character):
    # we should return the whole board as a map?
    print(f"X: {character['X']},Y: {character['Y']}")
    print("pretend this is a map")


def get_user_choice():
    directions = ["North", "East", "West", "South"]
    for direction_tuple in enumerate(directions, 1):
        print(f"{direction_tuple[0]}: {direction_tuple[1]}", end=" | ")
    user_choice = int(input("\nType 1 for moving North, 2 for moving East, 3 for moving West, 4 for moving South\n"))
    while user_choice not in [1, 2, 3, 4]:
        user_choice = int(input("Type 1 for moving North, 2 for moving East, 3 for moving West, 4 for moving South\n"))
    direction = {k: v for (k, v) in enumerate(directions, 1)}
    return direction[user_choice]


def validate_move(board, character, direction):
    """
    direction_check = {"North": board.get((character["X"], character["Y"] + 1), "Boundary"),
                       "East": board.get((character["X"] + 1, character["Y"]), "Boundary"),
                       "West": board.get((character["X"] - 1, character["Y"]), "Boundary"),
                       "South": board.get((character["X"], character["Y"] - 1), "Boundary")}
    if direction_check[direction] == "Boundary":
        print("The direction is not available!")
        return False
    else:
        return True
    """
    if direction == "North" and (character["X"], character["Y"] + 1) in board.keys():
        return True
    elif direction == "South" and (character["X"], character["Y"] - 1) in board.keys():
        return True
    elif direction == "West" and (character["X"] - 1, character["Y"]) in board.keys():
        return True
    elif direction == "East" and (character["X"] + 1, character["Y"]) in board.keys():
        return True
    else:
        print("Invalid action, you can't go that way!")

def move_character(character, direction):
    if direction == "North":
        character["Y"] += 1
    elif direction == "South":
        character["Y"] -= 1
    elif direction == "East":
        character["X"] += 1
    elif direction == "West":
        character["X"] -= 1
    else:
        print('Something wrong')

# def generate_monster(character):
    #if character["level"] == 1:
        monsters = [{"name": "Bird", "HP": 100, "Attack": 5}]
        #randomly choose a monster 
        #return whatever monster

# def battle_monster(character, monster):
    #Function roll for initiative (who goes first)
    #Roll for chance to attack/miss
    #battle monster
    #Check if monster is still alive

# Hit level 3 and then challenge. Roll a random number and from there is a chance to encounter a challenge.
def check_for_challenge(board, character):
    pass


def execute_challenge_protocol(character, board ):
    pass
    if board(character["X"], character["Y"]) == "Monster Room":
        battle_monster(character, generate_monster(character))


def character_has_leveled():
    pass

#Ascii art to show the level up of the character
def execute_glow_up_protocol():
    pass

#Check to see if goal is attained, killed a boss/reached level 3. Key value pair in the character called success: false
#switched to true if boss is killed
def check_if_goal_attained(board, character):
    pass


def game():
    rows = 10
    columns = 10
    board = make_board(rows, columns)
    character = make_character(input("Player Name?"))
    describe_current_location(board, character)
    achieved_goal = False
    while not achieved_goal:
        # prompt the current location
        # describe_current_location(board, character)
        direction = get_user_choice()
        valid_move = validate_move(board, character, direction)
        if valid_move:
            move_character(character, direction)
            describe_current_location(board, character)
            there_is_a_challenge = check_for_challenge(board, character)
            if there_is_a_challenge:
                execute_challenge_protocol(character)
                if character_has_leveled():
                    execute_glow_up_protocol()
            achieved_goal = check_if_goal_attained(board, character)
        else:
            # do something here if the move is not valid
            pass


def main():
    game()


if __name__ == '__main__':
    main()
