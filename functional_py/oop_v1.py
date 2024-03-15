from datetime import datetime


class Greeting:
    __intro: str = ""

    def __init__(self, greeting_intro: str) -> None:
        self.__intro = greeting_intro

    def greet(self, name: str) -> str:
        return f"{self.__intro}, {name}."

    def greet_list(self, names: list[str]) -> list[str]:
        greetings: list[str] = []
        for name in names:
            greetings.append(self.greet(name))
        return greetings


def main() -> None:
    current_time = datetime.now()
    if current_time.hour < 12:
        greeting_intro = "good morning"
    elif 12 <= current_time.hour < 18:
        greeting_intro = "good afternoon"
    else:
        greeting_intro = "good evening"

    name = input("Enter your name: ")
    greeting = Greeting(greeting_intro)
    greeting.greet(name)


if __name__ == "__main__":
    main()
