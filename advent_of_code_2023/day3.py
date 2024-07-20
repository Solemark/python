from math import isclose


class Number:
    def __init__(self, number: int, start: int, end: int, row: int) -> None:
        self.number: int = number
        self.start: int = start
        self.end: int = end
        self.row: int = row


class Symbol:
    def __init__(self, pos: int, row: int) -> None:
        self.pos: int = pos
        self.row: int = row


class Day3:
    def run(self, input: list[str]) -> int:
        output: int = 0
        numbers: list[Number] = []
        symbols: list[Symbol] = []
        start: int = 0
        for line, row in enumerate(input):
            item: str = ""
            starting: bool = True
            for pos, char in enumerate(row):
                if char in ["*", "#", "+", "$"]:
                    symbols.append(Symbol(pos, line))
                if char.isdigit():
                    item += char
                    if starting:
                        start = pos
                        starting = False
                if char == "." and item != "":
                    numbers.append(Number(int(item), start, pos, line))
                    item = ""
                    starting = True
                if pos == len(row) - 1 and item != "":
                    numbers.append(Number(int(item), start, pos, line))

        for number in numbers:
            success: bool = False
            for symbol in symbols:
                if success:
                    break
                if isclose(number.row, symbol.row, abs_tol=1):
                    for pos in range(number.start, (number.end + 1)):
                        if success:
                            break
                        if isclose(pos, symbol.pos, abs_tol=1):
                            output += number.number
                            success = True

        return output
