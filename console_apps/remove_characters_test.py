from pytest import fixture
from remove_characters import remove


@fixture
def data() -> tuple[str, list[str], str]:
    return "Hello World!", ["l", " ", "!"], "HeoWord"


def test_remove_characters(data: tuple[str, list[str], str]) -> None:
    inp, chars, exp = data
    assert exp == remove(inp, chars)
