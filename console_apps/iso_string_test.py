from unittest import TestCase

from iso_string import is_iso


class TestIsoString(TestCase):
    def setUp(self) -> None:
        self.data: list[list[str | bool]] = [
            ["egg", "add", True],
            ["foo", "bar", False],
            ["paper", "title", True],
        ]

    def test_is_isomorphic(self) -> None:
        for item in self.data:
            result: bool = is_iso(str(item[0]), str(item[1]))
            self.assertEqual(item[2], result)
