from typing import Callable, TypeAlias

Greet: TypeAlias = Callable[[str], str]
Calc: TypeAlias = Callable[[int | float, int | float], int | float]


def shout(text: str) -> str:
    return f"{text.upper()}!"


def whisper(text: str) -> str:
    return text.lower()


def greet(func: Greet) -> str:
    return func("Hello World")


def add(x: int | float, y: int | float) -> int | float:
    return x + y


def subtract(x: int | float, y: int | float) -> int | float:
    return x - y


def calculate(function: Calc, x: int | float, y: int | float) -> int | float:
    return function(x, y)


print(greet(shout))
print(greet(whisper))

print(calculate(add, 1, 1))
print(calculate(subtract, 1, 1))
