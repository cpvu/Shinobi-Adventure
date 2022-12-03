"""
Calvin Vu
A01291758

Hanxiao Mao
A01293003

Contains functions for leveling up the character.
"""


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

    >>> test_character = {"XP": 105 , "XPToLevelUp": 100, "Level": 2}
    >>> character_has_leveled(test_character)
    True

    >>> test_character = {"XP": 90 , "XPToLevelUp": 100, "Level": 1}
    >>> character_has_leveled(test_character)


    >>> test_character = {"XP": 100 , "XPToLevelUp": 100, "Level": 1}
    >>> character_has_leveled(test_character)
    True

    >>> test_character = {"XP": 120 , "XPToLevelUp": 100, "Level": 3}
    >>> character_has_leveled(test_character)
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

    def map_stats(stat_key, stat_value):
        """
        Increase the stat_value by 30 percent for the stat_key in combat_stats.

        :param stat_key: a dictionary key
        :param stat_value: a dictionary value
        :precondition: stat_key must be string
        :precondition: stat_value must be integer
        :post condition: increase stat_key by 30 percent for the stat_key in combat_stats
        :return: stat_key, stat_value as tuple object
        """
        if stat_key in combat_stats:
            stat_value *= 1.3
            stat_value = int(stat_value)
        return stat_key, stat_value

    for key, value in map(map_stats, character.keys(), character.values()):
        character[key] = value


def assign_experience(character):
    """
    Assign an increase in level and adjust experience to character dictionary object.

    :param character: a dictionary object
    :pre-condition: character must be a dictionary object containing key values: "Name" containing a string, X", "Y",
                   "Level", "XP", "XPToLevelUp", "HP", "Chakra", "Max Chakra", "Attack", "Magic", "Luck"
                   containing integer values, and  "Jutsu" containing a dictionary object.
    :pre-condition: character "XP" key value must be greater than "XPToLevelUp" key value
    :pre-condition: character "Level" key value must be less than 3
    :post-condition: Assign an increase in level and the appropriate amount of current experience for the new level
                     and the next level
    """
    remaining_experience = character["XP"] - character["XPToLevelUp"]

    character["Level"] += 1
    character["XP"] = remaining_experience
    character["XPToLevelUp"] += (character["XPToLevelUp"] / 2 + 100)


def execute_character_glow_up(character):
    """
    Execute character level up protocol.

    :param character: a dictionary object
    :pre-condition: character must be a dictionary object containing key values: "Name" containing a string, X", "Y",
                   "Level", "XP", "XPToLevelUp", "HP", "Chakra", "Max Chakra", "Attack", "Magic", "Luck"
                   containing integer values, and  "Jutsu" containing a dictionary object.
    :post-condition: Print a level up ASCII art and level up statement.
    """
    print(f"\t \t \t Congratulations, you are now Level {character['Level']}!")

    print("""            ██╗░░░░░███████╗██╗░░░██╗███████╗██╗░░░░░  ██╗░░░██╗██████╗░
            ██║░░░░░██╔════╝██║░░░██║██╔════╝██║░░░░░  ██║░░░██║██╔══██╗
            ██║░░░░░█████╗░░╚██╗░██╔╝█████╗░░██║░░░░░  ██║░░░██║██████╔╝
            ██║░░░░░██╔══╝░░░╚████╔╝░██╔══╝░░██║░░░░░  ██║░░░██║██╔═══╝░
            ███████╗███████╗░░╚██╔╝░░███████╗███████╗  ╚██████╔╝██║░░░░░
            ╚══════╝╚══════╝░░░╚═╝░░░╚══════╝╚══════╝  ░╚═════╝░╚═╝░░░░░""")
