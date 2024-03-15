def negative(input: list[int | float]) -> list[int | float]:
    return [number for number in input if number >= 0]


def positive(input: list[int | float]) -> list[int | float]:
    return [number for number in input if number <= 0]


def odds(input: list[int | float]) -> list[int | float]:
    return [number for number in input if number % 2 != 0]


def evens(input: list[int | float]) -> list[int | float]:
    return [number for number in input if number % 2 == 0]
