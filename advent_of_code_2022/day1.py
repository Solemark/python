def day1(data: list[str]) -> str:
    total: int = 0
    totals: list[int] = []
    for item in [*data, ""]:
        if item == "":
            totals.append(total)
            total = 0
        else:
            total += int(item)
    return f"Elf {max(i for i, _ in enumerate(totals))} has the most calories"
