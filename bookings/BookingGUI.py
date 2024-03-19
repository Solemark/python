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

        self.__booking_id = StringVar()
        self.__booking_date = StringVar()
        self.__num_weeks = StringVar()
        self.__property_owner_name = StringVar()
        self.__contact_number = StringVar()
        self.__address = StringVar()
        self.__rooms = StringVar()
        self.__garden_area = StringVar()
        self.__security_alarm_check = BooleanVar()
        self.__pool_maintenance = BooleanVar()
        self.__booking_list = []
        self.__rooms_cost = StringVar()
        self.__garden_area_cost = StringVar()
        self.__total_price = StringVar()
        self.__display_all = StringVar()

        Label(master, text="Please enter your booking details").grid(
            row=0, columnspan=2
        )
        Label(master, text="BookingId: ").grid(row=1, column=0)
        Entry(master, textvariable=self.__booking_id).grid(row=1, column=1)
        Label(master, text="Booking Date: ").grid(row=2, column=0)
        Entry(master, textvariable=self.__booking_date).grid(row=2, column=1)
        Label(master, text="Weeks: ").grid(row=3, column=0)
        Entry(master, textvariable=self.__num_weeks).grid(row=3, column=1)
        Label(master, text="Owner Name: ").grid(row=4, column=0)
        Entry(master, textvariable=self.__property_owner_name).grid(row=4, column=1)
        Label(master, text="Contact Number: ").grid(row=5, column=0)
        Entry(master, textvariable=self.__contact_number).grid(row=5, column=1)
        Label(master, text="Address: ").grid(row=6, column=0)
        Entry(master, textvariable=self.__address).grid(row=6, column=1)
        Label(master, text="Rooms: ").grid(row=7, column=0)
        Entry(master, textvariable=self.__rooms).grid(row=7, column=1)
        Label(master, text="Garden Area: ").grid(row=8, column=0)
        Entry(master, textvariable=self.__garden_area).grid(row=8, column=1)
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
            variable=self.__security_alarm_check,
            onvalue=True,
            offvalue=False,
        ).grid(row=11, column=0, columnspan=1)
        Checkbutton(
            master,
            text="Pool Maintenance",
            variable=self.__pool_maintenance,
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
        """
        Adds the current booking to the list
        """
        self.__booking_list.append(
            Luxury(
                self.__booking_id.get(),
                self.__booking_date.get(),
                int(self.__num_weeks.get()),
                self.__property_owner_name.get(),
                self.__contact_number.get(),
                self.__address.get(),
                int(self.__rooms.get()),
                int(self.__garden_area.get()),
                security_alarm_check=self.__security_alarm_check.get(),
                pool_maintenance=self.__pool_maintenance.get(),
            )
        )
        self.__calculation(self.__booking_list[-1])
        self.__clear()

    def __clear(self) -> None:
        """
        clears the GUI input fields
        """
        self.__booking_id.set("")
        self.__booking_date.set("")
        self.__num_weeks.set("")
        self.__property_owner_name.set("")
        self.__contact_number.set("")
        self.__address.set("")
        self.__rooms.set("")
        self.__garden_area.set("")
        self.__security_alarm_check.set(False)
        self.__pool_maintenance.set(False)
        self.__display_all.set("")

    def __display(self) -> None:
        """
        display's the GUI details
        """
        self.__display_all.set(
            "\n".join(booking.__str__() for booking in self.__booking_list)
        )

    def __exit(self) -> None:
        """
        exit the GUI
        """
        exit(0)

    def __calculation(self, booking: Luxury) -> None:
        """
        get the calculation data from input
        @param Luxury booking
        @returns None
        """
        room_cost: float = booking.get_rooms_cost()
        garden_area_cost: float = booking.get_garden_area_cost()
        total: float = (room_cost + garden_area_cost) * booking.get_num_weeks()
        self.__rooms_cost.set(str(room_cost))
        self.__garden_area_cost.set(str(garden_area_cost))
        self.__total_price.set(str(total + booking.get_luxury_cost()))


if __name__ == "__main__":
    BookingGUI()
