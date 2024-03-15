import unittest
from day2 import day2


class Day2_test(unittest.TestCase):
    def test_day2(self) -> None:
        expect: int = 8
        result: int = day2(
            [
                "3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",  # + 1
                "1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",  # + 2
                "8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
                "1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
                "6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green",  # + 5
            ],  # + 8
            {
                "red": 12,
                "green": 13,
                "blue": 14,
            },
        )
        self.assertEqual(expect, result)
