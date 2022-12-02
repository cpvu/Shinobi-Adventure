import random
import json
import time
from health_room import check_health_and_chakra_max
from character_location import printing_map
import itertools


def generate_monster(character):
    with open("monsters/monsters.json") as fileobject:
        all_monsters = json.load(fileobject)
        if character["Level"] == 1:
            return all_monsters[random.randint(0, 2)]
        elif character["Level"] == 2:
            return all_monsters[random.randint(0, 5)]
        elif character["Level"] == 3:
            return all_monsters[random.randint(0, 8)]


def generate_boss(character):
    if character["Level"] != 3:
        print("You have to reach Level 3 to fight the boss!")
    else:
        boss = {"name": "Madara Uchiha",
                "ability": [{"title": "Attack", "attack": 12}, {"title": "Shuriken", "attack": 22},
                            {"title": "Paper Bomb", "attack": 20}, {"title": "Recovery", "heal": 20}],
                "HP": 350}
        return boss


def generate_elite():
    elite = {
        "name": "Orochimaru",
        "ability": [{"title": "Attack", "attack": 12}, {"title": "Recovery", "heal": 20}],
        "HP": 350,
        "MaxHP": 350
    }
    return elite


def experience(character, monster_xp):
    character["XP"] += monster_xp
    time.sleep(0.5)
    print(f"You have gained {monster_xp} experience!")


def display_battle_menu():
    combat_options = ("Attack", "Jutsu", "Heal", "Flee")

    for battle_options in enumerate(combat_options, 1):
        print(f"{battle_options[0]} - {battle_options[1]}")


def display_jutsu(character: dict):
    jutsu_selection = [key for key in character["Jutsu"].keys()]

    for jutsu in enumerate(jutsu_selection, 1):
        print(f"{jutsu[0]} - {jutsu[1][0]} - {jutsu[1][2]}")

    jutsu_choice = input("Select your jutsu")
    while jutsu_choice not in ['1', '2', '3', '4']:
        print("Invalid input!")
        jutsu_choice = input("Select your jutsu")
    return jutsu_selection[int(jutsu_choice) - 1]


def display_normal_attack_sequence(character, monster):
    monster_attack = random.randint(0, 5) + monster["Attack"]
    character_attack = random.randint(0, 10) + character["Attack"]

    print(f"You inflicted {character_attack} damage with a slash")
    time.sleep(0.5)
    print(f'The {monster["name"]} flaps you for {monster_attack} damage!')
    time.sleep(0.5)

    monster["HP"] -= character_attack
    character["HP"] -= monster_attack


def display_battle_hp(character, monster):
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
    time.sleep(1)
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
        elif int(battle_action)== 2:
            jutsu_name = display_jutsu(character)
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
                printing_map(character)
                break
            else:
                print("Escape failed!")
                monster_damage_sequence(character, monster)
                display_battle_hp(character, monster)

    if monster["HP"] <= 0:
        print("The foe has been vanquished!")
        experience(character, monster["XP"])
