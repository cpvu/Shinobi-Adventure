import random


def generate_room_type():
    """
    Generate a random number corresponding to a string value representing a room type in the game board.

    :post-condition: Return a string value, "Empty Room" if the random number generated is greater than or equal to 0
                     and less than 45
    :post-condition: Return a string value, "Treasure Room" if the random number generated is greater than or equal to
                     45 and less than 59.
    :post-condition: Return a string value, "Monster Room" if the random number generated is greater than or equal to
                     60 and less than or equal to 100
    :return: a string value, representing an empty room on the game board
    :return: a string value, representing a treasure room on the game board
    :return: a string value, representing a monster room on the game board
    """
    random_number = random.randint(0, 100)
    if 0 <= random_number < 45:
        return "Empty Room"
    elif 45 <= random_number < 59:
        return "Game Event"
    else:
        return "Monster Battle"


def generate_game_board(row, column):
    """
    Generate a dictionary object with key value pairs representing the coordinates of the game board.

    :param row: an integer value
    :param column: an integer value
    :pre-condition: row must be an integer value greater than 0
    :pre-condition: column must be an integer value greater than 0
    :post-condition: generate a dictionary object with key pair values that represent the game board
    :return: a dictionary object, representing the game board
    """
    board = {(k, v): generate_room_type() for k in range(row) for v in range(column)}
    board[(0, 0)] = "Empty Room"
    board[(9, 9)] = "Boss room"
    board[(2, 2)] = "Health room"
    board[(2, 7)] = "Health room"
    board[(7, 2)] = "Health room"
    board[(7, 7)] = "Health room"
    board[(5, 5)] = "Elite room"

    return board

