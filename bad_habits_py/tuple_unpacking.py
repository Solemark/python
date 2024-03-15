def not_tuple_unpacking() -> None:
    mytuple: tuple[int, int] = (1, 2)
    a: int = mytuple[0]
    b: int = mytuple[1]
    print(a, b)


def proper_tuple_unpacking() -> None:
    a: int = 0
    b: int = 0
    mytuple: tuple[int, int] = (1, 2)
    a, b = mytuple
    print(a, b)


proper_tuple_unpacking()
