import io
from unittest import TestCase
from unittest.mock import patch

from battle import experience


class TestExperience(TestCase):
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_experience_for_character_XP_zero(self, mock_output):
        character = {"XP": 0}
        monster_xp = 10
        experience(character, monster_xp)
        expected_dictionary = {"XP": 10}
        expected_output = "You have gained 10 experience!\n"
        self.assertEqual(expected_output, mock_output.getvalue())
        self.assertEqual(expected_dictionary, character)

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_experience_for_monster_XP_zero(self, mock_output):
        character = {"XP": 20}
        monster_xp = 0
        experience(character, monster_xp)
        expected = {"XP": 20}
        expected_output = "You have gained 0 experience!\n"
        self.assertEqual(expected_output, mock_output.getvalue())
        self.assertEqual(expected, character)

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_experience_for_both_character_XP_and_monster_XP_zero(self, mock_output):
        character = {"XP": 0}
        monster_xp = 0
        experience(character, monster_xp)
        expected_output = "You have gained 0 experience!\n"
        expected = {"XP": 0}
        self.assertEqual(expected_output, mock_output.getvalue())
        self.assertEqual(expected, character)

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_experience_for_both_character_XP_and_monster_XP_non_zero(self, mock_output):
        character = {"XP": 33}
        monster_xp = 23
        experience(character, monster_xp)
        expected_output = "You have gained 23 experience!\n"
        expected = {"XP": 56}
        self.assertEqual(expected_output, mock_output.getvalue())
        self.assertEqual(expected, character)
