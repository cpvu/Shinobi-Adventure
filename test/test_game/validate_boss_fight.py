from unittest import TestCase
from game import validate_boss_fight
from unittest.mock import patch
import io


class TestValidateBossFight(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_character_level_one(self, mock_output):
        character = {"Level": 1}
        expected = validate_boss_fight(character)
        actual = False

        expected_output = "You've arrived at the Uchiha Dominion, but you are not strong enough yet.. Return here " \
                          "once you have reached Level 3!\n"

        actual_output = mock_output.getvalue()

        self.assertEqual(expected_output, actual_output)
        self.assertEqual(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_character_level_two(self, mock_output):
        character = {"Level": 2}
        expected = validate_boss_fight(character)
        actual = False

        expected_output = "You've arrived at the Uchiha Dominion, but you are not strong enough yet.. Return here " \
                          "once you have reached Level 3!\n"

        actual_output = mock_output.getvalue()

        self.assertEqual(expected_output, actual_output)
        self.assertEqual(expected, actual)

    def test_character_level_three(self):
        character_dictionary = {"Level": 3}
        expected_character_dictionary = validate_boss_fight(character_dictionary)
        actual = True

        self.assertEqual(expected_character_dictionary, actual)
