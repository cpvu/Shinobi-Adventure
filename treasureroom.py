"""
Calvin Vu
A01291758

Hanxiao Mao
A01293003
"""
import random
from battle import generate_monster, battle


def good_event(character):
    print("You open the chest...")
    print("Within are spoils of the war")


def bad_event(character):
    print("A enemy appears before you... defeat it to get the treasure")
    treasure_room_monster = generate_monster(character)
    battle(character, treasure_room_monster)


def neutral_event(character):
    print("You open the chest.. but theres nothing inside.")


def jackpot_event(character):
    pass


def execute_treasure_event(character):
    random_number = random.randint(0, 100)
    if 33 >= random_number >= 0:
        return good_event(character)
    elif 66 >= random_number > 33:
        return bad_event(character)
    elif 99 >= random_number > 66:
        return neutral_event(character)
    elif random_number == 100:
        return jackpot_event(character)




