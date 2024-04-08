from random import randint

from data_loader import get_data
from stub import CList, QList, AList, Ch, Qu


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


def __ask(CL: CList, QL: QList, AL: AList = [], i: int = 0) -> tuple[CList, AList]:
    """Ask questions and save answers"""
    if i > len(QL) - 1:
        return CL, AL
    Q: Qu = __roll(QL[i])
    CL = __search(CL, Q)
    return __ask(CL, QL, [*AL, Q.__str__()], i + 1)


def __roll(q: list[Qu]) -> Qu:
    """Determine which question in a category to ask"""
    return q[randint(0, len(q) - 1)]


def __search(CL: CList, Q: Qu, i: int = 0) -> CList:
    """Search for Characters with the Trait"""
    if i > len(CL) - 1:
        return CL
    CL[i].search_trait(Q.get_type(), Q.get_value())
    return __search(CL, Q, i + 1)


def __guess(CL: CList, char: Ch, i: int = 1) -> Ch:
    """perform a guess by finding the character with the highest weighting"""
    if i > len(CL) - 1:
        return char
    if CL[i].get_weighting() > char.get_weighting():
        return __guess(CL, CL[i], i + 1)
    return __guess(CL, char, i + 1)


if __name__ == "__main__":
    main()
