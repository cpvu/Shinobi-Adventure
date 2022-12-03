from unittest import TestCase
from level_up import assign_stats


class TestAssignStats(TestCase):
    def test_assign_stats(self):
        character = {"HP": 100, "Max HP": 100, "Attack": 20, "Magic": 10, "Chakra": 100, "Max Chakra": 100}
        assign_stats(character)

        expected = {"HP": 130, "Max HP": 130, "Attack": 26, "Magic": 13, "Chakra": 130, "Max Chakra": 130}

        self.assertEqual(expected, character)

    def test_assign_stats_different_values(self):
        character = {"HP": 100, "Max HP": 150, "Attack": 30, "Magic": 16, "Chakra": 100, "Max Chakra": 200}
        assign_stats(character)

        expected = {"HP": 130, "Max HP": 195, "Attack": 39, "Magic": 20, "Chakra": 130, "Max Chakra": 260}

        self.assertEqual(expected, character)


