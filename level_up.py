def character_has_leveled(character):
    """
    Determine if character is ready to level.
    :param character: a dictionary object
    :pre-condition: character must be a dictionary object containing key values: "Name" containing a string, X", "Y",
                   "Level", "XP", "XPToLevelUp", "HP", "Chakra", "Max Chakra", "Attack", "Magic", "Luck"
                   containing integer values, "Goal achieved" containing a boolean, and "Jutsu" containing
                   a dictionary object.
    :post-condition: Return True if the value in the key "XP" is greater than the value in key "XPToLevelUp" and the
                    value in the key "Level" is less than 3 in the character dictionary object
    :return: Return True if the integer value in the key "XP" is greater than the integer value in the key "XPToLevelUp"
    """
    if character["XP"] >= character["XPToLevelUp"] and character["Level"] < 3:
        return True


def assign_stats(character):
    """
    Assign an increase in the character dictionary's combat related stats.

    :param character: a dictionary object
    :pre-condition: character must be a dictionary object containing key values: "Name" containing a string, X", "Y",
                   "Level", "XP", "XPToLevelUp", "HP", "Chakra", "Max Chakra", "Attack", "Magic", "Luck"
                   containing integer values, "Goal achieved" containing a boolean, and "Jutsu" containing
                   a dictionary object.
    :post-condition: Contains a sub function to map the relevant combat stats by a multiplier
    """
    combat_stats = ["Max HP", "HP", "Attack", "Magic", "Chakra", "Max Chakra"]

    def map_level_up(key, value):
        if key in combat_stats:
            value *= 1.3
            value = int(value)
        return key, value

    for k, v in map(map_level_up, character.keys(), character.values()):
        character[k] = v


def assign_experience(character):
    """
    Assign an increase in level and adjust experience to character dictionary object.

    :param character: a dictionary object
    :pre-condition: character must be a dictionary object containing key values: "Name" containing a string, X", "Y",
                   "Level", "XP", "XPToLevelUp", "HP", "Chakra", "Max Chakra", "Attack", "Magic", "Luck"
                   containing integer values, and  "Jutsu" containing a dictionary object.
    :post-condition: Assign an increase in level and the appropriate amount of current experience for the new level
                     and the next level
    """
    remaining_experience = character["XP"] - character["XPToLevelUp"]

    character["Level"] += 1
    character["XP"] = remaining_experience
    character["XPToLevelUp"] += (character["XP"] / 2 + 100)

    print(f"\t \t \t Congratulations, you are now Level {character['Level']}!")


def execute_character_glow_up():
    """
    Print level up ASCII art.

    :post-condition: Print a level up ASCII art.
    """
    print("""            ██╗░░░░░███████╗██╗░░░██╗███████╗██╗░░░░░  ██╗░░░██╗██████╗░
            ██║░░░░░██╔════╝██║░░░██║██╔════╝██║░░░░░  ██║░░░██║██╔══██╗
            ██║░░░░░█████╗░░╚██╗░██╔╝█████╗░░██║░░░░░  ██║░░░██║██████╔╝
            ██║░░░░░██╔══╝░░░╚████╔╝░██╔══╝░░██║░░░░░  ██║░░░██║██╔═══╝░
            ███████╗███████╗░░╚██╔╝░░███████╗███████╗  ╚██████╔╝██║░░░░░
            ╚══════╝╚══════╝░░░╚═╝░░░╚══════╝╚══════╝  ░╚═════╝░╚═╝░░░░░""")
