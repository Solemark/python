from order import Order


class BookOrder(Order):
    __tax: float = 0.1

    def __init__(self, quantity: float, price: float) -> None:
        super().__init__(quantity, price, self.__tax)
