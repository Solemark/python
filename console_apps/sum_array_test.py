from pytest import fixture
from sum_array import compute


@fixture
def data() -> list[tuple[int | float, list[int | float]]]:
    return [
        (15, [1, 2, 3, 4, 5]),
        (-1, [1, 2, -3, 4, -5]),
    ]


def test_sum(data: list[tuple[int | float, list[int | float]]]) -> None:
    for item in data:
        expect, inp = item
        assert expect == compute(inp)
