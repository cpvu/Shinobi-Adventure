from unittest import TestCase
from generate_game_board import generate_room_type
from unittest.mock import patch
import io


class TestGenerateRoomType(TestCase):
    @patch("random.randint", return_value=20)
    def test_generate_room_type_empty_room(self, random_number_generator):
        expected = generate_room_type()
        actual = "Empty Room"

        self.assertEqual(expected, actual)

    @patch("random.randint", return_value=55)
    def test_generate_room_type_game_event(self, random_number_generator):
        expected = generate_room_type()
        actual = "Game Event"

        self.assertEqual(expected, actual)

    @patch("random.randint", return_value=80)
    def test_generate_room_type_game_event(self, random_number_generator):
        expected = generate_room_type()
        actual = "Monster Battle"

        self.assertEqual(expected, actual)
