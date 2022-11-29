import random


def character_has_leveled(character):
    if character["XP"] >= character["XPToLevelUp"]:
        return True

def get_character_stats(stat):
    combat_stats = ["Max HP", "Attack", "Defense", "Magic", "Luck"]
    if stat in combat_stats:
        return stat


def assign_stats(character):
    combat_stats = ["Max HP", "Attack", "Defense", "Magic", "Luck"]

    for stat in combat_stats:
        if stat == "Max HP":
            character[stat] += random.randint(50, 75)
        else:
            character[stat] += random.randint(3, 8)

def assign_experience(character):
    remaining_experience = character["XP"] - character["XPToLevelUp"]

    character["Level"] += 1
    character["XP"] = remaining_experience
    character["XPToLevelUp"] += 150

    print(f"\t \t \t Congratulations, you are now Level {character['Level']}!")



def execute_character_glow_up():
    print("""            ██╗░░░░░███████╗██╗░░░██╗███████╗██╗░░░░░  ██╗░░░██╗██████╗░
            ██║░░░░░██╔════╝██║░░░██║██╔════╝██║░░░░░  ██║░░░██║██╔══██╗
            ██║░░░░░█████╗░░╚██╗░██╔╝█████╗░░██║░░░░░  ██║░░░██║██████╔╝
            ██║░░░░░██╔══╝░░░╚████╔╝░██╔══╝░░██║░░░░░  ██║░░░██║██╔═══╝░
            ███████╗███████╗░░╚██╔╝░░███████╗███████╗  ╚██████╔╝██║░░░░░
            ╚══════╝╚══════╝░░░╚═╝░░░╚══════╝╚══════╝  ░╚═════╝░╚═╝░░░░░""")
