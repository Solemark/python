from traits import Traits


class Character:
    def __init__(self, name: str, traits: Traits) -> None:
        self.__name: str = name
        self.__traits: Traits = traits
        self.__weighting: int = 0

    def search_trait(self, trait: str, value: str) -> None:
        if self.__traits.__getattribute__(trait) == value:
            self.__weighting += 1

    def check_weighting(self) -> int:
        return self.__weighting
