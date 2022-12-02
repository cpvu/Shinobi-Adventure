import time


def check_health_and_chakra_max(character):
    if character["HP"] > character["Max HP"]:
        character["HP"] = character["Max HP"]
    if character["Chakra"] > character["Max Chakra"]:
        character["Chakra"] = character["Max Chakra"]


def execute_health_room(character):
    print("Sakura The Healer: Take a break fellow shinobi. Let me heal your wounds.\n")
    time.sleep(0.5)
    print("The shinobi healing casted a healing light onto your wounds to restore your health and chakra.")
    time.sleep(0.5)
    if character["HP"] < character["Max HP"]:
        character["Health"] += 25
        print("You have healed for 25 HP")
    else:
        print("Ah your is Health is already full!")

    if character["Chakra"] < character["Max Chakra"]:
        character["Chakra"] += 25
        print("You've gained 25 chakra!")
    else:
        print("Amazing, your chakra is already at full!")

    check_health_and_chakra_max(character)
