def insertion(input: list[int | float], count: int) -> list[int | float]:
    if count <= 1:
        return input
    else:
        insertion(input, count - 1)
        current: int | float = input[count - 1]
        i: int = count - 2
        while i >= 0 and input[i] > current:
            input[i + 1] = input[i]
            i -= 1
            input[i + 1] = current
        return input
