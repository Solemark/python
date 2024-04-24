from socket import socket
from item import Item


class Client:
    def __init__(self) -> None:
        while True:
            print("\n".join(self.client_prompt()))
            res: str = input("Enter your option: ")

            match res:
                case "1":
                    self.send_book()
                case "2":
                    self.send_movie()
                case _:
                    exit(0)

    def send_book(self) -> None:
        s: socket = socket()
        s.connect(("localhost", 8001))
        item: Item = self.get_details("book")
        s.send(item.__str__().encode())
        m = s.recv(1024).decode()
        print(m)
        s.close()

    def send_movie(self) -> None:
        s: socket = socket()
        s.connect(("localhost", 8002))
        item: Item = self.get_details("movie")
        s.send(item.__str__().encode())
        m = s.recv(1024).decode()
        print(m)
        s.close()

    def get_details(self, t: str) -> Item:
        print(f"Enter {t} details:")
        return Item(
            input(f"Enter {t} name: "),
            float(input(f"Enter {t} quantity: ")),
            float(input(f"Enter {t} price: ")),
        )

    def client_prompt(self) -> list[str]:
        return [
            "**************************************",
            "Place your order by selecting a number",
            "**************************************",
            "1. Purchase Book",
            "2. Purchase Movie",
            "3. Exit",
            "**************************************",
        ]


if __name__ == "__main__":
    Client()
