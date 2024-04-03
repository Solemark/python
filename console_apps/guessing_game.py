from random import randint


def __check(g: int, n: int) -> tuple[str, bool]:
    if g == n:
        return "You win!", True
    elif g > n:
        return "Lower! ", False
    else:
        return "Higher! ", False


def main() -> None:
    MAX: int = int(input("Lets play a guessing game!\nWhat should our max number be? "))
    NUMBER: int = randint(1, MAX)
    res: str = f"I'm thinking of a number between 1 and {MAX}. Can you guess it? "
    while True:
        GUESS: int = int(input(res))
        res, STATE = __check(GUESS, NUMBER)
        if STATE:
            print(res)
            break


if __name__ == "__main__":
    main()
