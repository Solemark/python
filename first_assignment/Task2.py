class Task2:
    __MAX_MARKS: int = 65

    def __init__(self) -> None:
        name: str = input("Enter the name of the student: ")
        mark = int(input(f"Enter {name}'s mark out of {str(self.__MAX_MARKS)}: "))
        p: float = (mark * 100) / self.__MAX_MARKS
        print(f"{name} recieved {str(round(p, 2))}% of the total marks")


if __name__ == "__main__":
    Task2()
