def recursive_sum(a: list[int], i: int = 0) -> int:
    if i >= len(a) - 1:
        return a[i]
    return a[i] + recursive_sum(a, i + 1)


def recursive_sum_tail(a: list[int], i: int = 0, total: int = 0) -> int:
    if i > len(a) - 1:
        return total
    return recursive_sum_tail(a, i + 1, total + a[i])
