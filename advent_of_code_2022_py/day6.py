class Day6:
    def run(self, data: str) -> int:
        output: int = 0
        for i in range(data.__len__()):
            a: str = data[i]
            b: str = data[i + 1]
            c: str = data[i + 2]
            d: str = data[i + 3]
            if a != b and a != c and a != d:
                if b != c and b != d:
                    if c != d:
                        output = i + 4
                        break
        return output
