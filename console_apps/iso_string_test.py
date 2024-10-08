from pytest import fixture
from iso_string import is_iso


@fixture
def data() -> list[tuple[str, str, bool]]:
    return [("egg", "add", True), ("foo", "bar", False), ("paper", "title", True)]


def test_is_isomorphic(data: list[tuple[str, str, bool]]):
    for i in data:
        i1, i2, exp = i
        assert exp == is_iso(i1, i2)
