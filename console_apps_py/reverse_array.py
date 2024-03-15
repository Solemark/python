from typing import Any


def reverse_same_array(arr: list[Any]) -> list[Any]:
    c: int = len(arr) - 1
    x: int = 0
    y: int = 0
    i: int = 0
    while i <= c:
        x = arr[i]
        y = arr[c]
        arr[i] = y
        arr[c] = x
        i += 1
        c -= 1
    return arr


def reverse_array(arr: list[Any]) -> list[Any]:
    output: list[Any] = []
    i: int = len(arr) - 1
    while i >= 0:
        output.append(arr[i])
        i -= 1
    return output
