from character import Character
from question import Question, FType, QType


def get_characters() -> list[Character]:
    return [
        Character(
            name="Kratos",
            eyes="green",
            gender="male",
            hair="brown",
            height="tall",
            pants="black",
            shirt="none",
            skin="white",
            weight="shredded",
        ),
        Character(
            name="Homura",
            eyes="purple",
            gender="female",
            hair="black",
            height="short",
            pants="black",
            shirt="white",
            skin="white",
            weight="thin",
        ),
    ]


def get_questions() -> list[list[Question]]:
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
            Question(FType.IS, "average", QType.HEIGHT),
            Question(FType.IS, "tall", QType.HEIGHT),
        ],
        [
            Question(FType.IS, "thin", QType.WEIGHT),
            Question(FType.IS, "average", QType.WEIGHT),
            Question(FType.IS, "fat", QType.WEIGHT),
            Question(FType.IS, "shredded", QType.WEIGHT),
        ],
        [
            Question(FType.IS, "male", QType.GENDER),
            Question(FType.IS, "female", QType.GENDER),
            Question(FType.IS, "non-binary", QType.GENDER),
        ],
        [
            Question(FType.WEAR, "red shirts", QType.SHIRT),
            Question(FType.WEAR, "green shirts", QType.SHIRT),
            Question(FType.WEAR, "blue shirts", QType.SHIRT),
            Question(FType.WEAR, "no shirt", QType.SHIRT),
        ],
        [
            Question(FType.WEAR, "red pants", QType.PANTS),
            Question(FType.WEAR, "green pants", QType.PANTS),
            Question(FType.WEAR, "blue pants", QType.PANTS),
            Question(FType.WEAR, "no pants", QType.PANTS),
        ],
    ]
