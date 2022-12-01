def make_character(character_name: str):
    character = {"Name": character_name, "X": 8, "Y": 8, "Level": 3, "XP": 0, "XPToLevelUp": 100,
                 "HP": 200, "Max HP": 200, "Chakra": 100, "Max Chakra": 100, "Attack": 20, "Defense": 8, "Magic": 11, "Luck": 2,
                 "Jutsu": {("Katon", "Unleash a fiery blast of chakra!"): 22}}
    return character

