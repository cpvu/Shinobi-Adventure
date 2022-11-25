import random
import time

def assignStatus(stats, character):
   pass

def levelUp(character):
    character["Level"] += 1
    character["HP"] += 50
    character["Attack"] += 25

def generate_monster(character):
    if character["Level"] == 1:
        level_one_monsters = [{"name": "Bird", "HP": 100, "MaxHP": 100, "Attack": 5, "XP": 40},
                   {"name": "Raven", "HP": 60, "MaxHP": 100, "Attack": 10, "XP": 35},
                   {"name": "Chicken", "HP": 80, "MaxHP": 100, "Attack": 7, "XP": 60}]

        battle_monster = level_one_monsters[random.randint(0, 2)]

    if character["Level"] == 2:
        level_two_monsters = [{"name": "Bird", "HP": 150, "Attack": 5, "XP": 40},
                              {"name": "Raven", "HP": 100, "Attack": 10, "XP": 35},
                              {"name": "Chicken", "HP": 200, "Attack": 7, "XP": 60}]

        battle_monster = level_one_monsters[random.randint(0, 2)]

    if character["Level"] == 3:
        level_three_monsters = [{"name": "Bird", "HP": 100, "MaxHP": 100, "Attack": 5},
                              {"name": "Raven", "HP": 60, "Attack": 10},
                              {"name": "Chicken", "HP": 80, "Attack": 7}]
        battle_monster = level_one_monsters[random.randint(0, 2)]
    return battle_monster


def battle(character, monster):
    while character["HP"] > 0 and monster["HP"] > 0:
        character_attack = random.randint(0, 10) + character["Attack"]
        monster_attack = random.randint(0, 5) + monster["Attack"]

        print(f"You inflicted {character_attack} damage with a great slash!")
        character["HP"] -= monster_attack
        print(f'The {monster["name"]} flaps you for {monster_attack} damage!')
        print(f'{monster["HP"]}/{monster["MaxHP"]}HP')
        monster["HP"] -= character_attack

        time.sleep(1)

    if monster["HP"] <= 0:
        battle_experience = monster["XP"] + random.randint(1, 10)
        character["XP"] += battle_experience
        print("The foe has been vanquished!")
        print(f"You have gained {battle_experience}!")


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

