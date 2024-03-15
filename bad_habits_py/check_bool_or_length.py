def checking_bool_or_len(x: bool, y: list[str]) -> None:
    if bool(x):
        pass

    if len(y) != 0:
        pass


def proper_checking_bool_or_len(x: bool | list[str]) -> None:
    if x:
        pass
