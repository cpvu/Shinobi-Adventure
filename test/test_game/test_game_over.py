from unittest import TestCase
from game import game_over
from unittest.mock import patch
import io


class TestGameOverTestCase(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_game_over_true_zero_hp(self, mock_output):
        character = {"HP": 0}
        expected = game_over(character)
        actual = True

        expected_output = "You have died...\n" \
                          "Game over, please try again\n"

        actual_output = mock_output.getvalue()

        self.assertEqual(expected_output, actual_output)
        self.assertEqual(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_game_over_true_negative_hp(self, mock_output):
        character = {"HP": -20}
        expected = game_over(character)
        actual = True

        expected_output = "You have died...\n" \
                          "Game over, please try again\n"

        actual_output = mock_output.getvalue()

        self.assertEqual(expected_output, actual_output)
        self.assertEqual(expected, actual)

    def test_game_over_false(self):
        character = {"HP": 100}
        expected = game_over(character)
        actual = False

        self.assertEqual(expected, actual)