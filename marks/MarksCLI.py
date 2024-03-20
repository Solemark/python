from enum import Enum
from Mark import Mark


class Op(Enum):
    """Enum for __init__() case"""

    NEW = 1
    SEARCH = 2
    LIST = 3


class MarksCLI:
    """CLI frontend for the Mark Entry System 3.0"""

    __students: list[Mark]
    __INSTR: list[str] = [
        "1 to add new student",
        "2 to search existing booking",
        "3 to list all bookings",
        "Enter any other key to quit",
    ]

    def __init__(self) -> None:
        self.__students = []
        print("Mark Entry System 3.0")
        while True:
            CMD: int = int(input(f"{self.__linebreak()}\n{', '.join(self.__INSTR)}"))
            match CMD:
                case Op.NEW:
                    self.__students = [*self.__students, self.__new()]
                case Op.SEARCH:
                    print(self.__search())
                case Op.LIST:
                    print(self.__students)
                case _:
                    exit(0)

    def __linebreak(self) -> str:
        """Function that creates a string linebreak"""
        return "__________"

    def __new(self) -> Mark:
        """Create and return a new Student"""
        print("Enter student details")
        return Mark(input("Name: "), int(input("Mark: ")))

    def __search(self) -> Mark | str:
        """Finds the Student from the student list"""
        out: Mark | str
        inp: str = input("Enter student name to search:")
        for student in self.__students:
            if inp == student.get_student_name():
                out = student
                break
        return out


if __name__ == "__main__":
    MarksCLI()
