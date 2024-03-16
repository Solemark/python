def day1(data: list[str], totals: list[int] = [], total: int = 0, i: int = 0) -> str:
    if len(data) - 1 <= i:
        return f"Elf {__getMax([*totals, total])} has the most calories"
    if data[i] == "":
        totals = [*totals, total]
        total = 0
    else:
        total = total + int(data[i])
    return day1(data, totals, total, i + 1)


def __getMax(totals: list[int]) -> int:
    return max(i for i, _ in enumerate(totals))
