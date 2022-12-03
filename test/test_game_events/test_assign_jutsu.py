from unittest import TestCase
from game_events import assign_jutsu
from unittest.mock import patch
import io


class TestAssignJutsu(TestCase):
    @patch('random.randint', return_value=25)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_assign_jutsu_minimum_damage(self, mock_output, random_number_generator):

        new_character_jutsu = ("Rasengan", "Spherical chakra channels into your left arm. You enemy is hit and spirals "
                                           "away.", "A powerful ball of spiraling chakra")

        actual_character_dictionary = {"Jutsu": {}}
        expected_character_dictionary = {"Jutsu": {("Rasengan", "Spherical chakra channels into your left arm. You "
                                                                "enemy is hit and spirals away.",
                                                    "A powerful ball of spiraling chakra"): 25}}

        assign_jutsu(actual_character_dictionary, new_character_jutsu)

        actual_output = mock_output.getvalue()
        expected_output = "You have gained a new Jutsu, Rasengan\n"

        self.assertEqual(expected_output, actual_output)
        self.assertEqual(expected_character_dictionary, actual_character_dictionary)

    @patch('random.randint', return_value=65)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_assign_jutsu_max_damage(self, mock_output, random_number_generator):
        new_character_jutsu = ("Fuuton", "A blast of wind emerges and blows the enemy away.",
                               "A destructive gust of wind")

        actual_character_dictionary = {"Jutsu": {}}
        expected_character_dictionary = {"Jutsu": {("Fuuton", "A blast of wind emerges and blows the enemy away.",
                                                    "A destructive gust of wind"): 65}}

        assign_jutsu(actual_character_dictionary, new_character_jutsu)

        actual_output = mock_output.getvalue()
        expected_output = "You have gained a new Jutsu, Fuuton\n"

        self.assertEqual(expected_output, actual_output)
        self.assertEqual(expected_character_dictionary, actual_character_dictionary)

    @patch('random.randint', return_value=35)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_assign_jutsu_average_damage(self, mock_output, random_number_generator):

        new_character_jutsu = ("Rasengan", "Spherical chakra channels into your left arm. You enemy is hit and spirals "
                                           "away.", "A powerful ball of spiraling chakra")
        actual_character_dictionary = {"Jutsu": {}}
        expected_character_dictionary = {"Jutsu": {("Rasengan", "Spherical chakra channels into your left arm. You "
                                                                "enemy is hit and spirals away.",
                                                    "A powerful ball of spiraling chakra"): 35}}

        assign_jutsu(actual_character_dictionary, new_character_jutsu)

        actual_output = mock_output.getvalue()
        expected_output = "You have gained a new Jutsu, Rasengan\n"

        self.assertEqual(expected_output, actual_output)
        self.assertEqual(expected_character_dictionary, actual_character_dictionary)
