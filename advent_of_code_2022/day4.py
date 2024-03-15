from functools import reduce


def day4(data: list[list[str]]) -> int:
    return reduce(__add, [__calc(row) for row in data])


def __add(x: int, y: int) -> int:
    return x + y


def __calc(row: list[str]) -> int:
    (left, right) = __str_list_to_number_list(row)
    if left[0] <= right[0] and left[1] >= right[1]:
        return 1
    elif left[0] >= right[0] and left[1] <= right[1]:
        return 1
    return 0


def __str_list_to_number_list(data: list[str]) -> tuple[list[int], list[int]]:
    left: list[int] = list(map(int, data[0].split("-")))
    right: list[int] = list(map(int, data[1].split("-")))
    return (left, right)
