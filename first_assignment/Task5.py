from tkinter import messagebox, StringVar, Tk, Entry, Label, Button


class Task5:
    __totalGrade: int
    __sNumber: int
    __avgTest: StringVar
    __stu_grade: StringVar

    def __init__(self) -> None:
        window = Tk()
        self.__totalGrade = 0
        self.__sNumber = 0
        self.__avgTest = StringVar()
        self.__stu_grade = StringVar()
        window.title("Mark Entry System 2.0")
        Label(window, text="Welcome to the mark entry system 2.0!").pack()
        Label(window, text="Please enter the student's grade between 0-100").pack()
        grade = Entry(window, textvariable=self.__stu_grade)
        grade.pack()
        self.avgText = StringVar()
        self.avgText.set("The average grade for students is: 0")
        Label(window, textvariable=self.avgText).pack()
        Button(window, text="Enter", command=self.__getGrade).pack()
        window.mainloop()

    def __getGrade(self) -> None:
        if int(self.__stu_grade.get()) <= 49:
            messagebox.showinfo("Student Grade", "Student has failed (F)")
        elif int(self.__stu_grade.get()) <= 64:
            messagebox.showinfo("Student Grade", "Student has passed (P)")
        elif int(self.__stu_grade.get()) <= 74:
            messagebox.showinfo("Student Grade", "Student has recieved a Credit (C)")
        elif int(self.__stu_grade.get()) <= 84:
            messagebox.showinfo(
                "Student Grade", "Student has recieved a Distinction (D)"
            )
        else:
            messagebox.showinfo(
                "Student Grade", "Student has recieved a High Distinction (HD)"
            )
        self.__sNumber += 1
        self.__totalGrade += int(self.__stu_grade.get())
        self.avgText.set(
            f"The average grade for students is: {str(round(self.__totalGrade/self.__sNumber, 2))}"
        )


if __name__ == "__main__":
    Task5()
