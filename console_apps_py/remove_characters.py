def remove(input: str, chars: list[str]) -> str:
    return "".join(c for c in input if c not in chars)
