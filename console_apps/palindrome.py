def palindrome_fp(s: str, i: int = 0, j: int | None = None) -> bool:
    if j is None:
        j = len(s) - 1
    if i >= j:
        return True
    if s[i] != s[j]:
        return False
    return palindrome_fp(s, i + 1, j - 1)


def palindrome(s: str) -> bool:
    for i in range(len(s) - 1):
        a = s[i]
        b = s[(len(s) - 1) - i]
        if a != b:
            return False
    return True
