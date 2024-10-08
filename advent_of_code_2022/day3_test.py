from pytest import fixture
from day3 import day3


@fixture
def data() -> tuple[list[str], int]:
    return [
        "vJrwpWtwJgWrhcsFMMfFFhFp",
        "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
        "PmmdzqPrVvPwwTWBwg",
        "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
        "ttgJtRGJQctTZtZT",
        "CrZsJsPPZsGzwwsLwLmpwMDw",
    ], 157


def test_day3(data: tuple[list[str], int]) -> None:
    inp, exp = data
    res: int = day3(inp)
    assert exp == res
