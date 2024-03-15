def manually_close_file(filename: str) -> None:
    f = open(filename, "w")
    f.write("hello!\n")
    f.close()


def proper_close_file(filename: str) -> None:
    with open(filename, "w") as f:
        f.write("hello!\n")


proper_close_file("hello_world")
