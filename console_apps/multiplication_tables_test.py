from unittest import TestCase
from multiplication_tables import calculate


class test_multiplication_tables(TestCase):
    def test_1_x_12(self) -> None:
        expect = calculate(1, 12)
        result = [
            "1 x 0 = 0",
            "1 x 1 = 1",
            "1 x 2 = 2",
            "1 x 3 = 3",
            "1 x 4 = 4",
            "1 x 5 = 5",
            "1 x 6 = 6",
            "1 x 7 = 7",
            "1 x 8 = 8",
            "1 x 9 = 9",
            "1 x 10 = 10",
            "1 x 11 = 11",
            "1 x 12 = 12",
        ]
        self.assertEqual(expect, result)

    def test_5_x_12(self) -> None:
        expect = calculate(5, 12)
        result = [
            "5 x 0 = 0",
            "5 x 1 = 5",
            "5 x 2 = 10",
            "5 x 3 = 15",
            "5 x 4 = 20",
            "5 x 5 = 25",
            "5 x 6 = 30",
            "5 x 7 = 35",
            "5 x 8 = 40",
            "5 x 9 = 45",
            "5 x 10 = 50",
            "5 x 11 = 55",
            "5 x 12 = 60",
        ]
        self.assertEqual(expect, result)

    def test_9_x_12(self) -> None:
        expect = calculate(9, 12)
        result = [
            "9 x 0 = 0",
            "9 x 1 = 9",
            "9 x 2 = 18",
            "9 x 3 = 27",
            "9 x 4 = 36",
            "9 x 5 = 45",
            "9 x 6 = 54",
            "9 x 7 = 63",
            "9 x 8 = 72",
            "9 x 9 = 81",
            "9 x 10 = 90",
            "9 x 11 = 99",
            "9 x 12 = 108",
        ]
        self.assertEqual(expect, result)

    def test_10_x_12(self) -> None:
        expect = calculate(10, 12)
        result = [
            "10 x 0 = 0",
            "10 x 1 = 10",
            "10 x 2 = 20",
            "10 x 3 = 30",
            "10 x 4 = 40",
            "10 x 5 = 50",
            "10 x 6 = 60",
            "10 x 7 = 70",
            "10 x 8 = 80",
            "10 x 9 = 90",
            "10 x 10 = 100",
            "10 x 11 = 110",
            "10 x 12 = 120",
        ]
        self.assertEqual(expect, result)

    def test_12_x_12(self) -> None:
        expect = calculate(12, 12)
        result = [
            "12 x 0 = 0",
            "12 x 1 = 12",
            "12 x 2 = 24",
            "12 x 3 = 36",
            "12 x 4 = 48",
            "12 x 5 = 60",
            "12 x 6 = 72",
            "12 x 7 = 84",
            "12 x 8 = 96",
            "12 x 9 = 108",
            "12 x 10 = 120",
            "12 x 11 = 132",
            "12 x 12 = 144",
        ]
        self.assertEqual(expect, result)
