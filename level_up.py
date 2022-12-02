import random


def character_has_leveled(character):
    if character["XP"] >= character["XPToLevelUp"] and character["Level"] < 3:
        return True


def assign_stats(character):
    combat_stats = ["Max HP", "HP", "Attack", "Defense", "Magic"]

    def map_level_up(key, value):
        if key in combat_stats:
            value *= 1.3
            value = int(value)
        return key, value

    for k, v in map(map_level_up, character.keys(), character.values()):
        character[k] = v


def assign_experience(character):
    remaining_experience = character["XP"] - character["XPToLevelUp"]

    character["Level"] += 1
    character["XP"] = remaining_experience
    character["XPToLevelUp"] += (character["XP"] / 2 + 100)

    print(f"\t \t \t Congratulations, you are now Level {character['Level']}!")


def execute_character_glow_up():
    print("""            ██╗░░░░░███████╗██╗░░░██╗███████╗██╗░░░░░  ██╗░░░██╗██████╗░
            ██║░░░░░██╔════╝██║░░░██║██╔════╝██║░░░░░  ██║░░░██║██╔══██╗
            ██║░░░░░█████╗░░╚██╗░██╔╝█████╗░░██║░░░░░  ██║░░░██║██████╔╝
            ██║░░░░░██╔══╝░░░╚████╔╝░██╔══╝░░██║░░░░░  ██║░░░██║██╔═══╝░
            ███████╗███████╗░░╚██╔╝░░███████╗███████╗  ╚██████╔╝██║░░░░░
            ╚══════╝╚══════╝░░░╚═╝░░░╚══════╝╚══════╝  ░╚═════╝░╚═╝░░░░░""")
