from typing import Any


def swap(a: Any, b: Any) -> tuple[Any, Any]:
    a, b = b, a
    return a, b
