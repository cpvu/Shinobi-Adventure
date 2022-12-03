from unittest import TestCase
import io
from unittest.mock import patch

from battle import display_battle_hp


class TestDisplayBattleHp(TestCase):
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_display_battle_hp_for_typical_character_and_monster(self, mock_output):
        character = {"Name": "han", "HP": 22, "Max HP": 30, "Chakra": 32, "Max Chakra": 40}
        monster = {"name": "aaa", "HP": 20}
        display_battle_hp(character, monster)
        expected = "aaa - HP:20HP\nhan - HP: 22/30 Chakra:32/40\n"
        self.assertEqual(expected, mock_output.getvalue())



