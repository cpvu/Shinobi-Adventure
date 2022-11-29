import random
import json
import time


def generate_monster(character):
    with open("monsters/monsters.json") as fileobject:
        all_monsters = json.load(fileobject)

        if character["Level"] == 1:
            return all_monsters[random.randint(0, 2)]
        elif character["Level"] == 2:
            return all_monsters[random.randint(0, 5)]
        elif character["Level"] == 3:
            return all_monsters[random.randint(0, 8)]


def experience(character, monster_xp):
    character["XP"] += monster_xp
    print(f"You have gained {monster_xp} experience!")


def battle(character,  monster):
    while character["HP"] > 0 and monster["HP"] > 0:
        character_attack = random.randint(0, 10) + character["Attack"]
        monster_attack = random.randint(0, 5) + monster["Attack"]

        print(f"You inflicted {character_attack} damage with a great slash!")
        character["HP"] -= monster_attack
        print(f'The {monster["name"]} flaps you for {monster_attack} damage!')
        print(f'{monster["name"]}:{monster["HP"]}/{monster["MaxHP"]}HP')
        print(f'{character["Name"]}: {character["HP"]}/{character["Max HP"]}')
        monster["HP"] -= character_attack

        time.sleep(1)

    if monster["HP"] <= 0:
        print("The foe has been vanquished!")
        experience(character, monster["XP"])

    if character["HP"] < 0:
        print("You have died...")
        print("Game over, please try again")


"""
def execute_challenge_protocol(character, event):
    if event == "Monster Room":
        monster = generate_monster()
        battle(character, monster)
    elif event == "Treasure":
        type_of_event = treasureEvent()
        if type_of_event == "good"
            treasure_EventGood(character)
        elif type_of_event == "bad":
            treasureEventBad()
            
"""
