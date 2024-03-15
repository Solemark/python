import unittest
from day4 import day4


class advent_of_code_2022_tests(unittest.TestCase):
    def test_day4(self) -> None:
        data: list[list[str]] = [
            ["2-4", "6-8"],
            ["2-3", "4-5"],
            ["5-7", "7-9"],
            ["2-8", "3-7"],
            ["6-6", "4-6"],
            ["2-6", "4-8"],
        ]
        expect: int = 2
        result: int = day4(data)
        self.assertEqual(expect, result)
