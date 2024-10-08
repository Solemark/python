from pytest import fixture
from palindrome import palindrome_fp, palindrome


@fixture
def data() -> list[tuple[str, bool]]:
    return [
        ("DAD", True),
        ("Dad", False),
        ("ABCDCBA", True),
        ("ABCDcba", False),
    ]


def test_is_palindrome_fp(data: list[tuple[str, bool]]) -> None:
    for item in data:
        inp, exp = item
        assert exp == palindrome_fp(inp)


def test_is_palindrome(data: list[tuple[str, bool]]) -> None:
    for item in data:
        inp, exp = item
        assert exp == palindrome(inp)
