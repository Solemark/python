from typing import Callable


def greet(func: Callable) -> str:
    return func("Hello world")


def calculate(function: Callable, x: int | float, y: int | float) -> int | float:
    return function(x, y)


print(greet(lambda s: f"{s.upper()}"))
print(greet(lambda s: f"{s.lower()}"))
print(calculate(lambda a, b: a + b, 1, 1))
print(calculate(lambda a, b: a - b, 1, 1))
