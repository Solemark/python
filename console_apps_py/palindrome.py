def __check_str(input: str, start: int, end: int) -> bool:
    if start > end:
        return True
    if __check_chars(input[start], input[end]) is False:
        return False
    return __check_str(input, start + 1, end - 1)


def __check_chars(x: str, y: str) -> bool:
    return True if x == y else False


def palindrome_fp(input: str) -> bool:
    return __check_str(input, 0, len(input) - 1)


def palindrome(input: str) -> bool:
    for start in range(len(input) - 1):
        if input[start] != input[(len(input) - 1) - start]:
            return False
    return True
