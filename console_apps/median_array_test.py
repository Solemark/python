from unittest import TestCase

from median_array import get_median_array


class TestMedianArray(TestCase):
    def test_median_array(self) -> None:
        data: list[list[list[int | float]]] = [
            [[1, 3], [2], [2]],
            [[1, 2], [3, 4], [2.5]],
        ]
        for part in data:
            expect: int | float = part[2][0]
            result: int | float = get_median_array(part[0], part[1])
            self.assertEqual(expect, result)
