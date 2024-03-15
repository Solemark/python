def manual_string_formatting(hello: str, world: str) -> str:
    return hello + ", " + world + "!"


def proper_string_formatting(hello: str, world: str) -> str:
    return f"{hello}, {world}!"


print(manual_string_formatting("hello", "world"))
print(proper_string_formatting("hello", "world"))
