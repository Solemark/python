from unittest import TestCase
from recursive_sum import number, array


class test_recursive_sum(TestCase):
    def test_sum_number(self) -> None:
        input: int = 10
        expect: int = 55
        self.assertEqual(expect, number(input, 0))

    def test_sum_array(self) -> None:
        input: list[int | float] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        expect: int = 55
        self.assertEqual(expect, array(input, len(input), 0))
