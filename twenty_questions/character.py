from dataclasses import dataclass


@dataclass(init=True)
class Traits:
    hair: str
    eyes: str
    skin: str
    height: str
    weight: str
    shirt: str
    pants: str


class Character(Traits):
    def __init__(
        self,
        name: str,
        hair: str,
        eyes: str,
        skin: str,
        height: str,
        weight: str,
        shirt: str,
        pants: str,
    ) -> None:
        super().__init__(hair, eyes, skin, height, weight, shirt, pants)
        self.__name: str = name
        self.__weighting: int = 0

    def get_name(self) -> str:
        return self.__name

    def get_weighting(self) -> int:
        return self.__weighting

    def search_trait(self, trait: str, value: str) -> None:
        if self.__getattribute__(trait) == value:
            self.__weighting = self.__weighting + 1
