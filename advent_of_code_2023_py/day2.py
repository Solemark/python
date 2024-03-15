import re
from typing import Any


def day2(games: list[str], dice: dict) -> int:
    games_str: list[list[str]] = [game.replace(" ", "").split(";") for game in games]
    results: list[list[bool]] = [__play_rounds(game, dice) for game in games_str]
    result: list[bool] = __flatten(results)
    return __count_points(result)


def __play_rounds(game: list[str], dice: dict) -> list[bool]:
    results_rounds: list[list[bool]] = [
        __check_round(round.split(","), dice) for round in game
    ]
    rounds_results: list[list[bool]] = [__check_game(round) for round in results_rounds]
    results: list[bool] = [False if False in rounds_results else True]
    return results


def __check_round(round: list[str], dice: dict) -> list[bool]:
    return [(__count_round(item, dice)) for item in round]


def __count_round(roll: str, dice: dict):
    return (
        False
        if dice[re.sub(r"\d+", "", roll)] <= int(re.sub(r"[^0-9.]", "", roll))
        else True
    )


def __check_game(game: list[bool]):
    return False if False in game else True


def __count_points(games: list[bool], total: int = 0, pos: int = 0) -> int:
    if pos >= (len(games)):
        return total
    if games[pos] is True:
        total += pos + 1
    return __count_points(games, total, (pos + 1))


def __flatten(outer_list: list[list[Any]]) -> list[Any]:
    return [item for inner_list in outer_list for item in inner_list]
