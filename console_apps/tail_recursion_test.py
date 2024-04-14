from unittest import TestCase

from tail_recursion import recursive_sum, recursive_sum_tail


class TestTailRecursion(TestCase):
    def setUp(self) -> None:
        self.expect: int = 55
        self.data: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    def test_recursive_sum(self) -> None:
        self.assertEqual(self.expect, recursive_sum(self.data))

    def test_recursive_sum_tail(self) -> None:
        self.assertEqual(self.expect, recursive_sum_tail(self.data))
