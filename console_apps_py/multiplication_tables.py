def calculate(table: int, max: int) -> list[str]:
    return [__format_data(table, x) for x in range(max + 1)]


def __format_data(table: int, number: int) -> str:
    return f"{str(table)} x {str(number)} = {str(table * number)}"
