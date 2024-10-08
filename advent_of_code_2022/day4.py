def day4(data: list[list[str]]) -> int:
    total: int = 0
    for row in data:
        left, right = __split_row(row)
        if left[0] <= right[0] and left[1] >= right[1]:
            total += 1
        elif left[0] >= right[0] and left[1] <= right[1]:
            total += 1
    return total


def __split_row(data: list[str]) -> tuple[list[int], list[int]]:
    left: list[int] = list(map(int, data[0].split("-")))
    right: list[int] = list(map(int, data[1].split("-")))
    return left, right
