from pytest import fixture
from reverse_array import reverse_same_array, reverse_array


@fixture
def data() -> tuple[list[int], list[int]]:
    return ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [10, 9, 8, 7, 6, 5, 4, 3, 2, 1])


def test_reverse_array(data: tuple[list[int], list[int]]) -> None:
    inp, exp = data
    assert exp == reverse_array(inp)
    assert exp == reverse_same_array(inp)
