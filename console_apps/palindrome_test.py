from unittest import TestCase
from palindrome import palindrome_fp, palindrome


class TestCheckPalindrome(TestCase):
    def setUp(self) -> None:
        self.data: list[tuple[str, bool]] = [
            ("DAD", True),
            ("Dad", False),
            ("ABCDCBA", True),
            ("ABCDcba", False),
        ]

    def test_is_palindrome_fp(self) -> None:
        for item in self.data:
            self.assertEqual(item[1], palindrome_fp(item[0]))

    def test_is_palindrome(self) -> None:
        for item in self.data:
            self.assertEqual(item[1], palindrome(item[0]))
