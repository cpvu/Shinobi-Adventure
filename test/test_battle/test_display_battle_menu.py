import io
from unittest import TestCase
from unittest.mock import patch

from battle import display_battle_menu


class TestDisplayBattleMenu(TestCase):
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_display_battle_menu(self, mock_output):
        expected = '1 - Attack\n2 - Jutsu\n3 - Heal\n4 - Flee\n'
        display_battle_menu()
        self.assertEqual(expected, mock_output.getvalue())


