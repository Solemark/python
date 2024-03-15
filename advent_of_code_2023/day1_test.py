import unittest
from day1 import day1


class Day2_test(unittest.TestCase):
    def test_day2(self) -> None:
        expect: int = 142
        result: int = day1(
            [
                "1abc2",  # 12
                "pqr3stu8vwx",  # 38
                "a1b2c3d4e5f",  # 15
                "treb7uchet",  # 77
            ]  # 142
        )
        self.assertEqual(expect, result)
