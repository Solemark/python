from pytest import fixture
from gacha_roll import roll


@fixture
def data() -> list[str]:
    return ["FGO", "AK", "GI", "Unknown"]


def test_gacha_roll(data: list[str]) -> None:
    for i in data:
        assert i in roll(i)
