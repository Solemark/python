from pytest import fixture
from day6 import day6


@fixture
def data() -> tuple[list[str], list[int]]:
    return [
        "mjqjpqmgbljsphdztnvjfqwrcgsmlb",
        "bvwbjplbgvbhsrlpgdmjqwftvncz",
        "nppdvjthqldpwncqszvftbrmjlhg",
        "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg",
        "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw",
    ], [7, 5, 6, 10, 11]


def test_day6(data: tuple[list[str], list[int]]) -> None:
    inp, exp = data
    assert exp == day6(inp)
