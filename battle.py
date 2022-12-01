import random
import json
import time
import itertools

def generate_jutsu():
    jutsu_names = ["Chidori", "Raikira", "Kirin"]
    random_number = random.randint(20, 100)


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


def display_battle_menu():
    combat_options = ("Attack", "Jutsu", "Heal", "Flee")

    for battle_options in enumerate(combat_options, 1):
        print(f"{battle_options[0]} - {battle_options[1]}")


def display_jutsu(character: dict):

    jutsu_selection = [key for key in character["Jutsu"].keys()]

    for jutsu in enumerate(jutsu_selection, 1):
        print(f"{jutsu[0]} - {jutsu[1][0]}")

    jutsu_choice = int(input("Select your jutsu")) - 1

    return jutsu_selection[jutsu_choice]


def display_normal_attack_sequence(character, monster):
    monster_attack = random.randint(0, 5) + monster["Attack"]
    character_attack = random.randint(0, 10) + character["Attack"]

    print(f"You inflicted {character_attack} damage with a slash")
    print(f'The {monster["name"]} flaps you for {monster_attack} damage!')

    monster["HP"] -= character_attack
    character["HP"] -= monster_attack


def display_battle_hp(character, monster):
    print(f'{monster["name"]}:{monster["HP"]}/{monster["MaxHP"]}HP')
    print(f'{character["Name"]}: {character["HP"]}/{character["Max HP"]}')


def monster_damage_sequence(character, monster):
    monster_attack = random.randint(0, 5) + monster["Attack"]
    print(f'The {monster["name"]} flaps you for {monster_attack} damage!')
    character["HP"] -= monster_attack


def character_damage_sequence(character, monster, character_attack = "slice"):
    character_damage = random.randint(0, 10) + character["Attack"]

    if character_attack in character["Jutsu"].keys():
        character_damage += character["Jutsu"][character_attack]
        print(character_attack[1])
        character_attack = character_attack[0]

    print(f"You inflicted {character_damage} damage with {character_attack}")
    monster["HP"] -= character_damage


def heal_character(character):
    heal_amount = character["Magic"] * 2
    character["HP"] += heal_amount
    if character["HP"] > character["Max HP"]:
        character["HP"] = character["Max HP"]
    print(f"You casted Chakra healing to heal {heal_amount}")


def battle(character, monster):
    while monster["HP"] > 0 and character["HP"] > 0:
        display_battle_menu()
        battle_action = int(input("What will you do?"))

        if battle_action == 1:
            character_damage_sequence(character, monster)
            monster_damage_sequence(character, monster)
            display_battle_hp(character, monster)
        elif battle_action == 2:
            jutsu_name = display_jutsu(character)
            character_damage_sequence(character, monster, jutsu_name)
            monster_damage_sequence(character, monster)
            display_battle_hp(character, monster)
        elif battle_action == 3:
            heal_character(character)
            monster_damage_sequence(character, monster)
            display_battle_hp(character, monster)
        elif battle_action == 4:
            print("You have escaped battle!")
            break

    if monster["HP"] <= 0:
        print("The foe has been vanquished!")
        experience(character, monster["XP"])
