from pytest import fixture
from tail_recursion import recursive_sum, recursive_sum_tail


@fixture
def data() -> tuple[int, list[int]]:
    return 55, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def test_recursive_sum(data: tuple[int, list[int]]) -> None:
    exp, inp = data
    assert exp == recursive_sum(inp)


def test_recursive_sum_tail(data: tuple[int, list[int]]) -> None:
    exp, inp = data
    assert exp == recursive_sum_tail(inp)
