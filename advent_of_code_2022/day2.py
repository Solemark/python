rps: dict = {
    "A": "Rock",
    "B": "Paper",
    "C": "Scissors",
    "X": "Rock",
    "Y": "Paper",
    "Z": "Scissors",
}
points: dict = {
    "Rock": 1,
    "Paper": 2,
    "Scissors": 3,
    "Loss": 0,
    "Draw": 3,
    "Win": 6,
}
results: dict = {
    "Rock-Paper": points["Win"],
    "Paper-Scissors": points["Win"],
    "Scissors-Rock": points["Win"],
    "Paper-Rock": points["Loss"],
    "Scissors-Paper": points["Loss"],
    "Rock-Scissors": points["Loss"],
    "Rock-Rock": points["Draw"],
    "Paper-Paper": points["Draw"],
    "Scissors-Scissors": points["Draw"],
}


def day2(data: list[list[str]], i: int = 0, total: int = 0) -> int:
    total += points[rps[data[i][1]]]
    total += results[f"{rps[data[i][0]]}-{rps[data[i][1]]}"]
    if len(data) - 1 <= i:
        return total
    return day2(data, i + 1, total)
