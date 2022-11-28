def make_character(character_name: str):
    character = {"Name": character_name, "X": 0, "Y": 0, "Level": 1,"XP": 0, "XPToLevelUp": 100, "XP": 0,
                 "HP": 150, "Max HP": 150, "Attack": 10, "Defense": 8, "Magic": 11, "Luck": 2}
    return character


combat_stats = {"stats": [{"HP": 150}, {"Max HP": 150}, {"Attack": 10}, {"Defense": 8}, {"Magic": 11}, {"Luck": 2}]}