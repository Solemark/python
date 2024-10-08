from pytest import fixture
from day1 import day1


@fixture
def data() -> tuple[list[str], str]:
    return [
        "1000",  # 1
        "2000",
        "3000",
        "",
        "4000",  # 2
        "",
        "5000",  # 3
        "6000",
        "",
        "7000",  # 4
        "8000",
        "9000",
        "",
        "10000",  # 5
    ], "Elf 4 has the most calories"


def test_day1(data) -> None:
    inp, exp = data
    assert exp == day1(inp)
