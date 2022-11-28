import random


def character_has_leveled(character):
    if character["XP"] >= character["XPToLevelUp"]:
        return True


def assign_stats(stat_name, stat_value):
    if stat_name == "Max HP":
        stat_gain = random.randint(50, 75)
        new_stat = stat_gain + stat_value
    else:
        stat_gain = random.randint(2, 10)
        new_stat = stat_gain + stat_value
    return new_stat


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
