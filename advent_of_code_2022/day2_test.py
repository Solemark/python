from pytest import fixture
from day2 import day2


@fixture
def data() -> tuple[list[list[str]], int]:
    return [["A", "Y"], ["B", "X"], ["C", "Z"]], 15


def test_day2(data: tuple[list[list[str]], int]) -> None:
    inp, exp = data
    assert exp == day2(inp)
