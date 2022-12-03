from unittest import TestCase
from game_events import execute_good_fortune_event
from unittest.mock import patch
import io


class TestExecuteGoodFortunteEvent(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_execute_good_fortune_event(self, mock_output):
        character_dictionary = {"Attack": 30, "Magic": 25}
        execute_good_fortune_event(character_dictionary)

        actual_output = mock_output.getvalue()

        expected_output = "You stroll along and look for a place to sleep for the night.\n" \
            "Suddenly you're struck with a mind numbing headache. Your vision blurs immensely.\n" \
            "You hear a ghostly voice.. 'Uchiha... revenge..\n" \
            "...ta..ke m..y eye..s..I..am..sasuke...uchiha...the..mangekou...sharingan.. is.. no..w..yo..urs...\n" \
            "You snap out of it. Your vision, suddenly clear. But you feel like now you see so much more.\n" \
            "Witness this new power in your next battle..\n"

        actual_character = character_dictionary
        expected_character = {"Attack": 55, "Magic": 50}

        self.assertEqual(expected_character, actual_character)
        self.assertEqual(expected_output, actual_output)
