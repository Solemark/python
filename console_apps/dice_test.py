from unittest import TestCase
from dice import roll


class TestDiceRoll(TestCase):
    def test_d20(self) -> None:
        expect = roll(20)
        result = range(1, 21)
        self.assertIn(expect, result)

    def test_d12(self) -> None:
        expect = roll(12)
        result = range(1, 13)
        self.assertIn(expect, result)

    def test_d10(self) -> None:
        expect = roll(10)
        result = range(1, 11)
        self.assertIn(expect, result)

    def test_d8(self) -> None:
        expect = roll(8)
        result = range(1, 9)
        self.assertIn(expect, result)

    def test_d6(self) -> None:
        expect = roll(6)
        result = range(1, 7)
        self.assertIn(expect, result)

    def test_d4(self) -> None:
        expect = roll(4)
        result = range(1, 5)
        self.assertIn(expect, result)
