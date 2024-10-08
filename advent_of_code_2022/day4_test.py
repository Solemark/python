from pytest import fixture
from day4 import day4


@fixture
def data() -> tuple[list[list[str]], int]:
    return [
        ["2-4", "6-8"],
        ["2-3", "4-5"],
        ["5-7", "7-9"],
        ["2-8", "3-7"],
        ["6-6", "4-6"],
        ["2-6", "4-8"],
    ], 2


def test_day4(data: tuple[list[list[str]], int]) -> None:
    inp, exp = data
    res: int = day4(inp)
    assert exp == res
