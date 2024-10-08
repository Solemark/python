from pytest import fixture
from fizz_buzz import fizz_buzz


@fixture
def data() -> tuple[list[int], list[str]]:
    return (
        [3, 5, 20],
        [
            "1",
            "2",
            "fizz",
            "4",
            "buzz",
            "fizz",
            "7",
            "8",
            "fizz",
            "buzz",
            "11",
            "fizz",
            "13",
            "14",
            "fizzbuzz",
            "16",
            "17",
            "fizz",
            "19",
            "buzz",
        ],
    )


def test_fizz_buzz_to_twenty(data: tuple[list[int], list[str]]) -> None:
    inp, exp = data
    assert exp == fizz_buzz(inp[0], inp[1], inp[2])
