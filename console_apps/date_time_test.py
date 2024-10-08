from pytest import fixture
from date_time import datetime
from date_time import get_current_time, format_date


@fixture
def dates() -> list[tuple[int, str]]:
    return [
        (1, "1st"),
        (2, "2nd"),
        (3, "3rd"),
        (4, "4th"),
        (10, "10th"),
        (11, "11th"),
        (12, "12th"),
        (13, "13th"),
        (14, "14th"),
        (30, "30th"),
        (31, "31st"),
    ]


def test_current_time() -> None:
    now: datetime = datetime.now()
    expect = (
        f"The date is: {now.strftime('%A')} "
        f"the {format_date(now.day)} "
        f"of { now.strftime('%B')} "
        f"{now.year}"
    )
    assert expect == get_current_time()


def test_format_date(dates: list[tuple[int, str]]) -> None:
    for i in dates:
        assert format_date(i[0]) == i[1]
