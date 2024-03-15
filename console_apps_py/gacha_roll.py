from functools import partial
from random import randint


def roll(game: str) -> str:
    play_fn = partial(__play, game)
    match game:
        case "FGO":
            output = play_fn(100, 300, 5)
        case "AK":
            output = play_fn(50, 100, 6)
        case "GI":
            output = play_fn(60, 90, 5)
        case _:
            output = "Unknown Game!"
    return output


def __play(game: str, rate: int, pity: int, rarity: int) -> str:
    return next(
        (
            f"it took {roll}/{pity} to get a {rarity}* in {game}"
            for roll in range(1, pity + 1)
            if roll == pity or rate == randint(1, rate)
        ),
    )
