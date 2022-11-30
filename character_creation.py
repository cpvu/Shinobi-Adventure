def make_character(character_name: str):
    character = {"Name": character_name, "X": 0, "Y": 0, "Level": 1, "XP": 0, "XPToLevelUp": 100,
                 "HP": 200, "Max HP": 200, "Attack": 20, "Defense": 8, "Magic": 11, "Luck": 2,
                 "Jutsu": {"Katon": [22, "Unleash a fiery blast of chakra!"]}}
    return character

