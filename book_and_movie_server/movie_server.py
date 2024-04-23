from socket import socket
from typing import Any
from os import linesep

from movie import Movie


class MovieServer:
    def __init__(
        self, address: str = "localhost", port: int = 8002, connections: int = 5
    ) -> None:
        self.ADDRESS: str = address
        self.PORT: int = port
        self.CONNECTIONS: int = connections
        self.movies: list[Movie] = self.__get_movies()

        self.SERVER = socket()
        self.SERVER.bind((self.ADDRESS, self.PORT))
        self.SERVER.listen(self.CONNECTIONS)

        print(f"listening on {self.ADDRESS}:{self.PORT}")

        self.__run_server()

    def __run_server(self) -> None:
        """Run the Movie Server"""
        while True:
            sock, addr = self.SERVER.accept()
            print(f"Incoming message from {addr}")
            b: list[str] = sock.recv(1024).decode().split(",")
            self.__save_movies(Movie(b[0], float(b[1]), float(b[2])))
            sock.send(f"Movie successfully saved: {self.movies[-1].__str__()}".encode())
            sock.close()

    def __get_movies(self) -> list[Movie]:
        """Get the list of movies from file"""
        f: Any = open("data/movies.csv").readlines()
        movies: list[Movie] = []
        for d in f:
            b: list[str] = d.split(",")
            movies = [*movies, Movie(b[0], float(b[1]), float(b[2]))]
        return movies

    def __save_movies(self, b: Movie) -> None:
        """Save the Movie list"""
        self.movies.append(b)
        f: Any = open("data/movies.csv", "w")
        for movie in self.movies:
            f.write(movie.__str__() + linesep)


if __name__ == "__main__":
    MovieServer()
