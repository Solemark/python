from random import randint

from character import Character
from question import Question
from data_loader import load_characters, load_questions


def __roll(q: list[Question]) -> Question:
    M: int = len(q) - 1
    i: int = randint(0, M)
    return q[i]


def main() -> None:
    characters: list[Character] = load_characters()
    questions: list[list[Question]] = load_questions()
    asked: list[str] = []
    for Q in questions:
        q: Question = __roll(Q)
        asked = [*asked, q.__str__()]
        for i, C in enumerate(characters):
            characters[i].search_trait(q.get_type(), q.get_value())
    for C in characters:
        print(f"{C.get_name()}: {C.get_weighting()}")
    print(f"questions asked: {asked}")


if __name__ == "__main__":
    main()
