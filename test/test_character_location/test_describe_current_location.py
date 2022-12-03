from unittest import TestCase
from unittest.mock import patch
import io

from character_location import describe_current_location


class TestDescribeCurrentLocation(TestCase):
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_describe_current_location_in_plus_sign(self, mock_output):
        character = {"X": 2, "Y": 3}
        describe_current_location(character)
        expected = "+ + + + + + + + + B\n+ + + + + + + + + +\n+ + H + + + + H + +\n+ + + + + + + + + +\n" \
                   "+ + + + + E + + + +\n+ + + + + + + + + +\n+ + U + + + + + + +\n+ + H + + + + H + +\n" \
                   "+ + + + + + + + + +\n+ + + + + + + + + +\n"
        self.assertEqual(expected, mock_output.getvalue())

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_describe_current_location_in_B_letter_sign(self, mock_output):
        character = {"X": 9, "Y": 9}
        describe_current_location(character)
        expected = "+ + + + + + + + + U\n+ + + + + + + + + +\n+ + H + + + + H + +\n+ + + + + + + + + +\n" \
                   "+ + + + + E + + + +\n+ + + + + + + + + +\n+ + + + + + + + + +\n+ + H + + + + H + +\n" \
                   "+ + + + + + + + + +\n+ + + + + + + + + +\n"
        self.assertEqual(expected, mock_output.getvalue())

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_describe_current_location_in_H_letter_sign(self, mock_output):
        character = {"X": 2, "Y": 2}
        describe_current_location(character)
        expected = "+ + + + + + + + + B\n+ + + + + + + + + +\n+ + H + + + + H + +\n+ + + + + + + + + +\n" \
                   "+ + + + + E + + + +\n+ + + + + + + + + +\n+ + + + + + + + + +\n+ + U + + + + H + +\n" \
                   "+ + + + + + + + + +\n+ + + + + + + + + +\n"
        self.assertEqual(expected, mock_output.getvalue())

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_describe_current_location_in_E_letter_sign(self, mock_output):
        character = {"X": 5, "Y": 5}
        describe_current_location(character)
        expected = "+ + + + + + + + + B\n+ + + + + + + + + +\n+ + H + + + + H + +\n+ + + + + + + + + +\n" \
                   "+ + + + + U + + + +\n+ + + + + + + + + +\n+ + + + + + + + + +\n+ + H + + + + H + +\n" \
                   "+ + + + + + + + + +\n+ + + + + + + + + +\n"
        self.assertEqual(expected, mock_output.getvalue())
