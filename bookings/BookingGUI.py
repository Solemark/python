from tkinter import Tk, Label, Entry, StringVar, Button, Checkbutton, BooleanVar
from Booking import Luxury


class BookingGUI:
    __booking_id: StringVar
    __booking_date: StringVar
    __num_weeks: StringVar
    __property_owner_name: StringVar
    __contact_number: StringVar
    __address: StringVar
    __rooms: StringVar
    __garden_area: StringVar
    __security_alarm_check: BooleanVar
    __pool_maintenance: BooleanVar
    __booking_list: list[Luxury]

    __rooms_cost: StringVar
    __garden_area_cost: StringVar
    __total_price: StringVar
    __display_all: StringVar

    def __init__(self) -> None:
        master = Tk()
        master.title("NQ-RE Services Calculator")

        self.__b_id = StringVar()
        self.__date = StringVar()
        self.__weeks = StringVar()
        self.__owner = StringVar()
        self.__number = StringVar()
        self.__address = StringVar()
        self.__rooms = StringVar()
        self.__area = StringVar()
        self.__alarm = BooleanVar()
        self.__pool = BooleanVar()
        self.__booking_list = []
        self.__rooms_cost = StringVar()
        self.__garden_area_cost = StringVar()
        self.__total_price = StringVar()
        self.__display_all = StringVar()

        Label(master, text="Please enter your booking details").grid(
            row=0, columnspan=2
        )
        Label(master, text="BookingId: ").grid(row=1, column=0)
        Entry(master, textvariable=self.__b_id).grid(row=1, column=1)
        Label(master, text="Booking Date: ").grid(row=2, column=0)
        Entry(master, textvariable=self.__date).grid(row=2, column=1)
        Label(master, text="Weeks: ").grid(row=3, column=0)
        Entry(master, textvariable=self.__weeks).grid(row=3, column=1)
        Label(master, text="Owner Name: ").grid(row=4, column=0)
        Entry(master, textvariable=self.__owner).grid(row=4, column=1)
        Label(master, text="Contact Number: ").grid(row=5, column=0)
        Entry(master, textvariable=self.__number).grid(row=5, column=1)
        Label(master, text="Address: ").grid(row=6, column=0)
        Entry(master, textvariable=self.__address).grid(row=6, column=1)
        Label(master, text="Rooms: ").grid(row=7, column=0)
        Entry(master, textvariable=self.__rooms).grid(row=7, column=1)
        Label(master, text="Garden Area: ").grid(row=8, column=0)
        Entry(master, textvariable=self.__area).grid(row=8, column=1)
        Button(master, text="Submit", command=self.__submit).grid(
            row=9, column=0, columnspan=1
        )
        Button(master, text="Clear", command=self.__clear).grid(
            row=9, column=1, columnspan=1
        )
        Button(master, text="Display", command=self.__display).grid(
            row=10, column=0, columnspan=1
        )
        Button(master, text="Exit", command=self.__exit).grid(
            row=10, column=1, columnspan=1
        )
        Checkbutton(
            master,
            text="Security Check",
            variable=self.__alarm,
            onvalue=True,
            offvalue=False,
        ).grid(row=11, column=0, columnspan=1)
        Checkbutton(
            master,
            text="Pool Maintenance",
            variable=self.__pool,
            onvalue=True,
            offvalue=False,
        ).grid(row=11, column=1, columnspan=1)
        Label(master, text="Rooms Cost: ").grid(row=12, column=0, columnspan=1)
        Label(master, textvariable=self.__rooms_cost).grid(
            row=12, column=1, columnspan=1
        )
        Label(master, text="Garden Area Cost: ").grid(row=13, column=0, columnspan=1)
        Label(master, textvariable=self.__garden_area_cost).grid(
            row=13, column=1, columnspan=1
        )
        Label(master, text="Total Price: ").grid(row=14, column=0, columnspan=1)
        Label(master, textvariable=self.__total_price).grid(
            row=14, column=1, columnspan=1
        )
        Label(master, textvariable=self.__display_all).grid(row=15, columnspan=2)
        master.mainloop()

    def __submit(self) -> None:
        """Adds the current booking to the list"""
        self.__booking_list.append(
            Luxury(
                b_id=self.__b_id.get(),
                date=self.__date.get(),
                weeks=int(self.__weeks.get()),
                owner=self.__owner.get(),
                number=self.__number.get(),
                address=self.__address.get(),
                rooms=int(self.__rooms.get()),
                area=float(self.__area.get()),
                alarm=self.__alarm.get(),
                pool=self.__pool.get(),
            )
        )
        self.__calculation(self.__booking_list[-1])
        self.__clear()

    def __clear(self) -> None:
        """clears the GUI input fields"""
        self.__b_id.set("")
        self.__date.set("")
        self.__weeks.set("")
        self.__owner.set("")
        self.__number.set("")
        self.__address.set("")
        self.__rooms.set("")
        self.__area.set("")
        self.__alarm.set(False)
        self.__pool.set(False)
        self.__display_all.set("")

    def __display(self) -> None:
        """display's the GUI details"""
        self.__display_all.set(
            "\n".join(booking.__str__() for booking in self.__booking_list)
        )

    def __exit(self) -> None:
        """exit the GUI"""
        exit(0)

    def __calculation(self, booking: Luxury) -> None:
        """
        get the calculation data from input
        @param Luxury booking
        @returns None
        """
        room_cost: float = booking.get_rooms_cost()
        garden_area_cost: float = booking.get_area_cost()
        total: float = (room_cost + garden_area_cost) * booking.get_weeks()
        self.__rooms_cost.set(str(room_cost))
        self.__garden_area_cost.set(str(garden_area_cost))
        self.__total_price.set(str(total + booking.get_luxury_cost()))


if __name__ == "__main__":
    BookingGUI()
