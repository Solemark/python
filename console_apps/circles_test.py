from math import pi
from pytest import fixture
from circles import get_area, get_circ


@fixture
def areas() -> list[list[int | float]]:
    return [
        [pi, 1],
        [0, 0],
        [(pi * 2.1**2), 2.1],
    ]


@fixture
def circs() -> list[list[int | float]]:
    return [
        [6.2831853, 1],
        [0, 0],
        [(pi * 2.1 * 2), 2.1],
    ]


def test_area(areas) -> None:
    for item in areas:
        assert round(item[0], 2) == round(get_area(item[1]), 2)


def test_circ(circs) -> None:
    for item in circs:
        assert round(item[0], 2) == round(get_circ(item[1]), 2)
