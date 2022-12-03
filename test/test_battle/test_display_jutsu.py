import io
from unittest import TestCase
from unittest.mock import patch

from battle import display_jutsu


class TestDisplayJutsu(TestCase):
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_display_jutsu_for_one_element_for_key_jutsu(self, mock_output):
        character = {"Jutsu": {("Katon", "Unleash a fiery blast of chakra!", "A powerful fire blast"): 22}}
        display_jutsu(character)
        expected = "1 - Katon - A powerful fire blast"
        self.assertEqual(expected, mock_output.getvalue())

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_display_jutsu_for_multi_elements_for_key_jutsu(self, mock_output):
        character = {"Jutsu": {("Katon", "Unleash a fiery blast of chakra!", "A powerful fire blast"): 22, ("abc",
                                                                                                            "xyz",
                                                                                                            "qwe"): 2}}
        display_jutsu(character)
        expected = "1 - Katon - A powerful fire blast\n2 - abc - qwe\n"
        self.assertEqual(expected, mock_output.getvalue())
