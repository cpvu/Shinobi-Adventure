"""
Calvin Vu
A01291758

Hanxiao Mao
A01293003

Contains functions for character and board locations.
"""


def describe_current_location(character):
    """
    Print the game board.

    :param character: a dictionary object
    :pre-condition: character must be a dictionary object containing key values: "Name" containing a string, X",
                 "Y", "Level", "XP", "XPToLevelUp", "HP", "Chakra", "Max Chakra", "Attack", "Magic", "Luck"
                 containing integer values, "Goal achieved" containing a boolean, and "Jutsu" containing
                 a dictionary object.
    :post-condition: Print the default game map for a 10 by 10 board.
    """
    default_map = ["+ + + + + + + + + B", "+ + + + + + + + + +", "+ + H + + + + H + +", "+ + + + + + + + + +",
                   "+ + + + + E + + + +", "+ + + + + + + + + +", "+ + + + + + + + + +", "+ + H + + + + H + +",
                   "+ + + + + + + + + +", "+ + + + + + + + + +"]
    current_map = default_map[:]
    target_row = current_map[9 - character["Y"]].split(' ')
    target_row[character["X"]] = 'U'
    current_map[9 - character["Y"]] = " ".join(target_row)
    for line in current_map:
        print(line)


def get_user_choice():
    """
    Return the user choice for the direction that the character will move.

    :post-condition: print an enumerated statement containing the options for the character to move
    :post-condition: assign the inputted user choice to the corresponding direction as a string value
    :post-condition: print "Invalid input!" if the user choice does not correspond to a game direction
    :return: a string value, representing the direction corresponding to the chosen user input
    """
    directions = ["North", "West", "East", "South"]
    for direction_tuple in enumerate(directions, 1):
        print(f"{direction_tuple[0]}: {direction_tuple[1]}", end=" | ")
    user_choice = input("\nType 1 for moving North, 2 for moving East, 3 for moving West, 4 for moving South\n")
    while user_choice not in ['1', '2', '3', '4']:
        print("Invalid input!")
        user_choice = input("Type 1 for moving North, 2 for moving East, 3 for moving West, 4 for moving South\n")
    direction = {k: v for (k, v) in enumerate(directions, 1)}
    return direction[int(user_choice)]


def validate_move(board, character, direction):
    """
    Validate the user inputted direction on the game board.

    :param board: a dictionary object
    :param character: a dictionary object
    :param direction: a dictionary object
    :pre-condition: board must be a dictionary object containing key value pairs representing the game board
    :pre-condition: character must be a dictionary object containing key values: "Name" containing a string, X",
                     "Y", "Level", "XP", "XPToLevelUp", "HP", "Chakra", "Max Chakra", "Attack", "Magic", "Luck"
                     containing integer values, "Goal achieved" containing a boolean, and "Jutsu" containing
                     a dictionary object.
    :pre-condition: direction must be a string value containing "North", "South", "West", or "East
    :post-condition: Evaluate if the argument direction to a corresponding increase of an integer of one in the key
                     X or Y in character is in the board dictionary character
    :return: a boolean value, True if the direction and new character coordinate is valid in the board dictionary
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
        return False


def move_character(character, direction):
    """
    Evaluate the user inputted direction to generate the new character board coordinates.

    :param character: a dictionary object
    :param direction: a string object
    :pre-condition: character must be a dictionary object containing key values: "Name" containing a string, X",
                    "Y", "Level", "XP", "XPToLevelUp", "HP", "Chakra", "Max Chakra", "Attack", "Magic", "Luck"
                    containing integer values, "Goal achieved" containing a boolean, and "Jutsu" containing
                    a dictionary object.
    :pre-condition: direction must be a string value containing "North", "South", "West", or "East"
    :post-condition: Adjust the character key pair coordinate by an integer value of one that corresponds to the
                     argument direction
    :return: a string value, representing the direction corresponding to the chosen user input
    """
    if direction == "North":
        character["Y"] += 1
    elif direction == "South":
        character["Y"] -= 1
    elif direction == "East":
        character["X"] += 1
    elif direction == "West":
        character["X"] -= 1
