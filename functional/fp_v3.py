from datetime import datetime
from typing import Callable
from functools import partial

Introducer = Callable[[], str]
IntroFunc = Callable[[str], str]


def get_intro() -> str:
    current_time = datetime.now()
    if current_time.hour < 12:
        output = "good morning"
    elif 12 <= current_time.hour < 18:
        output = "good afternoon"
    else:
        output = "good evening"
    return output


def greet(name: str, intro: Introducer) -> str:
    return f"{intro()}, {name}."


def greet_list(names: list[str], intro: IntroFunc) -> list[str]:
    return [intro(name) for name in names]


def get_name() -> str:
    return input("Enter your name: ")


def main() -> None:
    greet_fn = partial(greet, intro=get_intro)
    print(greet_fn(get_name()))
    print(greet_list(["Tim", "Jim", "Tom"], greet_fn))


if __name__ == "__main__":
    main()
