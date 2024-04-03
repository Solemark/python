from unittest import TestCase
from remove_characters import remove


class TestRemoveCharacters(TestCase):
    def test_remove_characters(self) -> None:
        string: str = "Hello World!"
        chars: list[str] = ["l", " ", "!"]
        expect: str = "HeoWord"
        self.assertEqual(expect, remove(string, chars))
