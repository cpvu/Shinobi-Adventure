"""
Calvin Vu
A01291758

Hanxiao Mao
A01293003
"""
from makeboard import make_board

def make_character(character_name: str):
    character = {"Name": character_name, "X": 0, "Y": 0, "Level": 1, "XP": 0, "Current HP": 10, "Max HP": 100, "Attack": 10, "Luck": 0}
    return character


def describe_current_location(board, character)
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
    direction_check = {"North": board.get((character["X"], character["Y"] + 1), "Boundary"),
                       "East": board.get((character["X"] + 1, character["Y"]), "Boundary"),
                       "West": board.get((character["X"] - 1, character["Y"]), "Boundary"),
                       "South": board.get((character["X"], character["Y"] - 1), "Boundary")}
    if direction_check[direction] == "Boundary":
        print("The direction is not available!")
        return False
    else:
        return True


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


def check_for_challenge():
    # if
    pass


def execute_challenge_protocol(character):
    pass


def character_has_leveled():
    pass


def execute_glow_up_protocol():
    pass


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
            there_is_a_challenge = check_for_challenge()
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
