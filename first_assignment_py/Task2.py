class Task2:
    def __init__(self) -> None:
        __MAX_MARKS__: int = 65
        name: str = input("Enter the name of the student: ")
        mark = int(input(f"Enter {name}'s mark out of {str(__MAX_MARKS__)}: "))
        p: float = (mark * 100) / __MAX_MARKS__
        print(f"{name} recieved {str(round(p, 2))}% of the total marks")
