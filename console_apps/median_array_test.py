from pytest import fixture
from median_array import get_median_array


@fixture
def data() -> list[list[list[int | float]]]:
    return [
        [[1, 3], [2], [2]],
        [[1, 2], [3, 4], [2.5]],
    ]


def test_median_array(data) -> None:
    for i in data:
        exp: int | float = i[2][0]
        res: int | float = get_median_array(i[0], i[1])
        assert exp == res
