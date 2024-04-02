from math import floor, ceil


def get_median_array(x: list[int | float], y: list[int | float]) -> int | float:
    arr = sorted(x + y)
    i: int = len(arr)
    return (
        arr[int(i / 2)]
        if i % 2 != 0
        else (arr[floor(i / 2) - 1] + arr[ceil(i / 2)]) / 2
    )
