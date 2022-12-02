def printing_map(character):
    """
         Print the game board.

         :param character: a dictionary object
         :pre-condition: character must be a dictionary object containing key pair values relevant to the character's
                         name, current coordinates relative to the game board, combat stats, and abilities.
         :post-condition: Print the default game map for a 10 by 10 board.
    """
    default_map = ["+ + + + + + + + + B", "+ + + + + + + + + +", "+ + H + + + + H + +", "+ + + + + + + + + +",
                   "+ + + + + + + + + +", "+ + + + + M + + + +", "+ + + + + + + + + +", "+ + H + + + + H + +",
                   "+ + + + + + + + + +", "+ + + + + + + + + +"]
    current_map = default_map[:]
    target_row = current_map[9 - character["Y"]].split(' ')
    target_row[character["X"]] = 'U'
    current_map[9 - character["Y"]] = " ".join(target_row)
    for line in current_map:
        print(line)


def describe_current_location(character):
    """
         Print the character's current coordinates and game board.

         :param character: a dictionary object
         :pre-condition: character must be a dictionary object containing key pair values relevant to the character's
                         name, current coordinates relative to the game board, combat stats, and abilities.
         :post-condition: Print the values stored in the key "X" and "Y" of the character object
         :post-condition: Print the game board with the character's corresponding location
     """
    # we should return the whole board as a map?
    print(f"X: {character['X']},Y: {character['Y']}")
    printing_map(character)


def get_user_choice():
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