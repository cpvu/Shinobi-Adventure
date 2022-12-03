from unittest import TestCase
from game_events import execute_sacred_water_event
from unittest.mock import patch
import io


class TestExecuteSacredWaterEvent(TestCase):
    @patch("random.randint", return_value=0)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_execute_sacred_water_event_for_random_number_is_zero(self, mock_output, _):
        character = {"HP": 78}
        execute_sacred_water_event(character)

        actual_output = mock_output.getvalue()

        expected_output = "You grow quite thirsty.\n" \
            "There is a river nearby, a villager tells you that drinking this water brings about good fortune.\n"\
            "You take a handful of the water and drink it.\n"\
            "The water had something in it and made you feel sick! You take 0 damage.\n"

        actual_character = character
        expected_character = {"HP": 78}

        self.assertEqual(expected_character, actual_character)
        self.assertEqual(expected_output, actual_output)

    @patch("random.randint", return_value=10)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_execute_sacred_water_event_for_random_number_is_ten(self, mock_output, _):
        character = {"HP": 78}
        execute_sacred_water_event(character)

        actual_output = mock_output.getvalue()

        expected_output = "You grow quite thirsty.\n" \
            "There is a river nearby, a villager tells you that drinking this water brings about good fortune.\n"\
            "You take a handful of the water and drink it.\n"\
            "The water had something in it and made you feel sick! You take 10 damage.\n"

        actual_character = character
        expected_character = {"HP": 68}

        self.assertEqual(expected_character, actual_character)
        self.assertEqual(expected_output, actual_output)

    @patch("random.randint", return_value=5)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_execute_sacred_water_event_for_random_number(self, mock_output, _):
        character = {"HP": 78}
        execute_sacred_water_event(character)

        actual_output = mock_output.getvalue()

        expected_output = "You grow quite thirsty.\n" \
            "There is a river nearby, a villager tells you that drinking this water brings about good fortune.\n"\
            "You take a handful of the water and drink it.\n"\
            "The water had something in it and made you feel sick! You take 5 damage.\n"

        actual_character = character
        expected_character = {"HP": 73}

        self.assertEqual(expected_character, actual_character)
        self.assertEqual(expected_output, actual_output)
