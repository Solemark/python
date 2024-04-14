from unittest import TestCase
from calculator import add, subtract, multiply, divide


class TestCalculator(TestCase):
    def setUp(self) -> None:
        self.data = [
            [5, 5],
            [5, -5],
            [-5, -5],
        ]

    def test_addition(self) -> None:
        for item in self.data:
            a: int = item[0]
            b: int = item[1]
            self.assertAlmostEqual((a + b), add(a, b))

    def test_subtraction(self) -> None:
        for item in self.data:
            a: int = item[0]
            b: int = item[1]
            self.assertAlmostEqual((a - b), subtract(a, b))

    def test_multiplication(self) -> None:
        for item in self.data:
            a: int = item[0]
            b: int = item[1]
            self.assertAlmostEqual((a * b), multiply(a, b))

    def test_division(self) -> None:
        for item in self.data:
            a: int = item[0]
            b: int = item[1]
            self.assertAlmostEqual((a / b), divide(a, b))
