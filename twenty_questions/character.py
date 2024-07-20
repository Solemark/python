class Traits:
    def __init__(
        self,
        eyes: str,
        gender: str,
        hair: str,
        height: str,
        pants: str,
        shirt: str,
        skin: str,
        weight: str,
    ) -> None:
        self.eyes: str = eyes
        self.gender: str = gender
        self.hair: str = hair
        self.height: str = height
        self.pants: str = pants
        self.shirt: str = shirt
        self.skin: str = skin
        self.weight: str = weight


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
        """Get character name"""
        return self.__name

    def get_weighting(self) -> int:
        """Get character weighting"""
        return self.__weighting

    def search_trait(self, trait: str, value: str) -> None:
        """See if character has attribute and update weighting"""
        if self.__getattribute__(trait) == value:
            self.__weighting = self.__weighting + 1
