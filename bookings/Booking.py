class Booking:
    def __init__(
        self,
        booking_id: str = "",
        booking_date: str = "",
        num_weeks: int = 0,
        property_owner_name: str = "",
        contact_number: str = "",
        address: str = "",
        rooms: int = 0,
        garden_area: float = 0.0,
    ) -> None:
        self.__booking_id = booking_id
        self.__booking_date = booking_date
        self.__num_weeks = num_weeks
        self.__property_owner_name = property_owner_name
        self.__contact_number = contact_number
        self.__address = address
        self.__rooms = rooms
        self.__garden_area = garden_area

    def set_booking_id(self, booking_id: str) -> None:
        self.__booking_id = booking_id

    def get_booking_id(self) -> str:
        return self.__booking_id

    def set_booking_date(self, booking_date: str) -> None:
        self.__booking_date = booking_date

    def get_booking_date(self) -> str:
        return self.__booking_date

    def set_num_weeks(self, num_weeks: int) -> None:
        self.__num_weeks = num_weeks

    def get_num_weeks(self) -> int:
        return self.__num_weeks

    def set_property_owner_name(self, property_owner_name: str) -> None:
        self.__property_owner_name = property_owner_name

    def get_property_owner_name(self) -> str:
        return self.__property_owner_name

    def set_contact_number(self, contact_number: str) -> None:
        self.__contact_number = contact_number

    def get_contact_number(self) -> str:
        return self.__contact_number

    def set_address(self, address: str) -> None:
        self.__address = address

    def get_address(self) -> str:
        return self.__address

    def set_rooms(self, rooms: int) -> None:
        self.__rooms = rooms

    def get_rooms(self) -> int:
        return self.__rooms

    def get_rooms_cost(self) -> float:
        return self.__rooms * 5

    def set_garden_area(self, garden_area: float) -> None:
        self.__garden_area = garden_area

    def get_garden_area(self) -> float:
        return self.__garden_area

    def get_garden_area_cost(self) -> float:
        return self.__garden_area * 2

    def __str__(self) -> str:
        return (
            f"id: {self.__booking_id}, "
            f"date: {self.__booking_date}, "
            f"weeks: {self.__num_weeks}, "
            f"owner: {self.__property_owner_name}, "
            f"number: {self.__contact_number}, "
            f"address: {self.__address}, "
            f"rooms: {self.__rooms}, "
            f"room cost: {self.get_rooms_cost()}, "
            f"garden area: {self.__garden_area}, "
            f"garden area cost: {self.get_garden_area_cost()}"
        )


class Luxury(Booking):
    def __init__(
        self,
        booking_id="",
        booking_date="",
        num_weeks=0,
        property_owner_name="",
        contact_number="",
        address="",
        rooms=0,
        garden_area=0.0,
        security_alarm_check=False,
        pool_maintenance=False,
    ) -> None:
        super().__init__(
            booking_id,
            booking_date,
            num_weeks,
            property_owner_name,
            contact_number,
            address,
            rooms,
            garden_area,
        )
        self.__security_alarm_check = security_alarm_check
        self.__pool_maintenance = pool_maintenance

    def set_security_alarm_check(self, security_alarm_check: bool) -> None:
        self.__security_alarm_check = security_alarm_check

    def get_security_alarm_check(self) -> bool:
        return self.__security_alarm_check

    def set_pool_maintenance(self, pool_maintenance: bool) -> None:
        self.__pool_maintenance = pool_maintenance

    def get_pool_maintenance(self) -> bool:
        return self.__pool_maintenance

    def get_luxury_cost(self) -> float:
        output: float = 0.0

        if self.__pool_maintenance is True:
            output += 50.0

        if self.__security_alarm_check is True:
            output += 50

        return output

    def __str__(self) -> str:
        return (
            f"{super().__str__()}, "
            f"security alarm check: {self.__security_alarm_check}, "
            f"pool maintenance check: {self.__pool_maintenance}, "
            f"total cost: {self.get_luxury_cost()}"
        )
