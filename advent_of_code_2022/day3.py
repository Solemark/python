from string import ascii_lowercase


def day3(data: list[str]) -> int:
    total: int = 0
    for item in data:
        chars: list[str] = []
        length: int = len(item)
        LS: str = __split_str(0, int(length / 2) - 1, item)
        RS: str = __split_str(int(length / 2), length - 1, item)
        for LC in LS:
            total += __calc(LC, RS, chars)
    return total


def __split_str(J: int, E: int, IN: str) -> str:
    output: str = ""
    while J <= E:
        output += IN[J]
        J += 1
    return output


def __calc(LC: str, RS: str, chars: list[str]) -> int:
    if LC in RS and LC not in chars:
        chars.append(LC)
        return __alphabet_index(LC) + 26 if LC == LC.upper() else __alphabet_index(LC)
    return 0


def __alphabet_index(char: str) -> int:
    return ascii_lowercase.index(char.lower()) + 1
