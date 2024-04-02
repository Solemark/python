from functools import reduce


def sum(input: list[int | float]) -> int | float:
    return reduce(lambda a, b: a + b, input)
