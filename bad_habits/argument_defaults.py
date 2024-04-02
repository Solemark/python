def bad_append(data: int, arr: list = []) -> list[object]:
    arr.append(data)
    return arr


def proper_append(data: int, arr: list | None = None) -> list[object]:
    if arr is None:
        arr = []
    # arr.append(data)
    return [*arr, data]


arr1: list[object] = bad_append(0)
arr2: list[object] = bad_append(1)
print("improper:", arr1, arr2)
arr1 = proper_append(0)
arr2 = proper_append(1)
print("proper:", arr1, arr2)
