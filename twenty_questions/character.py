from dataclasses import dataclass


@dataclass(init=True)
class Traits:
    eyes: str
    gender: str
    hair: str
    height: str
    pants: str
    shirt: str
    skin: str
    weight: str


class Character(Traits):
    def __init__(
        self,
        name: str,
        eyes: str,
        gender: str,
        hair: str,
        height: str,
        pants: str,
        shirt: str,
        skin: str,
        weight: str,
    ) -> None:
        super().__init__(eyes, gender, hair, height, pants, shirt, skin, weight)
        self.__name: str = name
        self.__weighting: int = 0

    def get_name(self) -> str:
        return self.__name

    def get_weighting(self) -> int:
        return self.__weighting

    def search_trait(self, trait: str, value: str) -> None:
        if self.__getattribute__(trait) == value:
            self.__weighting = self.__weighting + 1
