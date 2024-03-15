import unittest

from day3 import day3


class advent_of_code_2022_tests(unittest.TestCase):
    def test_day3(self) -> None:
        data = [
            "vJrwpWtwJgWrhcsFMMfFFhFp",
            "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
            "PmmdzqPrVvPwwTWBwg",
            "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
            "ttgJtRGJQctTZtZT",
            "CrZsJsPPZsGzwwsLwLmpwMDw",
        ]
        expect: int = 157
        result: int = day3(data)
        self.assertEqual(expect, result)
