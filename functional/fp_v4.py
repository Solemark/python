O_LIST = "Origin List"
S_LIST = "Sorted List"


def display(text: str, list: list[int]) -> str:
    return f"{text}: {list}"


def main() -> None:
    test_list: list[int] = [120, 68, -20, 0, 5, 67, 14, 99]

    # immutable sort
    sorted_list = sorted(test_list)
    print(display(O_LIST, test_list))
    print(display(S_LIST, sorted_list))

    # mutable sort
    test_list.sort()
    print(display(O_LIST, test_list))


main()
