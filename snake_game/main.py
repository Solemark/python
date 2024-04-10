from random import randint

from snake import Snake
from stub import Axis, Fields, Position


def play(board: list[list[str]]) -> None:
    """Play the snake game"""
    snake: Snake = Snake()
    snake_head: Position = snake.get_head()
    board[snake_head.y][snake_head.x] = Fields.Snake.value

    food: Position = __place_food(board, snake_head)
    board[food.y][food.x] = Fields.Food.value

    print(food)
    print(snake)
    __display_board(board)
    # TODO - create loop -> 5 food
    # TODO - get keyboard input -> Up, Down, Left, Right
    # TODO - grow snake by 1 when it eats food


def __place_food(board: list[list[str]], snake_head: Position) -> Position:
    """Create a new Position for food"""
    x: int = __boundary_check(randint(0, len(board[0]) - 1), board, Axis.x)
    y: int = __boundary_check(randint(0, len(board) - 1), board, Axis.y)
    if x == snake_head.x and y == snake_head.y:
        return __place_food(board, snake_head)
    return Position(x, y)


def __boundary_check(i: int, board: list[list[str]], axis: Axis) -> int:
    """Check that the Position attribute is within the playable area"""
    if axis == Axis.x:
        if i <= 0:
            return 1
        if i >= len(board[0]) - 1:
            return len(board[0]) - 2
    else:
        if i <= 0:
            return 1
        if i >= len(board) - 1:
            return len(board) - 2
    return i


def __display_board(board: list[list[str]]) -> None:
    """Print the current board state to the console"""
    for row in board:
        print(row)


if __name__ == "__main__":
    play(
        [
            ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],
            ["*", " ", " ", " ", " ", " ", " ", " ", " ", "*"],
            ["*", " ", " ", " ", " ", " ", " ", " ", " ", "*"],
            ["*", " ", " ", " ", " ", " ", " ", " ", " ", "*"],
            ["*", " ", " ", " ", " ", " ", " ", " ", " ", "*"],
            ["*", " ", " ", " ", " ", " ", " ", " ", " ", "*"],
            ["*", " ", " ", " ", " ", " ", " ", " ", " ", "*"],
            ["*", " ", " ", " ", " ", " ", " ", " ", " ", "*"],
            ["*", " ", " ", " ", " ", " ", " ", " ", " ", "*"],
            ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],
        ]
    )
