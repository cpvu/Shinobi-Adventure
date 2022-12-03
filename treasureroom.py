"""
Calvin Vu
A01291758

Hanxiao Mao
A01293003
"""
import random
import time
from battle import generate_monster, execute_battle_protocol


def generate_jutsu():
    with open("monsters/jutsus.txt") as fileobject:
        all_jutsus = []
        for line in fileobject.readlines():
            jutsu_pair = line.strip().split(',')
            all_jutsus.append((jutsu_pair[0], jutsu_pair[1], jutsu_pair[2]))
        return all_jutsus[random.randint(0, len(all_jutsus) - 1)]


def assign_jutsu(character, jutsu):
    character["Jutsu"][jutsu] = random.randint(25, 60)
    print(f"You have gained a new Jutsu, {jutsu[0]}")


def open_sacred_scroll(character: dict):
    print("You enter the room")
    print("A sacred ninja art scroll lays bare on the floor, upon touching it you feel a new power flow into you..")
    time.sleep(1)
    new_jutsu = generate_jutsu()
    if new_jutsu in character["Jutsu"]:
        print("You already have this jutsu.. better luck next time.")

    assign_jutsu(character, new_jutsu)


def treasure_chest_battle(character: dict):
    print("A enemy appears before you... defeat it to get the treasure")
    treasure_room_monster = generate_monster(character)
    execute_battle_protocol(character, treasure_room_monster)


def neutral_event():
    print("You open the chest.. but theres nothing inside. Better luck next time!")
    time.sleep(1)


def treasure_chest_poisin_gas(character):
    print("You enter the room...")
    time.sleep(1)
    print("You open the chest.")
    gas_damage = random.randint(0, 10)
    character["HP"] -= gas_damage
    print(f"The chest releases a poisonous gas and inflicts {gas_damage} to you.")


def jackpot_event(character):
    print("You enter the room...")
    time.sleep(1)
    print("A beam of light strikes through your eyes. A voice echoes.. the mangekyou sharingan is now yours.")
    print("You feel an unknown power surge within you. See your power in your next battle..")
    character["Attack"] += 25
    character["Magic"] += 25


def execute_treasure_event(character):
    random_number = random.randint(0, 100)
    if 33 >= random_number >= 0:
        return open_sacred_scroll(character)
    elif 66 >= random_number > 33:
        return treasure_chest_battle(character)
    elif 85 >= random_number > 66:
        return neutral_event()
    elif 99 >= random_number > 86:
        return treasure_chest_poisin_gas(character)
    elif random_number == 100:
        return jackpot_event(character)
