def negative(arr: list[int | float]) -> list[int | float]:
    return [number for number in arr if number >= 0]


def positive(arr: list[int | float]) -> list[int | float]:
    return [number for number in arr if number <= 0]


def odds(arr: list[int | float]) -> list[int | float]:
    return [number for number in arr if number % 2 != 0]


def evens(arr: list[int | float]) -> list[int | float]:
    return [number for number in arr if number % 2 == 0]
