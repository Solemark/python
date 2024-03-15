def addition(n: int | float):
    return n + n


numbers = (1, 2, 3, 4)
for item in map(addition, numbers):
    print(item, end=", ")
