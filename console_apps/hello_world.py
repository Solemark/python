def greet(self, g: str = "Hello World!", x: int = 1, f: str = "Goodbye World!") -> str:
    return f"{g}\nx is 1\n{f}" if x == 1 else f"{g}\n{f}"
