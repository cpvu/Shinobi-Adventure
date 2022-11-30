"""
Calvin Vu
A01291758

Hanxiao Mao
A01293003
"""
from makeboard import make_board
from battle import generate_monster, display_battle_menu, battle
from treasureroom import execute_treasure_event
from character_creation import make_character
from character_location import describe_current_location, get_user_choice, validate_move, move_character
from level_up import character_has_leveled, execute_character_glow_up, assign_experience, assign_stats


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
    else:
        return "Empty Room"


def execute_event_protocol(character, event):
    if event == "Battle":
        monster = generate_monster(character)
        print(f"A {monster['name']} has appeared before you!")
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
    describe_current_location(character)
    achieved_goal = False
    while not achieved_goal:
        # prompt the current location
        # describe_current_location(board, character)
        print(character)
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
