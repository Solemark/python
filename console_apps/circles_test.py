from unittest import TestCase
from math import pi
from circles import get_area, get_circ


class TestCircle(TestCase):
    def setUp(self) -> None:
        self.areas: list[list[float | int]] = [
            [pi, 1],
            [0, 0],
            [(pi * 2.1**2), 2.1],
        ]
        self.circs: list[list[float | int]] = [
            [6.2831853, 1],
            [0, 0],
            [(pi * 2.1 * 2), 2.1],
        ]

    # Test areas when radius >= 0
    def test_area(self) -> None:
        for item in self.areas:
            self.assertAlmostEqual(item[0], get_area(item[1]))

    def test_circ(self) -> None:
        for item in self.circs:
            self.assertAlmostEqual(item[0], get_circ(item[1]))
