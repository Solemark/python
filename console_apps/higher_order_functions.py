from typing import Callable


def shout(text: str) -> str:
    return f"{text.upper()}!"


def whisper(text: str) -> str:
    return text.lower()


def greet(func: Callable) -> str:
    return func("Hello world")


def add(x: int | float, y: int | float) -> int | float:
    return x + y


def subtract(x: int | float, y: int | float) -> int | float:
    return x - y


def calculate(function: Callable, x: int | float, y: int | float) -> int | float:
    return function(x, y)


print(greet(shout))
print(greet(whisper))
print(calculate(add, 1, 1))
print(calculate(subtract, 1, 1))
