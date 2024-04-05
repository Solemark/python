from enum import Enum, auto


class QType(Enum):
    HAIR = "hair"
    EYES = "eyes"
    SKIN = "skin"
    HEIGHT = "height"
    WEIGHT = "weight"
    SHIRT = "shirt"
    PANTS = "pants"


class FType(Enum):
    HAVE = auto()
    IS = auto()
    WEAR = auto()


class Question:
    def __init__(self, form: FType, question: str, type: QType) -> None:
        self.__form: int = form
        self.__question: str = question
        self.__type: QType = type

    def get_type(self) -> str:
        return self.__type.value

    def question_prefix(self) -> str:
        match self.__form:
            case FType.HAVE:
                return "does your character have"
            case FType.IS:
                return "Is your character"
            case FType.WEAR:
                return "Does your character wear"

    def get_value(self) -> str:
        val: str = self.__question.split(" ")
        return val[0] if len(val) > 1 else self.__question

    def __str__(self) -> str:
        return f"{self.question_prefix()} {self.__question}"
