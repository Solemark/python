from unittest import TestCase

from swap_variables import swap


class test_swap_variables(TestCase):
    def test_swap_variables(self) -> None:
        self.assertEqual(swap(1, 2), (2, 1))
