class Item:
    __name: str
    __tax: float
    __quantity: float
    __price: float
    __tax_cost: float
    __total_bill: float

    def __init__(self, name: str, quantity: float, price: float, tax: float) -> None:
        self.__name = name
        self.__quantity = quantity
        self.__price = price
        self.__tax = tax
        self.__tax_cost = (quantity * price) * self.__tax
        self.__total_bill = (quantity * price) + self.__tax_cost

    def set_name(self, v: str) -> None:
        """Set the item name"""
        self.__name = v

    def get_name(self) -> str:
        """Get the item name"""
        return self.__name

    def set_quantity(self, v: float) -> None:
        """Set the item quantity"""
        self.__quantity = v

    def get_quantity(self) -> float:
        """Get the item quantity"""
        return self.__quantity

    def set_price(self, v: float) -> None:
        """Set the item price"""
        self.__price = v

    def get_price(self) -> float:
        """Get the item price"""
        return self.__price

    def set_tax(self, v: float) -> None:
        """Set the item tax"""
        self.__tax = v

    def get_tax(self) -> float:
        """Get the item tax"""
        return self.__tax

    def get_result(self) -> float:
        """Get the item result"""
        return self.__total_bill

    def serialize(self) -> dict[str, str | float]:
        """Serialize the item to be sent across the network"""
        return {
            "name": self.__name,
            "quantity": self.__quantity,
            "price": self.__price,
        }

    def __str__(self) -> str:
        return f"{self.__name},{self.__quantity},{self.__price}"
