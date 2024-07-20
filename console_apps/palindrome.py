def palindrome_fp(s: str, i: int = 0, j: int | None = None) -> bool:
    if j is None:
        j = len(s) - 1
    if i >= j:
        return True
    if __check_chars(s[i], s[j]):
        return False
    return palindrome_fp(s, i + 1, j - 1)


def __check_chars(x: str, y: str) -> bool:
    return x != y


def palindrome(s: str) -> bool:
    for i in range(len(s) - 1):
        if __check_chars(s[i], s[(len(s) - 1) - i]):
            return False
    return True
