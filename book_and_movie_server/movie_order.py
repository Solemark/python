from order import Order


class MovieOrder(Order):
    __tax: float = 0.3

    def __init__(self, quantity: float, price: float) -> None:
        super().__init__(quantity, price, self.__tax)
