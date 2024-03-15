class Task4:
    def __init__(self) -> None:
        total: int = 0
        count: int = 0
        print("Mark Entry System \n enter a mark above 100 to close the system")
        while True:
            name = input("Enter student name: ")
            grade = int(input("Enter student grade (0-100): "))
            print("")
            if grade > 100:
                break
            elif grade <= 49:
                print(name + " has failed(F)")
            elif grade <= 64:
                print(name + " has passed(P)")
            elif grade <= 74:
                print(name + " has recieved a Credit(C)")
            elif grade <= 84:
                print(name + " has recieved a Distinction(D)")
            else:
                print(name + " has recieved a High Distinction(HD)")
            count += 1
            total += grade
        avgGrade = total / count
        print(f"The average student grade is: {str(round(avgGrade, 2))}")
