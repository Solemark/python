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
    "RockPaper": points["Win"],
    "RockRock": points["Draw"],
    "RockScissors": points["Loss"],
    "PaperScissors": points["Win"],
    "PaperPaper": points["Draw"],
    "PaperRock": points["Loss"],
    "ScissorsRock": points["Win"],
    "ScissorsPaper": points["Loss"],
    "ScissorsScissors": points["Draw"],
}


def day2(data: list[list[str]]) -> int:
    total: int = 0
    for item in data:
        a, b, c = points[rps[item[1]]], rps[item[0]], rps[item[1]]
        total += a + results[f"{b}{c}"]
    return total
