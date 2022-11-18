"""
Calvin Vu
A01291758

Hanxiao Mao
A01293003
"""


def make_board(row: int, column: int):
    pass


def make_character(str: str):
    pass


def describe_current_location(board, character):
    pass


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
