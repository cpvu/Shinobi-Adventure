"""
Calvin Vu
A01291758

Hanxiao Mao
A01293003
"""
import random
from battle import generate_monster, battle


def treasure_chest(character):
    print("You open the chest...")
    print("Within are spoils of the war")


def treasure_chest_battle(character):
    print("A enemy appears before you... defeat it to get the treasure")
    treasure_room_monster = generate_monster(character)
    battle(character, treasure_room_monster)


def neutral_event(character):
    print("You open the chest.. but theres nothing inside.")

def treasure_chest_poisin_gas(character):
    print("You enter the room...")
    print("You open the chest.")
    gas_damage = random.randint(0, 10)
    print(f"The chest releases a poisonous gas and inflicts {gas_damage} to you.")


def jackpot_event(character):
    print("You enter the room...")
    print("You open the chest.")
    character["Attack"] += 50
    print("You found the holy sword excalibur. A tremendous power boost.")


def execute_treasure_event(character):
    random_number = random.randint(0, 100)
    if 33 >= random_number >= 0:
        return treasure_chest(character)
    elif 66 >= random_number > 33:
        return treasure_chest_battle(character)
    elif 85 >= random_number > 66:
        return neutral_event(character)
    elif 99 >= random_number > 86:
        return treasure_chest_poisin_gas(character)
    elif random_number == 100:
        return jackpot_event(character)




