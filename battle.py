import random
import json
import time
import itertools
from health_room import check_health_and_chakra_max
from character_location import describe_current_location


def generate_elite_monster() -> dict:
    """
    Read and generate the elite monster from elite_monster.json file.

    :precondition: the elite monster information must store as an object in json file
    :post condition: read the elite monster information from json object and return it as dictionary
    :raises FileNotFoundError: if 'elite_monster.json' not exist or not exist in the 'monsters' directory
    :return: a dictionary store all the monster information
    >>> generate_elite_monster()
    {'name': 'Orochimaru', 'ability': [{'title': 'Attack', 'attack': 12}, {'title': 'Recovery', 'heal': 20}], \
'HP': 350, 'MaxHP': 350, 'XP': 100}
    """
    try:
        with open("monsters/elite_monster.json") as fileobject:
            elite_monster = json.load(fileobject)
    except FileNotFoundError:
        print(f"The file 'elite_monster.json' not exist or not in the monsters directory.")
    else:
        return elite_monster


def generate_boss_monster() -> dict:
    """
    Read and generate the boss from boss.json file.

    :precondition: boss information must store as an object in json file
    :post condition: read the boss information from json object and return it as dictionary
    :raises FileNotFoundError: if 'boss.json' not exist or not exist in the 'monsters' directory
    :return: a dictionary store all the boss information
    >>> generate_boss_monster()
    {'name': 'Madara Uchiha', 'ability': [{'title': 'Attack', 'attack': 12}, {'title': 'Susanoo', 'attack': 28}, \
{'title': 'Gunbai', 'attack': 20}, {'title': 'Recovery', 'heal': 20}], 'HP': 350, 'XP': 0}
    """
    try:
        with open("monsters/boss.json") as fileobject:
            boss = json.load(fileobject)
    except FileNotFoundError:
        print(f"The file 'boss.json' not exist or not in the monsters directory.")
    else:
        return boss


def generate_monster(character: dict) -> dict:
    """
    Read and generate a dictionary that contain a random monsters information from monsters.json file.

    :param character: a dictionary that must have a "Level" key, value must between [1, 3]
    :precondition: monsters information must store as objects in an array in json file
    :post condition: return a dictionary that store a random monster information in 'monsters.json' file according to
                     the character "Level" value
    :raises FileNotFoundError: if 'monsters.json' not exist or not exist in the 'monsters' directory
    :return: a dictionary that contain a random monster information in 'monsters.json' file
    """
    try:
        with open("monsters/monsters.json") as fileobject:
            all_monsters = json.load(fileobject)
    except FileNotFoundError:
        print(f"The file 'monsters.json' not exist or not in the monsters directory.")
    else:
        if character["Level"] == 1:
            return all_monsters[random.randint(0, 2)]
        elif character["Level"] == 2:
            return all_monsters[random.randint(0, 5)]
        elif character["Level"] == 3:
            return all_monsters[random.randint(0, 8)]


def experience(character: dict, monster_xp: int):
    """
    Add monster_xp to the value of "XP" key in character and print relevant information.

    :param character: a dictionary that contain an "XP" key, type of the value of "XP" key is integer
    :param monster_xp: a positive integer
    :precondition: character must be a dictionary that contain at least an "XP" key, the value of "XP" key must be a
                   positive integer
    :precondition: monster_xp must be a positive integer
    :post condition: Add monster_xp to the value of "XP" key in character and print the experience gained
    """
    character["XP"] += monster_xp
    time.sleep(0.5)
    print(f"You have gained {monster_xp} experience!")


def display_battle_menu():
    """
    Print "Attack", "Jutsu", "Heal", "Flee" as enumeration with numbers that start from 1.

    :precondition: no precondition
    :post condition:  print "Attack", "Jutsu", "Heal", "Flee" as enumeration with numbers that start from 1
    """
    combat_options = ("Attack", "Jutsu", "Heal", "Flee")

    for battle_options in enumerate(combat_options, 1):
        print(f"{battle_options[0]} - {battle_options[1]}")


def display_jutsu(character: dict):
    """

    :param character:
    :return:
    """
    jutsu_selection = [key for key in character["Jutsu"].keys()]
    jutsu_numbers = []
    for jutsu in enumerate(jutsu_selection, 1):
        print(f"{jutsu[0]} - {jutsu[1][0]} - {jutsu[1][2]}")
        jutsu_numbers.append(str(jutsu[0]))
    return jutsu_numbers, jutsu_selection


def get_jutsu_choice(character):
    jutsu_numbers_and_selection = display_jutsu(character)
    jutsu_choice = (input("Select your jutsu or enter q to go back"))
    if jutsu_choice == 'q':
        return 'q'
    while jutsu_choice not in jutsu_numbers_and_selection[0]:
        print("Invalid input")
        jutsu_choice = (input("Select your jutsu or enter q to go back"))
        if jutsu_choice == 'q':
            return 'q'

    return jutsu_numbers_and_selection[1][int(jutsu_choice) - 1]


def display_battle_hp(character, monster):
    """
    Print the monster name and HP, character Name, current HP, current Chakra.

    :param character: a dictionary have "Name", "HP", "Max HP", "Chakra", "Max Chakra" as keys
    :param monster: a dictionary have "name", "HP" as keys
    :precondition: character must be a dictionary that contain "Name", "HP", "Max HP", "Chakra", "Max Chakra" as keys
    :precondition: monster must be a dictionary have "name", "HP" as keys
    :post condition: print the monster name and HP, character Name, current HP, current Chakra.
    """
    print(f'{monster["name"]} - HP:{monster["HP"]}HP')
    print(f'{character["Name"]} - HP: {character["HP"]}/{character["Max HP"]} Chakra:{character["Chakra"]}/'
          f'{character["Max Chakra"]}')


def monster_damage_sequence(character, monster):
    monster_attacks_sequence = itertools.cycle(monster["ability"])
    monster_attack = next(monster_attacks_sequence)
    if monster_attack["title"] == "Recovery":
        print(f'{monster["name"]} use {monster_attack["title"]} and heal himself {monster_attack["heal"]} point HP')
        monster["HP"] += 20
    else:
        current_attack = random.randint(0, 3) + monster_attack["attack"]
        print(f'{monster["name"]} use {monster_attack["title"]} and cause {current_attack} damage!')
        time.sleep(0.5)
        character["HP"] -= current_attack


def character_damage_sequence(character, monster, character_attack="slice"):
    character_damage = random.randint(0, 10) + character["Attack"]

    if character_attack in character["Jutsu"].keys():
        character_damage = character["Jutsu"][character_attack] + character["Magic"]
        jutsu_chakra = int(character_damage / 2)

        if character["Chakra"] < jutsu_chakra:
            print("Not enough chakra to cast this jutsu..")
            return

        character["Chakra"] -= jutsu_chakra
        print(f"{character_attack[1]} {jutsu_chakra} chakra points used.")
        time.sleep(0.5)
        character_attack = character_attack[0]

    print(f"You inflicted {character_damage} damage with {character_attack}")
    time.sleep(0.5)
    monster["HP"] -= character_damage


def heal_character(character):
    heal_amount = int(character["Magic"] * 2)
    chakra_used = int(heal_amount * 1.2 - character["Magic"])
    if character["Chakra"] < chakra_used:
        print("No more chakra available.. A grave mistake to heal.")
        return
    if character["HP"] >= character["Max HP"]:
        print("Health is already full! I can't make a mistake like that again..")
        return

    character["Chakra"] -= chakra_used
    character["HP"] += heal_amount
    check_health_and_chakra_max(character)

    print(f"You activate your healing scroll to heal your wounds for {heal_amount}")
    print(f"You expended {chakra_used} chakra.")


def execute_battle_protocol(character, monster):
    while monster["HP"] > 0 and character["HP"] > 0:
        display_battle_menu()
        battle_action = input("What will you do?")
        while battle_action not in ['1', '2', '3', '4']:
            print("Invalid input!")
            battle_action = input("What will you do?")

        if int(battle_action) == 1:
            character_damage_sequence(character, monster)
            monster_damage_sequence(character, monster)
            display_battle_hp(character, monster)
        elif int(battle_action) == 2:
            jutsu_name = get_jutsu_choice(character)
            if jutsu_name == 'q':
                continue
            character_damage_sequence(character, monster, jutsu_name)
            monster_damage_sequence(character, monster)
            display_battle_hp(character, monster)
        elif int(battle_action) == 3:
            heal_character(character)
            monster_damage_sequence(character, monster)
            display_battle_hp(character, monster)
        elif int(battle_action) == 4:
            escape_chance = random.randint(1, 10)
            if (monster['name'] != "Madara Uchiha" or monster['name'] != "Orochimaru") and escape_chance < 6:
                print("You have escaped battle!")
                describe_current_location(character)
                break
            else:
                print("Escape failed!")
                monster_damage_sequence(character, monster)
                display_battle_hp(character, monster)

    if monster["HP"] <= 0:
        print("The foe has been vanquished!")
        experience(character, monster["XP"])
        describe_current_location(character)
