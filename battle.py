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

    :param character: a dictionary that contain an "XP" key, type of the value of "XP" key is positive integer
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
    Print the jutsu as enumeration with numbers start from 1.

    :param character: a dictionary have a key "Jutsu"
    :precondition: character must be a dictionary have a key "Jutsu", the value is a dictionary that length greater than
                   zero
    :precondition: the key of "Jutsu" value dictionary must be a tuple that has three non-empty string elements.
    :post condition: print the jutsu as enumeration with numbers start from 1 and return a tuple
    :return: a tuple, first element is a number list, second element is string list.
    """
    jutsu_selection = [key for key in character["Jutsu"].keys()]
    jutsu_numbers = []
    for jutsu in enumerate(jutsu_selection, 1):
        print(f"{jutsu[0]} - {jutsu[1][0]} - {jutsu[1][2]}")
        jutsu_numbers.append(str(jutsu[0]))

    return jutsu_numbers, jutsu_selection


def get_jutsu_choice(character):
    """
    Return character's jutsu key according to user input.

    :param character: a dictionary have a key "Jutsu"
    :precondition: character must be a dictionary have a key "Jutsu", the value is a dictionary that length greater than
                   zero
    :post condition: if user input is not the number in jutsu enumeration and not "q", prompt user "Invalid input" and
                     ask user to input again
    :post condition: if user input is "q", return "q"
    :post condition: if user input is in the numbers of jutsu enumeration, return the matched key of "jutsu" value in
                     character
    :return: return "q" if user input "q", otherwise, return the matched key of "jutsu" value in character
    """
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
    :precondition: character must be a dictionary that contain "Name" key, value should be non-empty string
    :precondition: character must have "HP", "Max HP", "Chakra", "Max Chakra" as keys, all values should be non-zero
                   positive integer
    :precondition: monster must be a dictionary have "name" key, value should be non-empty string, "HP" key, value
                   should be non-zero positive integer
    :post condition: print the monster name and HP, character Name, current HP, current Chakra.
    """
    print(f'{monster["name"]} - HP:{monster["HP"]}HP')
    print(f'{character["Name"]} - HP: {character["HP"]}/{character["Max HP"]} Chakra:{character["Chakra"]}/'
          f'{character["Max Chakra"]}')


def monster_damage_sequence(character, monster):
    """
    Decide the monster behavior according to the ability.

    :param character: a dictionary have an "HP" key
    :param monster: a dictionary have "ability" key that value is a dictionary
    :precondition: character must be a dictionary that as least have an "HP" key, which value is a positive integer
    :precondition: monster must be a dictionary have "ability" key that value is a dictionary, which has "title", "heal"
                   or "attack" keys, all values should be positive integer
    :post condition: if monster "ability" is "Recovery", add 20 to monster "HP"
    :post condition: if monster "ability" is not "Recovery", reduce character "HP" according to the monster "attack"
    """
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
    """
    Reduce monster "HP" according to character_attack.

    :param character: a dictionary has "Jutsu", "Attack", "HP", "Magic", "Chakra" keys
    :param monster: a dictionary has "HP" key
    :param character_attack: a string, with a default value of "slice"
    :precondition: character is a dictionary has "Jutsu", "Attack", "HP", "Magic", "Chakra" keys
    :precondition: monster is a dictionary has "HP" key
    :post condition: if character_attack in "Jutsu" list, reduce the monster "HP" according to the "Jutsu" attack and
                     "Magic"
    :post condition: if character_attack not in "Jutsu" list, reduce the monster "HP" according to character "Attack"
    :post condition: if character_attack in "Jutsu" list and character "Chakra" lower than the damage, prompt not enough
                     chakra message
    """
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
    """
    Increase character "HP", maintain the same if character "Chakra" is not enough or "HP" already full.

    :param character: a dictionary has "Magic", "Chakra", "HP" keys
    :precondition: character must be a dictionary that has "Magic", "Chakra", "HP" keys
    :post condition: increase character "HP", if "Chakra" is higher than increase amount
    :post condition: maintain same character "HP", if "Chakra" is lower than increase amount
    :post condition: maintain same character "HP", if "HP" is higher than or equal to "Max HP"
    """
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
    """
    Execute the battle sequence according to user input.

    :param character: a dictionary
    :param monster: a dictionary
    :precondition: character must be a dictionary has "X", "Y", "Level", "XP", "XPToLevelUp", "HP", "Max HP", "Chakra",
                   "Max Chakra", "Attack", "Magic", "Luck", "Goal Achieved", "Jutsu" as keys
    :precondition: monster must be a dictionary has "name", "HP", "XP", "ability" as keys
    :post condition: validate the user input is one of '1', '2', '3', '4'
    :post condition: if user input is "1", call character_damage_sequence(), monster_damage_sequence(),
                     display_battle_hp() functions as sequence
    :post condition: if user input is "2", call get_jutsu_choice() and check the return value, if it's "q",
                     start from the while loop again, if it's not "q" call character_damage_sequence(),
                     monster_damage_sequence(), display_battle_hp() functions as sequence
    :post condition: if user input is "3", call heal_character(), monster_damage_sequence(),
                     display_battle_hp() functions as sequence
    :post condition: if user input is "4", generate a random number, then check if monster is "Madara Uchiha" or
                     "Orochimaru", if it is and the random number is lower than 6 prompt user escape successful and call
                     describe_current_location(), else prompt user escape failed and monster_damage_sequence()
                     display_battle_hp() functions as sequence
    :post condition: if monster "HP" lower than zero, print "The foe has been vanquished!" and call
                     experience() describe_current_location() functions as sequence
    """
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
