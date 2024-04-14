from unittest import TestCase
from reverse_array import reverse_same_array, reverse_array


class TestReverseArray(TestCase):
    def setUp(self) -> None:
        self.data: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.expect: list[int] = list(reversed(self.data))

    def test_reverse_array(self) -> None:
        self.assertEqual(self.expect, reverse_array(self.data))

    def test_reverse_same_array(self) -> None:
        self.assertEqual(self.expect, reverse_same_array(self.data))
