def recursive_sum(a: list[int], i: int = 0) -> int:
    """
    0 + a
    0 + a + b
    0 + a + b + c
    0 + a + b + c + d
    0 + a + b + c + d + e
    0 + a + b + c + d + 5
    0 + a + b + c + 9
    0 + a + b + 12
    0 + a + 14
    0 + 15
    15
    """
    if i >= len(a) - 1:
        return a[i]
    return a[i] + recursive_sum(a, i + 1)


def recursive_sum_tail(a: list[int], i: int = 0, total: int = 0) -> int:
    """
    0 + 1
    1 + 2
    3 + 3
    6 + 4
    10 + 5
    15
    total: int = 0
    for n in a:
        total += n
    return total
    """
    if i > len(a) - 1:
        return total
    return recursive_sum_tail(a, i + 1, total + a[i])


def main() -> None:
    a: list[int] = [1, 2, 3, 4, 5]
    print(recursive_sum(a))
    print(recursive_sum_tail(a))


if __name__ == "__main__":
    main()
