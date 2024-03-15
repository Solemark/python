import unittest

from day5 import day5


class advent_of_code_2022_tests(unittest.TestCase):
    def test_day5(self) -> None:
        data: list[list[str]] = [["Z", "N"], ["M", "C", "D"], ["P"]]
        MOVES: list[list[int]] = [[1, 2, 1], [3, 1, 3], [2, 2, 1], [1, 1, 2]]
        EXPECT: list[list[str]] = [["C"], ["M"], ["P", "D", "N", "Z"]]
        self.assertEqual(EXPECT, day5(data, MOVES))
