def is_iso(x: str, y: str) -> bool:
    return set(x).__len__() == set(y).__len__()
