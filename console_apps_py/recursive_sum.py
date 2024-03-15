def number(input: int, total: int) -> int:
    if input <= 0:
        return total
    total += input
    return number(input - 1, total)


def array(input: list[int | float], current: int, total: int | float) -> int | float:
    if current <= 0:
        return total
    total += input[current - 1]
    return array(input, current - 1, total)
