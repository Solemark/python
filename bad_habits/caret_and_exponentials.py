def caret_and_exponentials(a: int, b: int) -> int:
    x = a ^ b  # bitwise xor
    y = a**b  # exponential
    return x | y
