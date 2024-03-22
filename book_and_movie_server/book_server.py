from flask import Flask, request
from markupsafe import escape
from typing import Any

from book import Book

app = Flask(__name__)


@app.get("/books")
def get_books() -> list[dict[str, str | float]]:
    """Get the entire book list from the server"""
    books: list[Book] = __get_book_list()
    return [b.serialize() for b in books]


@app.get("/books/<book>")
def get_book(book: str) -> dict[str, str | float]:
    """Get a specific book from the server"""
    books: list[Book] = __get_book_list()
    return [b.serialize() for b in books if b.get_name() == escape(book)][0]


@app.post("/books/save")
def save_book() -> Any:
    """Save a new book to the DB"""
    res: Any = request.json
    books: list[Book] = [*__get_book_list(), res]
    __save_book_list(books)


def __get_book_list() -> list[Book]:
    """Get the list of books from file"""
    b = open("data/books.csv").readlines()
    books: list[Book] = []
    for i in b:
        j: list[str] = i.split(",")
        books = [*books, Book(j[0], float(j[1]), float(j[2]))]
    return books


def __save_book_list(books: list[Book]) -> None:
    """Save the Book list"""
    f: Any = open("data/books.csv", "w")
    for book in books:
        f.write(book.__str__())
