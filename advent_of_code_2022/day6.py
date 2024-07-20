def day6(data: list[str]) -> list[int]:
    return [__calc(item) for item in data]


def __calc(item: str, i: int = 0) -> int:
    if i + 3 >= len(item):
        return i + 4
    if __val(item, i):
        return i + 4
    return __calc(item, i + 1)


def __val(item: str, i: int) -> bool:
    v4 = item[i] != item[i + 1] and item[i] != item[i + 2] and item[i] != item[i + 3]
    v3 = item[i + 1] != item[i + 2] and item[i + 1] != item[i + 3]
    v2 = item[i + 2] != item[i + 3]
    return v4 and v3 and v2
