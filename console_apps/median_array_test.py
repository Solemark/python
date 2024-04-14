from unittest import TestCase

from median_array import get_median_array


class TestMedianArray(TestCase):
    def setUp(self) -> None:
        self.data: list[list[list[int | float]]] = [
            [[1, 3], [2], [2]],
            [[1, 2], [3, 4], [2.5]],
        ]

    def test_median_array(self) -> None:
        for part in self.data:
            expect: int | float = part[2][0]
            result: int | float = get_median_array(part[0], part[1])
            self.assertEqual(expect, result)
