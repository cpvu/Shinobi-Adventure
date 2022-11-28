import random


def assign_stats(stat_name, stat_value):
    if stat_name == "Max HP":
        stat_gain = random.randint(50, 75)
        #print(f"\t \t \t {key_item[0]}: {stats[key_item[0]]} + {stat_gain } = {stats[key_item[0]] + stat_gain}")
        new_stat = stat_gain + stat_value
    else:
        stat_gain = random.randint(2, 10)
        #print(f"\t \t \t {key_item[0]}: {stats[key_item[0]]} + {stat_gain} = {stats[key_item[0]] + stat_gain}")
        new_stat = stat_gain + stat_value
    return new_stat


def assign_experience(character):
    remaining_experience = character["XP"] - character["XPToLevelUp"]

    character["Level"] += 1
    character["XP"] = remaining_experience
    character["XPToLevelUp"] += 150

    print(f"\t \t \t Congratulations, you are now Level {character['Level']}!")


def character_has_leveled(character):
    if character[0]["XP"] >= character[0]["XPToLevelUp"]:
        return True

def execute_character_glow_up():
    print("""            ██╗░░░░░███████╗██╗░░░██╗███████╗██╗░░░░░  ██╗░░░██╗██████╗░
            ██║░░░░░██╔════╝██║░░░██║██╔════╝██║░░░░░  ██║░░░██║██╔══██╗
            ██║░░░░░█████╗░░╚██╗░██╔╝█████╗░░██║░░░░░  ██║░░░██║██████╔╝
            ██║░░░░░██╔══╝░░░╚████╔╝░██╔══╝░░██║░░░░░  ██║░░░██║██╔═══╝░
            ███████╗███████╗░░╚██╔╝░░███████╗███████╗  ╚██████╔╝██║░░░░░
            ╚══════╝╚══════╝░░░╚═╝░░░╚══════╝╚══════╝  ░╚═════╝░╚═╝░░░░░""")


def main():
    count = 0
    character = {"Name": "Calvin", "X": 0, "Y": 0, "Level": 1, "XP": 101, "XPToLevelUp": 100,
                 "stats": [{"HP": 100}, {"Max HP": 100}, {"Attack": 10}, {"Defense": 8}, {"Magic": 11}, {"Luck": 2}]}
    while count < 10:
        character["XP"] += 100

        if character_has_leveled(character):
            execute_character_glow_up()
            assign_experience(character)
            print(f"\t \t \t Congratulations, you are now Level {character['Level']}!")
            character[1]["stats"] = list(map(assign_stats, character[1]["stats"]))


        count += 1



if __name__ == '__main__':
    main()