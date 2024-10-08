from pytest import fixture
from day5 import day5


@fixture
def data() -> tuple[list[list[str]], list[list[int]], list[list[str]]]:
    return (
        [["Z", "N"], ["M", "C", "D"], ["P"]],
        [[1, 2, 1], [3, 1, 3], [2, 2, 1], [1, 1, 2]],
        [["C"], ["M"], ["P", "D", "N", "Z"]],
    )


def test_day5(data: tuple[list[list[str]], list[list[int]], list[list[str]]]) -> None:
    inp, mov, exp = data
    assert exp == day5(inp, mov)
