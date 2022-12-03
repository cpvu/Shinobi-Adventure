def make_character(character_name: str):
    character = {"Name": character_name,
                 "X": 5,
                 "Y": 4,
                 "Level": 1,
                 "XP": 0,
                 "XPToLevelUp": 100,
                 "HP": 200,
                 "Max HP": 200,
                 "Chakra": 100,
                 "Max Chakra": 100,
                 "Attack": 100,
                 "Magic": 11,
                 "Luck": 2,
                 "Goal Achieved": False,
                 "Jutsu": {("Katon", "Unleash a fiery blast of chakra!", "A powerful fire blast"): 22}}
    return character
