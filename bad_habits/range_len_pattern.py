def range_len_pattern():
    a: list[int] = [1, 2, 3]
    for i in range(len(a)):
        print(a[i])


def proper_range_len_pattern():
    a: list[int] = [1, 2, 3]
    for i in a:
        print(i)


def proper_range_len_pattern_b():
    a: list[int] = [1, 2, 3]
    for i in enumerate(a):  # enumerate gets the index
        print(i)
