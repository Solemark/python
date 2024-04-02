def checking_type_equality() -> None:
    p: tuple[int, int] = (1, 2)

    if type(p) == tuple:  # liskov substitution principle
        print("IS tuple")
    else:
        print("ISNT tuple")


def proper_checking_type_equality() -> None:
    p: tuple[int, int] = (1, 2)

    if isinstance(p, tuple):
        print("IS tuple")
    else:
        print("ISNT tuple")
