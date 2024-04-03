from unittest import TestCase
from reverse_array import reverse_same_array, reverse_array


class TestReverseArray(TestCase):
    input: list[int]

    def setUp(self):
        self.input = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    def test_reverse_same_array(self) -> None:
        self.assertEqual(list(reversed(self.input)), reverse_same_array(self.input))

    def test_reverse_array(self) -> None:
        self.assertEqual(list(reversed(self.input)), reverse_array(self.input))
