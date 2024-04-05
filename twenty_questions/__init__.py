from random import randint

from character import Character
from question import Question, QType


def __load_characters() -> list[Character]:
    return [
        Character(
            "Timmy",
            "blonde",
            "brown",
            "white",
            "short",
            "thin",
            "red",
            "blue",
        )
    ]


def __load_questions() -> list[list[Question]]:
    return [
        [
            Question(0, "blonde hair", QType.HAIR),
            Question(0, "brown hair", QType.HAIR),
            Question(0, "black hair", QType.HAIR),
        ],
        [
            Question(0, "brown eyes", QType.EYES),
            Question(0, "blue eyes", QType.EYES),
            Question(0, "black eyes", QType.EYES),
        ],
        [
            Question(0, "white skin", QType.SKIN),
            Question(0, "dark skin", QType.SKIN),
        ],
        [
            Question(1, "short", QType.HEIGHT),
            Question(1, "tall", QType.HEIGHT),
        ],
        [
            Question(1, "thin", QType.WEIGHT),
            Question(1, "fat", QType.WEIGHT),
        ],
        [
            Question(2, "red shirts", QType.SHIRT),
            Question(2, "green shirts", QType.SHIRT),
            Question(2, "blue shirts", QType.SHIRT),
        ],
        [
            Question(2, "red pants", QType.PANTS),
            Question(2, "green pants", QType.PANTS),
            Question(2, "blue pants", QType.PANTS),
        ],
    ]


def __roll(q: list[Question]) -> Question:
    M: int = len(q) - 1
    i: int = randint(0, M)
    return q[i]


def main() -> None:
    characters: list[Character] = __load_characters()
    questions: list[list[Question]] = __load_questions()
    asked: list[str] = []
    for Q in questions:
        q: Question = __roll(Q)
        asked = [*asked, q.__str__()]
        for i, C in enumerate(characters):
            characters[i].search_trait(q.get_type().value, q.get_value())
    for C in characters:
        print(f"{C.get_name()}: {C.get_weighting()}")
    print(f"questions asked: {asked}")


if __name__ == "__main__":
    main()
