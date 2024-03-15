from typing import Any
from unittest import TestCase


def swap(a: Any, b: Any) -> tuple[Any, Any]:
    a, b = b, a
    return a, b


class test_swap_variables(TestCase):
    def test_swap_variables(self) -> None:
        self.assertEqual(swap(1, 2), (2, 1))
