from pytest import fixture
from typing import Callable, TypeAlias
from filters import negative, positive, odds, evens

INP: list[int | float] = [0, 1, 2, 3, -4, 5, 6, 7, -8, 9, 10, -11]
Func: TypeAlias = Callable[[list[int | float]], list[int | float]]


@fixture
def exp() -> list[list[int | float]]:
    return [
        [0, 1, 2, 3, 5, 6, 7, 9, 10],
        [0, -4, -8, -11],
        [1, 3, 5, 7, 9, -11],
        [0, 2, -4, 6, -8, 10],
    ]


@fixture
def func() -> list[Func]:
    return [negative, positive, odds, evens]


def test_filter_funcs(exp: list[list[int | float]], func: list[Func]) -> None:
    for i in range(0, len(exp)):
        assert exp[i] == func[i](INP)
