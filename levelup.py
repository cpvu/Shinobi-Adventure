import random


def assign_stats(stats):
    key_item = list(stats.keys())
    if key_item[0] == "Max HP":
        stats[key_item[0]] += random.randint(50, 75)
    else:
        stats[key_item[0]] += random.randint(0, 6)
    return stats


def character_has_leveled(character):
    if character["XP"] >= character["XPToLevelUp"]:
        return True


def main():
    combat_stats = [{"HP": 100}, {"Max HP": 100}, {"Attack": 10}, {"Defense": 8}, {"Magic": 11}, {"Luck": 2}]
    character = {"Name": "Calvin", "X": 0, "Y": 0, "Level": 1, "XP": 150, "XPToLevelUp": 100,
                 "stats": combat_stats}

    if character_has_leveled(character):
        print("Level up!")
        combat_stats = list(map(assign_stats, combat_stats))


if __name__ == '__main__':
    main()