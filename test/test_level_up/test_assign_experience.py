from unittest import TestCase
from level_up import assign_experience


class TestAssignExperience(TestCase):
    def test_level_up_XP_equal_to_XPToLevelUp(self):
        character = {"Level": 2, "XP": 200, "XPToLevelUp": 200}
        assign_experience(character)

        expected = {"Level": 3, "XP": 0, "XPToLevelUp": 400}

        self.assertEqual(expected, character)

    def test_level_up_XP_greater_than_XPToLevelUp(self):
        character = {"Level": 1, "XP": 300, "XPToLevelUp": 200}
        assign_experience(character)

        expected = {"Level": 2, "XP": 100, "XPToLevelUp": 400}

        self.assertEqual(expected, character)

    def test_level_up_to_level_3(self):
        character = {"Level": 2, "XP": 405, "XPToLevelUp": 400}
        assign_experience(character)

        expected = {"Level": 3, "XP": 5, "XPToLevelUp": 700}

        self.assertEqual(expected, character)

