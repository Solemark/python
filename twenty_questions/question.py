class Question:
    def __init__(self, form: int, question: str) -> None:
        self.__form: int = form
        self.__question: str = question

    def question_prefix(self) -> str:
        match self.__form:
            case 0:
                return "does your character have"
            case 1:
                return "Is your character"
            case 2:
                return "Does your character wear"

    def get_form(self) -> int:
        return self.__form

    def get_question(self) -> str:
        return self.__question

    def get_value(self) -> str:
        val: str = self.__question.split(" ")
        return val[0] if len(val) > 1 else self.__question

    def __str__(self) -> str:
        return f"{self.question_prefix()} {self.__question}"
