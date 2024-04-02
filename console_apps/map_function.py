def do_map(numbers: list[int | float]) -> list[int | float]:
    return list(map(lambda a: a + a, numbers))


numbers: list[int | float] = [1, 2, 3, 4]
print(do_map(numbers))
