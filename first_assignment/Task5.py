from tkinter import messagebox, StringVar, Tk, Entry, Label, Button


class Task5:
    __total: int
    __student_num: int
    __avg: StringVar
    __grade: StringVar

    def __init__(self) -> None:
        window = Tk()
        self.__total = 0
        self.__student_num = 0
        self.__avg = StringVar()
        self.__grade = StringVar()
        window.title("Mark Entry System 2.0")
        Label(window, text="Welcome to the mark entry system 2.0!").pack()
        Label(window, text="Please enter the student's grade between 0-100").pack()
        grade = Entry(window, textvariable=self.__grade)
        grade.pack()
        self.__avg.set("The average grade for students is: 0")
        Label(window, textvariable=self.__avg).pack()
        Button(window, text="Enter", command=self.__get_grade).pack()
        window.mainloop()

    def __get_grade(self) -> None:
        if int(self.__grade.get()) <= 49:
            messagebox.showinfo("Student Grade", "Student has failed (F)")
        elif int(self.__grade.get()) <= 64:
            messagebox.showinfo("Student Grade", "Student has passed (P)")
        elif int(self.__grade.get()) <= 74:
            messagebox.showinfo("Student Grade", "Student has recieved a Credit (C)")
        elif int(self.__grade.get()) <= 84:
            messagebox.showinfo(
                "Student Grade", "Student has recieved a Distinction (D)"
            )
        else:
            messagebox.showinfo(
                "Student Grade", "Student has recieved a High Distinction (HD)"
            )
        self.__student_num += 1
        self.__total += int(self.__grade.get())
        self.__avg.set(
            f"The average grade for students is: {str(round(self.__total/self.__student_num, 2))}"
        )


if __name__ == "__main__":
    Task5()
