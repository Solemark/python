def fizz_buzz(fizz: int, buzz: int, max: int) -> list[str]:
    return [__calc(fizz, buzz, number) for number in range(1, max + 1)]


def __calc(fizz: int, buzz: int, number: int) -> str:
    output: str = ""
    output += "fizz" if number % fizz == 0 else ""
    output += "buzz" if number % buzz == 0 else ""
    output += f"{number}" if output == "" else ""
    return output
