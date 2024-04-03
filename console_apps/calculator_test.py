from unittest import TestCase
from calculator import add, subtract, multiply, divide


class TestCalculator(TestCase):
    def getData(self) -> list[list[int]]:
        return [
            [5, 5],
            [5, -5],
            [-5, -5],
        ]

    def test_addition(self) -> None:
        for data in self.getData():
            a: int = data[0]
            b: int = data[1]
            self.assertAlmostEqual((a + b), add(a, b))

    def test_subtraction(self) -> None:
        for data in self.getData():
            a: int = data[0]
            b: int = data[1]
            self.assertAlmostEqual((a - b), subtract(a, b))

    def test_multiplication(self) -> None:
        for data in self.getData():
            a: int = data[0]
            b: int = data[1]
            self.assertAlmostEqual((a * b), multiply(a, b))

    def test_division(self) -> None:
        for data in self.getData():
            a: int = data[0]
            b: int = data[1]
            self.assertAlmostEqual((a / b), divide(a, b))
