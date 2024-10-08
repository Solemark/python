from pytest import fixture
from calculator import add, sub, mul, div


@fixture
def data() -> list[list[int]]:
    return [
        [5, 5],
        [5, -5],
        [-5, -5],
    ]


def test_add(data) -> None:
    for i in data:
        a: int = i[0]
        b: int = i[1]
        assert add(a, b) == a + b


def test_sub(data) -> None:
    for i in data:
        a: int = i[0]
        b: int = i[1]
        assert sub(a, b) == a - b


def test_mul(data) -> None:
    for i in data:
        a: int = i[0]
        b: int = i[1]
        assert mul(a, b) == a * b


def test_div(data) -> None:
    for i in data:
        a: int = i[0]
        b: int = i[1]
        assert div(a, b) == a / b
