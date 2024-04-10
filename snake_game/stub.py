from dataclasses import dataclass
from enum import Enum, auto


class Axis(Enum):
    x = auto()
    y = auto()


class Direction(Enum):
    Up = auto()
    Left = auto()
    Right = auto()
    Down = auto()


class Fields(Enum):
    Wall = "*"
    Space = " "
    Snake = "#"
    Food = "@"


@dataclass(init=True)
class Position:
    x: int
    y: int
