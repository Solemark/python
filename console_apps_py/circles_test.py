from unittest import TestCase
from math import pi
from circles import get_area, get_circ


class test_circle(TestCase):
    def get_area_data(self) -> list[list[int | float]]:
        return [
            [pi, 1],
            [0, 0],
            [(pi * 2.1**2), 2.1],
        ]

    def get_circ_data(self) -> list[list[int | float]]:
        return [
            [6.2831853, 1],
            [0, 0],
            [(pi * 2.1 * 2), 2.1],
        ]

    # Test areas when radius >= 0
    def test_area(self) -> None:
        items = self.get_area_data()
        for item in items:
            self.assertAlmostEqual(item[0], get_area(item[1]))

    def test_circ(self) -> None:
        items = self.get_circ_data()
        for item in items:
            self.assertAlmostEqual(item[0], get_circ(item[1]))
