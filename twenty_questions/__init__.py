from random import randint

from character import Character
from question import Question
from data_loader import load_characters, load_questions


def __roll(q: list[Question]) -> Question:
    M: int = len(q) - 1
    i: int = randint(0, M)
    return q[i]


def main() -> None:
    CLIST: list[Character] = load_characters()
    QLIST: list[list[Question]] = load_questions()
    ALIST: list[str] = []
    char: Character = CLIST[0]
    for QS in QLIST:
        Q: Question = __roll(QS)
        ALIST = [*ALIST, Q.__str__()]
        for i, C in enumerate(CLIST):
            CLIST[i].search_trait(Q.get_type(), Q.get_value())
    for C in CLIST:
        char = C if C.get_weighting() > char.get_weighting() else char
    print(f"{char.get_name()}: {char.get_weighting()}")
    print(f"questions asked: {ALIST}")


if __name__ == "__main__":
    main()
