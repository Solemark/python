from unittest import TestCase
from gacha_roll import roll


class TestGachaRoll(TestCase):
    def setUp(self) -> None:
        self.substr: list[str] = ["FGO", "AK", "GI", "Unknown"]

    def test_gacha_roll(self) -> None:
        for substr in self.substr:
            self.assertIn(substr, roll(substr))
