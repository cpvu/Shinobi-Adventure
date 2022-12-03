from unittest import TestCase
from game_events import execute_sacred_water_event
from unittest.mock import patch
import io

class Test(TestCase):
    @patch("random.randint", return_value=15)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_execute_sacred_water_event(self, mock_output, random_number_generator):
        character = {"HP": 78}
        execute_sacred_water_event(character)

        actual_output = mock_output.getvalue()

        expected_output = "You grow quite thirsty.\n" \
                   "There is a river nearby, a villager tells you that drinking this water brings about good fortune.\n"\
                   "You take a handful of the water and drink it.\n"\
                   "The water had something in it and made you feel sick! You take 15 damage.\n"

        actual_character = character
        expected_character = {"HP": 63}

        self.assertEqual(expected_character, actual_character)
        self.assertEqual(expected_output, actual_output)

