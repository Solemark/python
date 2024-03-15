from unittest import TestCase
from recursive_sort import insertion


class test_recursive_sort(TestCase):
    def test_insertion_sort(self) -> None:
        input: list[int | float] = [5, 2, 9, 7, 14, 8]
        expect: list[int | float] = [2, 5, 7, 8, 9, 14]
        self.assertEqual(expect, insertion(input, len(input)))
