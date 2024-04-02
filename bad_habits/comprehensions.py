def never_using_comprehensions() -> None:
    dict_comp: dict[int, int] = {i: i * i for i in range(10)}
    list_comp: list[int] = [x * x for x in range(10)]
    set_comp: set[int] = {i % 3 for i in range(10)}
    gen_comp = (2 * x + 5 for x in range(10))
    print(dict_comp, list_comp, set_comp, gen_comp)


def always_using_comprehensions(a: list[int], b: list[int], n: int) -> list[int]:
    return [
        # What in the nine hells is this!?
        sum(a[n * i + k] * b[n * k + j] for k in range(n))
        for i in range(n)
        for j in range(n)
    ]
