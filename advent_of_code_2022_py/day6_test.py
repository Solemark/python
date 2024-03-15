import unittest
from day6 import Day6


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
        for i in range(data.__len__()):
            self.assertEqual(expect[i], Day6().run(data[i]), data[i])
