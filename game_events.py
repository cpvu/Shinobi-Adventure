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
    """
    Generate a random jutsu from a plain textfile containing jutsu name and descriptions.

    :post condition: Return a random jutsu from a randomly generated list of tuples containing the jutsu name
                     and descriptions
    post-condition: Print an error message "jutsus.txt does not exist or is not in the correct directory!" if a
                    FileNotFoundError occurs.
    :return: a tuple object, containing string values that represent the jutsu name and descriptors
    """
    try:
        with open("monsters/jutsus.txt") as fileobject:
            all_jutsus = []
    except FileNotFoundError:
        print("jutsus.txt does not exist or is not in the correct directory!")
    else:
        for line in fileobject.readlines():
            jutsu_pair = line.strip().split(',')
            all_jutsus.append((jutsu_pair[0], jutsu_pair[1], jutsu_pair[2]))
        return all_jutsus[random.randint(0, len(all_jutsus) - 1)]


def assign_jutsu(character: dict, jutsu: tuple):
    """
    Assign a character dictionary object a new key value pair representing a new jutsu.

    :param character: a dictionary object
    :param jutsu: a tuple object
    :pre-condition: character must be a dictionary object containing key values: "Name" containing a string, X", "Y",
                   "Level", "XP", "XPToLevelUp", "HP", "Chakra", "Max Chakra", "Attack", "Magic", "Luck"
                   containing integer values, "Goal achieved" containing a boolean, and "Jutsu" containing
                   a dictionary object.
    :pre-condition: jutsu must be a tuple object, containing three string values where one string represents the jutsu
                    name, one string represents the jutsu's description and one string represents the battle sequence.
    :post-condition: assign a new key value pair with a randomized value representing the jutsu's base damage to the
                     "Jutsu" key value in the character dictionary object
    :post-condition: print a statement indicating the jutsu the character gained
    """
    character["Jutsu"][jutsu] = random.randint(25, 60)
    print(f"You have gained a new Jutsu, {jutsu[0]}")


def execute_open_sacred_scroll(character: dict):
    """
    Execute game event to gain a new combat jutsu.

    :param character: a dictionary object
    :pre-condition: character must be a dictionary object containing key values: "Name" containing a string, X", "Y",
                   "Level", "XP", "XPToLevelUp", "HP", "Chakra", "Max Chakra", "Attack", "Magic", "Luck"
                   containing integer values, "Goal achieved" containing a boolean, and "Jutsu" containing
                   a dictionary object.
    :post-condition: execute treasure room game event to acquire a new jutsu.
    """
    print("You walk into a cave and stumble across an ancient dialect written on the walls.")
    print("Suddenly, the dialects glow fiercely with chakra, upon touching it you feel a new power flow into you..")
    time.sleep(1)
    new_jutsu = generate_jutsu()
    if new_jutsu in character["Jutsu"]:
        print("You already have this jutsu.. better luck next time.")

    assign_jutsu(character, new_jutsu)


def execute_sacred_scroll_battle(character: dict):
    """
    Execute game event to battle an enemy for obtain a new jutsu.
    :param character: a dictionary object
    :pre-condition: character must be a dictionary object containing key values: "Name" containing a string, X", "Y",
               "Level", "XP", "XPToLevelUp", "HP", "Chakra", "Max Chakra", "Attack", "Magic", "Luck"
               containing integer values, "Goal achieved" containing a boolean, and "Jutsu" containing
               a dictionary object.
    :post-condition: execute treasure room game event to battle an enemy to acquire a new jutsu
    :return:
    """
    print("You stumble across an ancient tablet containing a incantations for a jutsu. But you are ambushed by enemies")
    print("Prepare for battle!")
    treasure_room_monster = generate_monster(character)
    execute_battle_protocol(character, treasure_room_monster)
    print("You've defeated the enemies guarding the scroll! You walk up the tablet and touch it.")

    new_jutsu = generate_jutsu()
    if new_jutsu in character["Jutsu"]:
        print("You already have this jutsu.. better luck next time.")

    assign_jutsu(character, new_jutsu)


def execute_neutral_event():
    """
    Print dialogue for a neutral game event.

    :post-condition: Print dialogue for neutral treasure room game event
    """
    print("A scroll lays on the floor, you pick it up to see what it contains.")
    time.sleep(1)
    print("Turns out there's nothing inside.. Darn!")


def execute_sacred_water_event(character):
    """
    Print dialogue for game event that inflicts damage to character HP.

    :param character: a dictionary object
    :pre-condition: character must be a dictionary object containing key values: "Name" containing a string, X", "Y",
                   "Level", "XP", "XPToLevelUp", "HP", "Chakra", "Max Chakra", "Attack", "Magic", "Luck"
                    containing integer values, "Goal achieved" containing a boolean, and "Jutsu" containing
                    a dictionary object.
    :post-condition: print treasure room game event dialogue
    :post-condition: decrease the value contained in the key "HP" of the argument charcter dictionary object by a
                     randomized integer representing the amount of HP that the character loses
    """
    print("You grow quite thirsty.")
    time.sleep(1)
    print("There is a river nearby, a villager tells you that drinking this water brings about good fortune.")
    time.sleep(1)
    print("You take a handful of the water and drink it. ")
    time.sleep(1)
    random_damage = random.randint(0, 10)
    character["HP"] -= random_damage
    print(f"The water had something in it and made you feel sick! You take {random_damage} damage.")


def execute_good_fortune_event(character):
    """
    Execute rare game event to buff character attack and magic stats.

    :param character: a dictionary object
    :pre-condition: character must be a dictionary object containing key values: "Name" containing a string, X", "Y",
               "Level", "XP", "XPToLevelUp", "HP", "Chakra", "Max Chakra", "Attack", "Magic", "Luck"
               containing integer values, "Goal achieved" containing a boolean, and "Jutsu" containing
               a dictionary object.
    :post-condition: print game event dialogue
    :post-condition: assign an increase of a integer value of 25 to the character dictionary objects key value "Attack"
                     and "Magic"
    """

    print("You stroll along and look for a place to sleep for the night.")
    time.sleep(1)
    print("Suddenly you're struck with a mind numbing headache. Your vision blurs immensely.")
    time.sleep(1)
    print("You hear a ghostly voice.. 'Uchiha... revenge..'")
    print("...ta..ke m..y eye..s..I..am..sasuke...uchiha...the..mangekou...sharingan.. is.. no..w..yo..urs...")
    time.sleep(2)
    print("You snap out of it. Your vision, suddenly clear. But you feel like now you see so much more.")
    print("Witness this new power in your next battle..")

    character["Attack"] += 25
    character["Magic"] += 25


def generate_game_events(character):
    """
    Generate a random number that corresponds to a game event.
    :param character: a dictionary object
    :pre-condition: character must be a dictionary object containing key values: "Name" containing a string, X", "Y",
                    "Level", "XP", "XPToLevelUp", "HP", "Chakra", "Max Chakra", "Attack", "Magic", "Luck"
                    containing integer values, "Goal achieved" containing a boolean, and "Jutsu" containing
                    a dictionary object.
    :post-condition: execute game event function execute_open_sacred_scroll if the random number is greater than or
                     equal to 0 and less than or equal to 33
    :post-condition: execute game event function execute_sacred_scroll_battle if the random number is greater than 33
                     and less than or equal to 66
    :post-condition: execute game event function neural_event if the random number is greater than 66 and less than or
                     equal to 85
    :post-condition: execute game event function sacred_water_event(character) if the random number is greater than 86
                     and less than or equal to 99
    :post-condition: execute game event function execute_good_fortune_event if the random_number equal to 100
    :return: a None value
    """
    random_number = random.randint(0, 100)
    if 33 >= random_number >= 0:
        return execute_open_sacred_scroll(character)
    elif 66 >= random_number > 33:
        return execute_sacred_scroll_battle(character)
    elif 85 >= random_number > 66:
        return execute_neutral_event()
    elif 99 >= random_number > 86:
        return execute_sacred_water_event(character)
    elif random_number == 100:
        return execute_good_fortune_event(character)
