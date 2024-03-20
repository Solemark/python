class Order:
    __tax: float
    __quantity: float
    __price: float
    __tax_cost: float
    __total_bill: float

    def __init__(self, quantity: float, price: float, tax: float) -> None:
        self.__quantity = quantity
        self.__price = price
        self.__tax = tax
        self.__tax_cost = (quantity * price) * self.__tax
        self.__total_bill = (quantity * price) + self.__tax_cost

    def set_quantity(self, v: float) -> None:
        """Set the BookOrder quantity"""
        self.__quantity = v

    def get_quantity(self) -> float:
        """Get the BookOrder quantity"""
        return self.__quantity

    def set_price(self, v: float) -> None:
        """Set the BookOrder price"""
        self.__price = v

    def get_price(self) -> float:
        """Get the BookOrder price"""
        return self.__price

    def set_tax(self, v: float) -> None:
        self.__tax = v

    def get_tax(self) -> float:
        """Get the BookOrder tax"""
        return self.__tax

    def get_result(self) -> float:
        """Get the BookOrder result"""
        return self.__total_bill

    def __str__(self) -> str:
        return str(self.__quantity + self.__price + self.__total_bill)
