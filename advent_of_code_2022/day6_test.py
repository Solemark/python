import unittest
from day6 import day6


class advent_of_code_2022_tests(unittest.TestCase):
    def test_day6(self) -> None:
        data: list[str] = [
            "mjqjpqmgbljsphdztnvjfqwrcgsmlb",
            "bvwbjplbgvbhsrlpgdmjqwftvncz",
            "nppdvjthqldpwncqszvftbrmjlhg",
            "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg",
            "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw",
        ]
        expect: list[int] = [7, 5, 6, 10, 11]
        self.assertEqual(expect, day6(data))
