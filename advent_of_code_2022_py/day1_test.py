import unittest
from day1 import day1


class advent_of_code_2022_tests(unittest.TestCase):
    def test_day1(self) -> None:
        data = [
            "1000",  # 1
            "2000",
            "3000",
            "",
            "4000",  # 2
            "",
            "5000",  # 3
            "6000",
            "",
            "7000",  # 4
            "8000",
            "9000",
            "",
            "10000",  # 5
        ]
        expect: str = "Elf 4 has the most calories"
        result: str = day1(data)
        self.assertEqual(expect, result, f"expected: {expect}\nresult: {result}")
