from unittest import TestCase

from isomorphic_string import is_isomorphic


class TestIsoString(TestCase):
    def test_is_isomorphic(self) -> None:
        data: list[list[str | bool]] = [
            ["egg", "add", True],
            ["foo", "bar", False],
            ["paper", "title", True],
        ]
        for item in data:
            result: bool = is_isomorphic(str(item[0]), str(item[1]))
            self.assertEqual(item[2], result)
