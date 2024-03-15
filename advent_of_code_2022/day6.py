def day6(data: list[str]) -> list[int]:
    return [__calc(item) for item in data]


def __calc(item: str, i: int = 0) -> int:
    if item[i] != item[i + 1] and item[i] != item[i + 2] and item[i] != item[i + 3]:
        if item[i + 1] != item[i + 2] and item[i + 1] != item[i + 3]:
            if item[i + 2] != item[i + 3]:
                return i + 4
    return __calc(item, i + 1)
