from flask import Flask, request
from markupsafe import escape
from typing import Any

from movie import Movie

app = Flask(__name__)


@app.get("/movies")
def get_movies() -> list[dict[str, str | float]]:
    """Get the entire movie list from the server"""
    movies: list[Movie] = __get_movie_list()
    return [m.serialize() for m in movies]


@app.get("/movies/<movie>")
def get_movie(movie: str) -> dict[str, str | float]:
    """Get a specific movie from the server"""
    movies: list[Movie] = __get_movie_list()
    return [m.serialize() for m in movies if m.get_name() == escape(movie)][0]


@app.post("/movies/save")
def save_movie() -> Any:
    """Save a new movie to the DB"""
    res: Any = request.json
    movies: list[Movie] = [*__get_movie_list(), res]
    __save_movie_list(movies)


def __get_movie_list() -> list[Movie]:
    """Get the list of movies from file"""
    m = open("data/movies.csv").readlines()
    movies: list[Movie] = []
    for i in m:
        j: list[str] = i.split(",")
        movies = [*movies, Movie(j[0], float(j[1]), float(j[2]))]
    return movies


def __save_movie_list(movies: list[Movie]) -> None:
    """Save the Movie list"""
    f: Any = open("data/movies.csv", "w")
    for movie in movies:
        f.write(movie.__str__())
