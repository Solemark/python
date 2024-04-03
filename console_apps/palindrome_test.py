from unittest import TestCase
from palindrome import palindrome_fp, palindrome


class TestCheckPalindrome(TestCase):
    def test_is_palindrome_fp(self) -> None:
        self.assertEqual(True, palindrome_fp("DAD"))
        self.assertEqual(False, palindrome_fp("Dad"))
        self.assertEqual(True, palindrome_fp("ABCDCBA"))
        self.assertEqual(False, palindrome_fp("ABCDcba"))

    def test_is_palindrome(self) -> None:
        self.assertEqual(True, palindrome("DAD"))
        self.assertEqual(False, palindrome("Dad"))
        self.assertEqual(True, palindrome("ABCDCBA"))
        self.assertEqual(False, palindrome("ABCDcba"))
