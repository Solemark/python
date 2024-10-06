from typing import Any


def reverse_same_array(arr: list[Any]) -> list[Any]:
    i: int = 0
    j: int = len(arr) - 1
    while i <= j:
        (x, y) = (arr[i], arr[j])
        (arr[i], arr[j]) = (y, x)
        (i, j) = (i + 1, j - 1)
    return arr


def reverse_array(arr: list[Any]) -> list[Any]:
    (output, i) = ([], len(arr) - 1)
    while i >= 0:
        output.append(arr[i])
        i -= 1
    return output


def reverse_array_new(arr: list[Any]) -> list[Any]:
    return list(reversed(arr))
