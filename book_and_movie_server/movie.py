from item import Item


class Movie(Item):
    __tax: float = 0.3

    def __init__(self, name: str, quantity: float, price: float) -> None:
        super().__init__(name, quantity, price, self.__tax)
