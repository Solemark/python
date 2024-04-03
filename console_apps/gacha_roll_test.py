from unittest import TestCase
from gacha_roll import roll


class TestGachaRoll(TestCase):
    def test_gacha_roll_FGO(self) -> None:
        substr = "FGO"
        result = roll("FGO")
        self.assertIn(substr, result)

    def test_gacha_roll_AK(self) -> None:
        substr = "AK"
        result = roll("AK")
        self.assertIn(substr, result)

    def test_gacha_roll_GI(self) -> None:
        substr = "GI"
        result = roll("GI")
        self.assertIn(substr, result)

    def test_failed_roll(self) -> None:
        substr = roll("TEST")
        result = "Unknown Game!"
        self.assertEqual(substr, result)
