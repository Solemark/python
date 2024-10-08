from pytest import fixture
from recursive_sum import number, array


@fixture
def data() -> tuple[int, list[int | float]]:
    return (55, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])


def test_recursive_sum(data: tuple[int, list[int | float]]) -> None:
    exp, inp = data
    assert exp == number(inp[-1])
    assert exp == array(inp)
