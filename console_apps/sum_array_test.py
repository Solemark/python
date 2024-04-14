from unittest import TestCase
from sum_array import sum


class TestSumArray(TestCase):
    def setUp(self) -> None:
        self.data: list[tuple[int, list[int | float]]] = [
            (15, [1, 2, 3, 4, 5]),
            (-1, [1, 2, -3, 4, -5]),
        ]

    def test_sum(self) -> None:
        for item in self.data:
            expect, data = item
            self.assertEqual(expect, sum(data))
