import unittest
from day2 import day2


class advent_of_code_2022_tests(unittest.TestCase):
    def test_day2(self) -> None:
        data = [["A", "Y"], ["B", "X"], ["C", "Z"]]
        expect: int = 15
        result: int = day2(data)
        self.assertEqual(expect, result)
