"""
Calvin Vu
A01291758

Hanxiao Mao
A01293003
"""
from makeboard import make_board


def make_character(character_name: str):
    character = {"Name": character_name, "X": 0, "Y": 0, "Current HP": 10, "Max HP": 10, "Attack": 1, "Luck": 0}
    return character


def describe_current_location(board, character):
    # not quite clear about this one, what should we return, x,y of current location? and maybe N/E/W/S?
    # or we should return the whole board as a map?
    north = board.get((character["X"], character["Y"] + 1), "Boundary")
    east = board.get((character["X"] + 1, character["Y"]), "Boundary")
    west = board.get((character["X"] - 1, character["Y"]), "Boundary")
    south = board.get((character["X"], character["Y"] - 1), "Boundary")
    print(f"\t\t\tNorth: {north}")
    print(f"West:{west}| Current:({character['X']},{character['Y']}) |East:{east}")
    print(f"\t\t\tSouth: {south}")


def get_user_choice():
    pass


def validate_move(board, character, direction):
    pass


def move_character(character):
    pass


def check_for_challenge():
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
        describe_current_location(board, character)
        direction = get_user_choice()
        valid_move = validate_move(board, character, direction)
        if valid_move:
            move_character(character)
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
