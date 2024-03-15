from functools import reduce

ALPHABET: dict = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
    "e": 5,
    "f": 6,
    "g": 7,
    "h": 8,
    "i": 9,
    "j": 10,
    "k": 11,
    "l": 12,
    "m": 13,
    "n": 14,
    "o": 15,
    "p": 16,
    "q": 17,
    "r": 18,
    "s": 19,
    "t": 20,
    "u": 21,
    "v": 22,
    "w": 23,
    "x": 24,
    "y": 25,
    "z": 26,
}


def day3(data: list[str]) -> int:
    return reduce(__add, [__split_string(item) for item in data])


def __add(x: int, y: int) -> int:
    return x + y


def __split_string(S: str) -> int:
    chars: list[str] = []
    LS: str = __split_str(0, int(len(S) / 2) - 1, S)
    RS: str = __split_str(int(len(S) / 2), len(S) - 1, S)
    return reduce(__add, [__calc(LC, RS, chars) for LC in LS])


def __split_str(J: int, E: int, IN: str, OUT: str = "") -> str:
    return OUT if J > E else __split_str(J + 1, E, IN, OUT + IN[J])


def __calc(LC: str, RS: str, chars: list[str]) -> int:
    if LC in RS and LC not in chars:
        chars.append(LC)
        return __get_points(LC)
    return 0


def __get_points(C: str) -> int:
    return __fetch_points(C) + 26 if C == C.upper() else __fetch_points(C)


def __fetch_points(C: str) -> int:
    return ALPHABET[C.lower()]
