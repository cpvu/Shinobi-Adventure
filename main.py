"""
Calvin Vu
A01291758

Hanxiao Mao
A01293003
"""
from makeboard import make_board
from battle import generate_monster, battle
from treasureroom import execute_treasure_event
from character_creation import make_character
from character_location import describe_current_location, get_user_choice, validate_move, move_character
from levelup import character_has_leveled, execute_character_glow_up, assign_experience, assign_stats


def check_for_event(board, character):
    if board[(character["X"], character["Y"])] == "Treasure Room":
        return "Treasure"
    elif board[(character["X"], character["Y"])] == "Monster Room":
        return "Battle"
    else:
        return "Empty Room"


def execute_event_protocol(character, event):
    if event == "Battle":
        monster = generate_monster(character)
        battle(character, monster)
    elif event == "Treasure":
        execute_treasure_event(character)
    else:
        print("An empty room")
        return


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
            execute_event_protocol(character, check_for_event(board, character))
            if character["HP"] < 0:
                break
            if character_has_leveled(character):
                execute_character_glow_up()
            achieved_goal = check_if_goal_attained(board, character)
        else:
            # do something here if the move is not valid
            pass


def main():
    game()


if __name__ == '__main__':
    main()
