from functools import reduce


def day1(arr: list[str]) -> int:
    numbers: list[tuple[int, int]] = [__find_nums(row) for row in arr]
    results: list[int] = [(result[0] + result[1]) for result in numbers]
    return reduce(__add, [result for result in results])


def __find_nums(in_str: str) -> tuple[int, int]:
    chars: list[str] = list(in_str)
    numbers: list[str] = [char for char in chars if char.isdigit()]
    return (int(numbers[0]) * 10, int(numbers[-1]))


def __add(a: int, b: int) -> int:
    return a + b
