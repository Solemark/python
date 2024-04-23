from socket import socket
from typing import Any
from os import linesep

from book import Book


class BookServer:
    def __init__(
        self, address: str = "localhost", port: int = 8001, connections: int = 5
    ) -> None:
        self.ADDRESS: str = address
        self.PORT: int = port
        self.CONNECTIONS: int = connections
        self.books: list[Book] = self.__get_books()

        self.SERVER = socket()
        self.SERVER.bind((self.ADDRESS, self.PORT))
        self.SERVER.listen(self.CONNECTIONS)

        print(f"listening on {self.ADDRESS}:{self.PORT}")

        self.__run_server()

    def __run_server(self) -> None:
        """Run the Book Server"""
        while True:
            sock, addr = self.SERVER.accept()
            print(f"Incoming message from {addr}")

            b: list[str] = sock.recv(1024).decode().split(",")
            self.__save_books(Book(b[0], float(b[1]), float(b[2])))

            sock.send(f"Book successfully saved: {self.books[-1].__str__()}".encode())
            sock.close()

    def __get_books(self) -> list[Book]:
        """Get the list of books from file"""
        f: Any = open("data/books.csv").readlines()
        books: list[Book] = []
        for d in f:
            b: list[str] = d.split(",")
            books.append(Book(b[0], float(b[1]), float(b[2])))
        return books

    def __save_books(self, b: Book) -> None:
        """Save the Book list"""
        self.books.append(b)
        f: Any = open("data/books.csv", "w")
        for book in self.books:
            f.write(book.__str__() + linesep)


if __name__ == "__main__":
    BookServer()
