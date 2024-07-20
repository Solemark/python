class Booking:
    def __init__(
        self,
        b_id: str,
        date: str,
        weeks: int,
        owner: str,
        number: str,
        address: str,
        rooms: int,
        area: float,
    ) -> None:
        self.__id = b_id
        self.__date = date
        self.__weeks = weeks
        self.__owner = owner
        self.__number = number
        self.__address = address
        self.__rooms = rooms
        self.__area = area

    def set_id(self, b_id: str) -> None:
        """Update the Booking ID"""
        self.__id = b_id

    def get_id(self) -> str:
        """Get the Booking ID"""
        return self.__id

    def set_date(self, date: str) -> None:
        """Update the Booking Date"""
        self.__date = date

    def get_date(self) -> str:
        """Get the Booking Date"""
        return self.__date

    def set_weeks(self, weeks: int) -> None:
        """Update the Number of Weeks"""
        self.__weeks = weeks

    def get_weeks(self) -> int:
        """Get the Number of Weeks"""
        return self.__weeks

    def set_owner(self, owner: str) -> None:
        """Update the Property Owner"""
        self.__owner = owner

    def get_owner(self) -> str:
        """Get the Property Owner"""
        return self.__owner

    def set_number(self, number: str) -> None:
        """Update the Contact Number"""
        self.__number = number

    def get_number(self) -> str:
        """Get the Contact Number"""
        return self.__number

    def set_address(self, address: str) -> None:
        """Update the Booking Address"""
        self.__address = address

    def get_address(self) -> str:
        """Get the Booking Address"""
        return self.__address

    def set_rooms(self, rooms: int) -> None:
        """Update the Booking Rooms"""
        self.__rooms = rooms

    def get_rooms(self) -> int:
        """Get the Booking Rooms"""
        return self.__rooms

    def get_rooms_cost(self) -> float:
        """Get the Rooms Cost"""
        return self.__rooms * 5

    def set_area(self, area: float) -> None:
        """Update the Garden Area"""
        self.__area = area

    def get_area(self) -> float:
        """Get the Garden Area"""
        return self.__area

    def get_area_cost(self) -> float:
        """Get the Garden Area Cost"""
        return self.__area * 2

    def __str__(self) -> str:
        return (
            f"id: {self.__id}, "
            f"date: {self.__date}, "
            f"weeks: {self.__weeks}, "
            f"owner: {self.__owner}, "
            f"number: {self.__number}, "
            f"address: {self.__address}, "
            f"rooms: {self.__rooms}, "
            f"room cost: {self.get_rooms_cost()}, "
            f"garden area: {self.__area}, "
            f"garden area cost: {self.get_area_cost()}"
        )


class Luxury(Booking):
    def __init__(
        self,
        b_id: str,
        date: str,
        weeks: int,
        owner: str,
        number: str,
        address: str,
        rooms: int,
        area: float,
        alarm: bool,
        pool: bool,
    ) -> None:
        super().__init__(
            b_id,
            date,
            weeks,
            owner,
            number,
            address,
            rooms,
            area,
        )
        self.__alarm = alarm
        self.__pool = pool

    def set_alarm(self, alarm: bool) -> None:
        """Update the Security Alarm Check"""
        self.__alarm = alarm

    def get_alarm(self) -> bool:
        """Get the Security Alarm Check"""
        return self.__alarm

    def set_pool(self, pool: bool) -> None:
        """Update the Pool Maintenance Check"""
        self.__pool = pool

    def get_pool(self) -> bool:
        """Get the Pool Maintenance Check"""
        return self.__pool

    def get_luxury_cost(self) -> float:
        """Get the cost of luxuries"""
        output: float = 0.0
        output += 50.0 if self.__pool else 0.0
        output += 50.0 if self.__alarm else 0.0
        return output

    def __str__(self) -> str:
        return (
            f"{super().__str__()}, "
            f"security alarm check: {self.__alarm}, "
            f"pool maintenance check: {self.__pool}, "
            f"total cost: {self.get_luxury_cost()}"
        )
