from unittest import TestCase
from game_events import assign_jutsu
from unittest.mock import patch
import io


class TestAssignJutsu(TestCase):

    @patch('random.randint', return_value=25)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_assign_jutsu(self, mock_output, random_number_generator):

        new_character_jutsu = ("Fuuton","A blast of wind emerges and blows the enemy away.",
                               "A destructive gust of wind")
        character = {"Jutsu": {}}

        assign_jutsu(character, new_character_jutsu)

        actual = mock_output.getvalue()
        expected = "You have gained a new Jutsu, Fuuton\n"

        self.assertEqual(expected, actual)

