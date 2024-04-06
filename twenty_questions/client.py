from random import randint

from data_loader import get_data
from stub import CList, QList, AList, Ch, Qu


def __guess(CL: CList, char: Ch, i: int = 1) -> Ch:
    """perform a guess by finding the character with the highest weighting"""
    if i > len(CL) - 1:
        return char
    if CL[i].get_weighting() > char.get_weighting():
        return __guess(CL, CL[i], i + 1)
    return __guess(CL, char, i + 1)


def __roll(q: list[Qu]) -> Qu:
    """Determine which question in a category to ask"""
    M: int = len(q) - 1
    i: int = randint(0, M)
    return q[i]


def __ask(CL: CList, QL: QList, AL: AList = []) -> tuple[CList, AList]:
    """Ask questions as save answers & results"""
    for QS in QL:
        Q: Qu = __roll(QS)
        AL = [*AL, Q.__str__()]
        for i, _ in enumerate(CL):
            CL[i].search_trait(Q.get_type(), Q.get_value())
    return CL, AL


def main() -> None:
    """Watch the computer play 20 questions with itself!"""
    CL, QL = get_data()
    CL, AL = __ask(CL, QL)
    char: Ch = __guess(CL, CL[0])
    if char.get_weighting() == 0:
        """No correct questions! Pretend it didnt happen!"""
        main()
    print(f"{char.get_name()}: {char.get_weighting()}")
    print(f"questions asked: {AL}")


if __name__ == "__main__":
    main()
