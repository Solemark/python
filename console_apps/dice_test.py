from pytest import fixture
from dice import roll


@fixture
def dice() -> list[int]:
    return [4, 6, 8, 10, 12, 20]


def test_dice(dice: list[int]) -> None:
    for d in dice:
        assert roll(d) in range(1, d + 1)
