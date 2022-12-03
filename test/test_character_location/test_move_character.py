from unittest import TestCase
from character_location import move_character


class TestMoveCharacter(TestCase):
    def test_move_character_north(self):
        character_dictionary = {"X": 2, "Y": 2}
        direction = "North"
        expected = {"X": 2, "Y": 3}

        move_character(character_dictionary, direction)

        self.assertEqual(expected, character_dictionary)

    def test_move_character_west(self):
        character_dictionary = {"X": 2, "Y": 2}
        direction = "West"
        expected = {"X": 1, "Y": 2}

        move_character(character_dictionary, direction)

        self.assertEqual(expected, character_dictionary)

    def test_move_character_east(self):
        character_dictionary = {"X": 2, "Y": 2}
        direction = "East"
        expected = {"X": 3, "Y": 2}

        move_character(character_dictionary, direction)

        self.assertEqual(expected, character_dictionary)

    def test_move_character_south(self):
        character_dictionary = {"X": 2, "Y": 2}
        direction = "South"
        expected = {"X": 2, "Y": 1}

        move_character(character_dictionary, direction)

        self.assertEqual(expected, character_dictionary)

