class Task3:
    def __init__(self) -> None:
        grade: int = int(input("Please enter the student's grade(0-100): "))
        if grade <= 49:
            print("Student has failed(F)")
        elif grade <= 64:
            print("Student has passed(P)")
        elif grade <= 74:
            print("Student has recieved a Credit(C)")
        elif grade <= 84:
            print("Student has recieved a Distinction(D)")
        else:
            print("Student has recieved a High Distinction(HD)")
