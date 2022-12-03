"""
Calvin Vu
A01291758

Hanxiao Mao
A01293003

Contains functions for healing room event.
"""
import time


def check_health_and_chakra_max(character: dict):
    """
    Re-assign character health and chakra to the character's current Max HP/Max Chakra.

    :param character: a dictionary object
    :pre-condition: character must be a dictionary object containing key values: "Name" containing a string, X", "Y",
                   "Level", "XP", "XPToLevelUp", "HP", "Chakra", "Max Chakra", "Attack", "Magic", "Luck"
                   containing integer values, and  "Jutsu" containing a dictionary object.
    :post-condition: Re-assign character's Max HP or Max Chakra to current HP or Chakra respectively if their values
                     are greater than the latter.
    """
    if character["HP"] > character["Max HP"]:
        character["HP"] = character["Max HP"]
    if character["Chakra"] > character["Max Chakra"]:
        character["Chakra"] = character["Max Chakra"]


def execute_health_room(character: dict):
    """
    :param character: a dictionary object
    :pre-condition: character must be a dictionary object containing key values: "Name" containing a string, X", "Y",
                   "Level", "XP", "XPToLevelUp", "HP", "Chakra", "Max Chakra", "Attack", "Magic", "Luck"
                   containing integer values, and  "Jutsu" containing a dictionary object.
    :post-condition: Executes a game event to restore the characters healthy by re-assigning the character object's
                    "Max HP" and "Max Chakra" key value pairs to "HP" and "Chakra" key value pairs respectively
    """
    print("Sakura The Healer: Take a break fellow shinobi. Let me heal your wounds.\n")
    time.sleep(0.5)
    print("The shinobi healing casted a healing light onto your wounds to restore your health and chakra.")
    time.sleep(0.5)
    character["HP"] = character["Max HP"]
    character["Chakra"] = character["Max Chakra"]
    print("Ah your Health and chakra are fully recovery now!")
    print(f'{character["Name"]} - HP: {character["HP"]}/{character["Max HP"]} Chakra:{character["Chakra"]}/'
          f'{character["Max Chakra"]}')
    check_health_and_chakra_max(character)
