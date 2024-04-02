def is_isomorphic(x: str, y: str) -> bool:
    return True if set(x).__len__() == set(y).__len__() else False
