def day1(data: list[str], totals: list[int] = [], total: int = 0, i: int = 0) -> str:
    if len(data) - 1 <= i:
        return f"Elf {max(i for i in enumerate([*totals, int(data[i])]))[0]} has the most calories"
    if data[i] == "":
        totals = [*totals, total]
        total = 0
    else:
        total = total + int(data[i])
    return day1(data, totals, total, i + 1)
