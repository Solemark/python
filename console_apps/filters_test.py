from unittest import TestCase
from filters import negative, positive, odds, evens


class test_filter_negative(TestCase):
    def test_filter_negative(self) -> None:
        self.assertEqual(
            [0, 1, 2, 3, 5, 6, 7, 9, 10],
            negative([0, 1, 2, 3, -4, 5, 6, 7, -8, 9, 10, -11]),
        )

    def test_filter_positive(self) -> None:
        self.assertEqual(
            [0, -4, -8, -11], positive([0, 1, 2, 3, -4, 5, 6, 7, -8, 9, 10, -11])
        )

    def test_filter_odds(self) -> None:
        self.assertEqual(
            [1, 3, 5, 7, 9, -11], odds([0, 1, 2, 3, -4, 5, 6, 7, -8, 9, 10, -11])
        )

    def test_filter_evens(self) -> None:
        self.assertEqual(
            [0, 2, -4, 6, -8, 10], evens([0, 1, 2, 3, -4, 5, 6, 7, -8, 9, 10, -11])
        )
