import unittest
from day3 import Day3


class Day3_test(unittest.TestCase):
    def test_day3(self) -> None:
        expect: int = 4361
        result: int = Day3().run(
            [
                "467..114..",
                "...*......",
                "..35..633.",
                "......#...",
                "617*......",
                ".....+.58.",
                "..592.....",
                "......755.",
                "...$.*....",
                ".664.598..",
            ]
        )
        self.assertEqual(expect, result)

    def test_day3_odd_input(self) -> None:
        expect: int = 12345
        result: int = Day3().run(
            [
                "..+..",
                "12345",
            ]
        )
        self.assertEqual(expect, result)
