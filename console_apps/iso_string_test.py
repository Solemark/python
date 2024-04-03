from unittest import TestCase

from iso_string import is_iso


class TestIsoString(TestCase):
    def test_is_isomorphic(self) -> None:
        data: list[list[str | bool]] = [
            ["egg", "add", True],
            ["foo", "bar", False],
            ["paper", "title", True],
        ]
        for item in data:
            result: bool = is_iso(str(item[0]), str(item[1]))
            self.assertEqual(item[2], result)
