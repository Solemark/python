from unittest import TestCase
from recursive_sum import number, array


class TestRecursiveSum(TestCase):
    def setUp(self) -> None:
        self.expect: int = 55
        self.data: list[int | float] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    def test_recursive_sum(self) -> None:
        self.assertEqual(self.expect, number(self.data[-1]))
        self.assertEqual(self.expect, array(self.data))
