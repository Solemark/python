from functools import reduce


def compute(input: list[int | float]) -> int | float:
    return reduce(__add, input)


def __add(a: int | float, b: int | float) -> int | float:
    return a + b
