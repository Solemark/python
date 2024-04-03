from character import Character
from traits import Traits


def __load_characters() -> list[Character]:
    return [
        Character(
            "Timmy",
            Traits(
                "blonde",
                "brown",
                "white",
                "short",
                "thin",
                "red",
                "brown",
            ),
        )
    ]


def __validate(s: str) -> bool:
    return s.lower() == "y"


def main() -> None:
    characters: list[Character] = __load_characters()
    questions: list[str] = [
        "Is you character blonde?"
        "Does your character have brown eyes?"
        "Is you character white?"
        "Is you character short?"
        "Is you character thin?"
        "Does your character wear a red shirt?"
        "Does your character wear brown pants?"
    ]
    print("Answer yes(y) or no(n) to questions")
    for q in questions:
        RES: bool = __validate(input(f"{q} "))
        # TODO - What question did I just ask?
        # TODO - check when this is true against the characters


if __name__ == "__main__":
    main()
