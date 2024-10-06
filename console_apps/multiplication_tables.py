def calculate(table: int, max: int) -> list[str]:
    return [f"{str(table)} x {str(i)} = {str(table*i)}" for i in range(max + 1)]
