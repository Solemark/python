def day6(data: list[str]) -> list[int]:
    output: list[int] = []
    for item in data:
        for i, _ in enumerate(item):
            if __val(item, i):
                output.append(i + 4)
                break
    return output


def __val(item: str, i: int) -> bool:
    v4: bool = (
        item[i] != item[i + 1] and item[i] != item[i + 2] and item[i] != item[i + 3]
    )
    v3: bool = item[i + 1] != item[i + 2] and item[i + 1] != item[i + 3]
    v2: bool = item[i + 2] != item[i + 3]
    v1: bool = i + 3 >= len(item)
    return v4 and v3 and v2 or v1
