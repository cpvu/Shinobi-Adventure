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
    character["Health"] = character["Max HP"]
    character["Chakra"] = character["Max Chakra"]
    print("Ah your Health and chakra are fully recovery now!")
    print(f'{character["Name"]} - HP: {character["HP"]}/{character["Max HP"]} Chakra:{character["Chakra"]}/'
          f'{character["Max Chakra"]}')

    check_health_and_chakra_max(character)
