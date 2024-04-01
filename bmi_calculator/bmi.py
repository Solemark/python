class BMI:
    __id: str
    """id of the user record"""
    __height: float
    """height in mm and needs to be converted to m"""
    __weight: float
    """weight in kg"""

    def __init__(self, id: str, height: float, weight: float) -> None:
        self.__id = id
        self.__height = height
        self.__weight = weight

    def set_id(self, id: str) -> None:
        """set the id of the user"""
        self.__id = id

    def get_id(self) -> str:
        """get the id of the user"""
        return self.__id

    def set_height(self, height: float) -> None:
        """set the height of the user"""
        self.__height = height

    def get_height(self) -> float:
        """get the height of the user"""
        return self.__height

    def set_weight(self, weight: float) -> None:
        """set the weight of the user"""
        self.__weight = weight

    def get_weight(self) -> float:
        """get the weight of the user"""
        return self.__weight

    def get_rating(self) -> str:
        """get the bmi rating of the user"""
        bmi: float = self.__weight / ((self.__height / 100) ** 2)
        rating: str = ""
        if bmi < 16.00:
            rating = "Bulimic"
        if bmi < 16.99:
            rating = "Lean"
        if bmi < 18.49:
            rating = "Under"
        if bmi < 24.99:
            rating = "Normal"
        if bmi < 29.99:
            rating = "Over"
        if bmi < 34.99:
            rating = "Obese"
        if bmi >= 35:
            rating = "Morbid"
        return rating
