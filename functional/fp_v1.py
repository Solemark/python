from datetime import datetime


def get_intro() -> str:
    current_time = datetime.now()
    if current_time.hour < 12:
        output = "good morning"
    elif 12 <= current_time.hour < 18:
        output = "good afternoon"
    else:
        output = "good evening"
    return output


def greet(name: str, intro: str) -> str:
    return f"{intro}, {name}."


def greet_list(names: list[str], intro: str) -> list[str]:
    return [greet(name, intro) for name in names]


def main() -> None:
    name = input("Enter your name: ")
    print(greet(get_intro(), name))
    print(greet_list(["Tim", "Jim", "Tom"], get_intro()))


if __name__ == "__main__":
    main()
