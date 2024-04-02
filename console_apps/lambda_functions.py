from typing import Callable, TypeAlias

Greet: TypeAlias = Callable[[str], str]
Calc: TypeAlias = Callable[[int | float, int | float], int | float]


def greet(func: Greet) -> str:
    return func("Hello world")


def calculate(func: Calc, x: int | float, y: int | float) -> int | float:
    return func(x, y)


print(greet(lambda s: f"{s.upper()}!"))
print(greet(lambda s: f"{s.lower()}"))

print(calculate(lambda a, b: a + b, 1, 1))
print(calculate(lambda a, b: a - b, 1, 1))
