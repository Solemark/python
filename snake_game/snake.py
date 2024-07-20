from stub import Direction, Position


class Snake:
    def __init__(self) -> None:
        self.__head: Position = Position(3, 4)
        self.__last: Position = Position(self.__head.x - 1, self.__head.y)
        self.__len: int = 1
        self.__dir: Direction = Direction.Right
        self.__body: list[Position] = [self.__head]

    def set_head(self, pos: Position) -> None:
        """set the position of the head of the snake"""
        self.__head = pos

    def get_head(self) -> Position:
        """Get the position of the head of the snake"""
        return self.__head

    def set_last(self, pos: Position) -> None:
        """Set the last position of the head"""
        self.__last = pos

    def get_last(self) -> Position:
        """Get the last position of the head"""
        return self.__last

    def set_length(self, length: int) -> None:
        """Set the length of the snake"""
        self.__len = length

    def get_length(self) -> int:
        """Get the length of the snake"""
        return self.__len

    def set_direction(self, d: Direction) -> None:
        """Set the direction the snake is moving in"""
        self.__dir = d

    def get_direction(self) -> Direction:
        """Get the direction the snake is moving in"""
        return self.__dir

    def __body_to_str(self) -> str:
        """get self.__body: list[Position] as a str"""
        output: str = ""
        for item in self.__body:
            output += f"{item}"
        return output

    def __str__(self):
        return f"{self.__head}, {self.__last}, {self.__len}, {self.__dir}, {self.__body_to_str()}"
