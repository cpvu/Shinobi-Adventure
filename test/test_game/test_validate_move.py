from unittest import TestCase
from character_location import validate_move
import io
from unittest.mock import patch


class Test(TestCase):
    def test_validate_move_north(self):
        board = {(0, 0): "Empty Room", (1, 0): "Empty Room", (0, 1): "Empty Room", (1, 1): "Battle Event"}
        character = {"X": 0, "Y": 0}
        direction = "North"

        actual = validate_move(board, character, direction)
        expected = True

        self.assertEqual(expected, actual)

    def test_validate_move_east(self):
        board = {(0, 0): "Empty Room", (1, 0): "Empty Room", (0, 1): "Empty Room", (1, 1): "Battle Event"}
        character = {"X": 0, "Y": 0}
        direction = "East"

        actual = validate_move(board, character, direction)
        expected = True

        self.assertEqual(expected, actual)

    def test_validate_move_south(self):
        board = {(0, 0): "Empty Room", (1, 0): "Empty Room", (0, 1): "Empty Room", (1, 1): "Battle Event"}
        character = {"X": 0, "Y": 1}
        direction = "South"

        actual = validate_move(board, character, direction)
        expected = True

        self.assertEqual(expected, actual)

    def test_validate_move_west(self):
        board = {(0, 0): "Empty Room", (1, 0): "Empty Room", (0, 1): "Empty Room", (1, 1): "Battle Event"}
        character = {"X": 1, "Y": 0}
        direction = "West"

        actual = validate_move(board, character, direction)
        expected = True

        self.assertEqual(expected, actual)

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_validate_move_south_invalid(self, mock_output):
        board = {(0, 0): "Empty Room", (1, 0): "Empty Room", (0, 1): "Empty Room", (1, 1): "Battle Event"}
        character = {"X": 0, "Y": 0}
        direction = "South"

        actual = validate_move(board, character, direction)
        expected = False

        expected_print_output = "Invalid action, you can't go that way!\n"
        actual_print_output = mock_output.getvalue()

        self.assertEqual(expected_print_output, actual_print_output)
        self.assertEqual(expected, actual)

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_validate_move_north_invalid(self, mock_output):
        board = {(0, 0): "Empty Room", (0, 9): "Empty Room", (0, 8): "Empty Room", (0, 7): "Battle Event"}
        character = {"X": 0, "Y": 9}
        direction = "West"

        actual = validate_move(board, character, direction)
        expected = False

        expected_print_output = "Invalid action, you can't go that way!\n"
        actual_print_output = mock_output.getvalue()

        self.assertEqual(expected_print_output, actual_print_output)
        self.assertEqual(expected, actual)

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_validate_move_west_invalid(self, mock_output):
        board = {(0, 0): "Empty Room", (0, 9): "Empty Room", (0, 8): "Empty Room", (0, 7): "Battle Event"}
        character = {"X": 0, "Y": 8}
        direction = "West"

        actual = validate_move(board, character, direction)
        expected = False

        expected_print_output = "Invalid action, you can't go that way!\n"
        actual_print_output = mock_output.getvalue()

        self.assertEqual(expected_print_output, actual_print_output)
        self.assertEqual(expected, actual)
