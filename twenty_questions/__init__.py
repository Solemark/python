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


def __guess(CL: CLIST) -> CH | bool:
    """perform a guess by finding the character with the highest weighting"""
    char: CH = CL[0]
    for C in CL:
        if C.get_weighting() > char.get_weighting():
            char = C
    return char if char.get_weighting() > 0 else False


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
    char: CH | bool = __guess(CL)
    if char is False:
        print("No yes questions!")
    else:
        print(f"{char.get_name()}: {char.get_weighting()}")
    print(f"questions asked: {AL}")


if __name__ == "__main__":
    main()
