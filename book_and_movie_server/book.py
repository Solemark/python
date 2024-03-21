from item import Item


class Book(Item):
    __tax: float = 0.1

    def __init__(self, name: str, quantity: float, price: float) -> None:
        super().__init__(name, quantity, price, self.__tax)
