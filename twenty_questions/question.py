class Question:
    def __init__(self, form: int, question: str) -> None:
        self.__form: int = form
        self.__question: str = question

    def __question_prefix(self) -> str:
        match self.__form:
            case 0:
                return "does your character have"
            case 1:
                return "Is your character"
            case 2:
                return "Does your character wear"

    def __str__(self) -> str:
        return f"{self.__question_prefix()} {self.__question}"
