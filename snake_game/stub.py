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


class Position:
    def __init__(self, x: int, y: int) -> None:
        self.x: int = x
        self.y: int = y

    def __str__(self) -> str:
        return f"[{self.x},{self.y}]"
