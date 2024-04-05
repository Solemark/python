from random import randint

from character import Character
from question import Question, FType, QType


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
            Question(FType.HAVE, "blonde hair", QType.HAIR),
            Question(FType.HAVE, "brown hair", QType.HAIR),
            Question(FType.HAVE, "black hair", QType.HAIR),
        ],
        [
            Question(FType.HAVE, "brown eyes", QType.EYES),
            Question(FType.HAVE, "blue eyes", QType.EYES),
            Question(FType.HAVE, "black eyes", QType.EYES),
        ],
        [
            Question(FType.HAVE, "white skin", QType.SKIN),
            Question(FType.HAVE, "dark skin", QType.SKIN),
        ],
        [
            Question(FType.IS, "short", QType.HEIGHT),
            Question(FType.IS, "tall", QType.HEIGHT),
        ],
        [
            Question(FType.IS, "thin", QType.WEIGHT),
            Question(FType.IS, "fat", QType.WEIGHT),
        ],
        [
            Question(FType.WEAR, "red shirts", QType.SHIRT),
            Question(FType.WEAR, "green shirts", QType.SHIRT),
            Question(FType.WEAR, "blue shirts", QType.SHIRT),
        ],
        [
            Question(FType.WEAR, "red pants", QType.PANTS),
            Question(FType.WEAR, "green pants", QType.PANTS),
            Question(FType.WEAR, "blue pants", QType.PANTS),
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
            characters[i].search_trait(q.get_type(), q.get_value())
    for C in characters:
        print(f"{C.get_name()}: {C.get_weighting()}")
    print(f"questions asked: {asked}")


if __name__ == "__main__":
    main()
