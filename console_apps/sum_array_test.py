from unittest import TestCase
from sum_array import sum


class TestSumArray(TestCase):
    def test_sum_array(self) -> None:
        self.assertEqual(15, sum([1, 2, 3, 4, 5]))

    def test_sum_array_negatives(self) -> None:
        self.assertEqual(-1, sum([1, 2, -3, 4, -5]))
