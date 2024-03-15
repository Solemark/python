def bare_except() -> int | str:
    while True:
        try:
            s: str = input("Input a number: ")
            x: int = int(s)
            return x
        except:  # cant use CTRL+C to escape this one!
            print("Not a number, try again!")


def proper_except() -> int | str:
    while True:
        try:
            s: str = input("Input a number: ")
            x: int = int(s)
            return x
        # use Exception or the exception type, (ValueError in this case)
        except Exception:
            print("Not a number, try again!")
