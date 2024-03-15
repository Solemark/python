def index_counter_variable() -> None:
    data: list[int] = [1, 2, 3]

    i: int = 0
    for x in data:
        print(i, x)
        i += 1


def proper_index_counter_variable() -> None:
    data: list[int] = [1, 2, 3]

    for i, x in enumerate(data):
        print(i, x)
