from random import randint
from typing import TypeAlias

from character import Character
from question import Question
from data_loader import get_characters, get_questions

"""Types"""
CLIST: TypeAlias = list[Character]
QLIST: TypeAlias = list[list[Question]]
ALIST: TypeAlias = list[str]
CH: TypeAlias = Character
QU: TypeAlias = Question


def __guess(CL: CLIST, char: CH, i: int = 0) -> CH | bool:
    """perform a guess by finding the character with the highest weighting"""
    if i > len(CL) - 1:
        return char
    if CL[i].get_weighting() > char.get_weighting():
        char = CL[i]
    return __guess(CL, char, i + 1)


def __roll(q: list[QU]) -> QU:
    """Determine which question in a category to ask"""
    M: int = len(q) - 1
    i: int = randint(0, M)
    return q[i]


def __ask(CL: CLIST, QL: QLIST, AL: ALIST) -> tuple[CLIST, ALIST]:
    """Ask questions as save answers & results"""
    for QS in QL:
        Q: QU = __roll(QS)
        AL = [*AL, Q.__str__()]
        for i, _ in enumerate(CL):
            CL[i].search_trait(Q.get_type(), Q.get_value())
    return CL, AL


def main() -> None:
    """Play 20 questions with yourself!"""
    CL: CLIST = get_characters()
    QL: QLIST = get_questions()
    AL: ALIST = []
    CL, AL = __ask(CL, QL, AL)
    char: CH | bool = __guess(CL, CL[0])
    if char is False:
        print("No yes questions!")
    else:
        print(f"{char.get_name()}: {char.get_weighting()}")
    print(f"questions asked: {AL}")


if __name__ == "__main__":
    main()
