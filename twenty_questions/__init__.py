from random import randint

from character import Character
from question import Question
from data_loader import load_characters, load_questions


def __roll(q: list[Question]) -> Question:
    M: int = len(q) - 1
    i: int = randint(0, M)
    return q[i]


def main() -> None:
    CL: list[Character] = load_characters()
    QL: list[list[Question]] = load_questions()
    QA: list[str] = []
    c: Character = CL[0]
    for QS in QL:
        Q: Question = __roll(QS)
        QA = [*QA, Q.__str__()]
        for i, C in enumerate(CL):
            CL[i].search_trait(Q.get_type(), Q.get_value())
    for C in CL:
        c = C if C.get_weighting() > c.get_weighting() else c
    print(f"{c.get_name()}: {c.get_weighting()}")
    print(f"questions asked: {QA}")


if __name__ == "__main__":
    main()
