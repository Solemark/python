from unittest import TestCase
from date_time import datetime
from date_time import get_current_time, format_date


class TestDateTime(TestCase):
    def test_current_time(self) -> None:
        CURRENT_TIME = datetime.now()
        self.assertEqual(
            get_current_time(),
            (
                f"The date is: {CURRENT_TIME.strftime('%A')} "
                f"the {format_date(CURRENT_TIME.day)} "
                f"of { CURRENT_TIME.strftime('%B')} "
                f"{CURRENT_TIME.year}"
            ),
        )

    def test_format_date(self) -> None:
        self.assertEqual(format_date(1), "1st")
        self.assertEqual(format_date(2), "2nd")
        self.assertEqual(format_date(3), "3rd")
        self.assertEqual(format_date(4), "4th")
        self.assertEqual(format_date(10), "10th")
        self.assertEqual(format_date(11), "11th")
        self.assertEqual(format_date(12), "12th")
        self.assertEqual(format_date(13), "13th")
        self.assertEqual(format_date(14), "14th")
        self.assertEqual(format_date(30), "30th")
        self.assertEqual(format_date(31), "31st")
