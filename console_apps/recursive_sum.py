def number(m: int | float, i: int | float = 0, t: int | float = 0) -> int | float:
    if i > m:
        return t
    return number(m, i + 1, t + i)


def array(a: list[int | float], i: int = 0, t: int | float = 0) -> int | float:
    if i > len(a) - 1:
        return t
    return array(a, i + 1, t + a[i])
