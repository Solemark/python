from unittest import TestCase
from fizz_buzz import fizz_buzz


class test_fizz_buzz(TestCase):
    def test_fizz_buzz_to_twenty(self) -> None:
        result = fizz_buzz(3, 5, 20)
        expect = [
            "1",
            "2",
            "fizz",
            "4",
            "buzz",
            "fizz",
            "7",
            "8",
            "fizz",
            "buzz",
            "11",
            "fizz",
            "13",
            "14",
            "fizzbuzz",
            "16",
            "17",
            "fizz",
            "19",
            "buzz",
        ]
        self.assertEqual(expect, result)
