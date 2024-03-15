def day5(data: list[list[str]], MOVES: list[list[int]]) -> list[list[str]]:
    for MOVE in MOVES:
        moving: list[str] = []
        for _ in range(MOVE[0]):
            moving.append(data[MOVE[1] - 1].pop())
        data[MOVE[2] - 1] += moving
    return data
