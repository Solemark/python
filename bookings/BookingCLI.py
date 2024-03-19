from Booking import Luxury


class BookingCLI:
    """CLI frontend for the Bookings system"""

    INSTR: list[str] = [
        "1 to add new booking",
        "2 to search existing booking",
        "3 to list all bookings",
        "4 to update a booking",
        "5 to remove a booking",
        "Enter any other key to quit",
    ]
    bookings: list[Luxury]

    def __init__(self) -> None:
        self.bookings = []
        while True:
            CMD: str = input(f"{self.__linebreak()}\n{', '.join(self.INSTR)}\n")
            match CMD:
                case "1":
                    self.bookings = [*self.bookings, self.__new()]
                case "2":
                    print(self.__search())
                case "3":
                    print(self.__list())
                case "4":
                    self.bookings = self.__update()
                case "5":
                    self.bookings = self.__remove()
                case _:
                    exit(0)

    def __linebreak(self) -> str:
        """Function that creates a string linebreak"""
        return "__________"

    def __new(self) -> Luxury:
        """Creates a new Luxury object"""
        ID: str = input("Enter Booking ID: ")
        DATE: str = input("Enter Booking Date: ")
        WEEKS: str = input("Enter Number of Weeks: ")
        OWNER: str = input("Enter Property Owner Name: ")
        PHONE: str = input("Enter Contact Number: ")
        ADDR: str = input("Enter Booking Address: ")
        ROOMS: str = input("Enter Number of Rooms: ")
        AREA: str = input("Enter Garden Area: ")
        ALARM: str = input("Perform Security Alarm Check? (Y/N): ")
        POOL: str = input("Perform Pool Maintenance (Y/N): ")

        return Luxury(
            ID,
            DATE,
            int(WEEKS),
            OWNER,
            PHONE,
            ADDR,
            int(ROOMS),
            int(AREA),
            True if ALARM.upper() == "Y" else False,
            True if POOL.upper() == "Y" else False,
        )

    def __search(self) -> Luxury | str:
        """Finds the Luxury object from the bookings list"""
        ID: str = input("Enter Booking ID to search: ")
        for booking in self.bookings:
            if ID == booking.get_booking_id():
                return booking
        return "Invalid Booking ID!"

    def __list(self) -> str:
        """Returns all Luxury objects as a string"""
        return "\n".join(booking.__str__() for booking in self.bookings)

    def __update(self) -> list[Luxury]:
        """Updates an existing Luxury in the bookings list"""
        ID: str = input("Enter Booking ID to update: ")
        for i, booking in enumerate(self.bookings):
            if ID == booking.get_booking_id():
                self.bookings[i] = self.__new()
        return self.bookings

    def __remove(self) -> list[Luxury]:
        """Remove a Luxury from the bookings list"""
        ID: str = input("Enter Booking ID to remove: ")
        return [booking for booking in self.bookings if booking.get_booking_id() != ID]


if __name__ == "__main__":
    BookingCLI()
