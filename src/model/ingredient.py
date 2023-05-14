from bson.objectid import ObjectId


class Ingredient:

    def __init__(self,  id: ObjectId, categoryEN: str, nameEN: str, categoryZH: str, nameZH: str) -> None:
        self._id = id
        self.categoryEN = categoryEN
        self.nameEN = nameEN
        self.categoryZH = categoryZH
        self.nameZH = nameZH

    @classmethod
    def fromdict(cls, ingredient_dict: dict):
        return cls(ingredient_dict['_id'], ingredient_dict['categoryEN'], ingredient_dict['nameEN'], ingredient_dict['categoryZH'], ingredient_dict['nameZH'])

    def todict(self) -> dict:
        return self.__dict__

    @classmethod
    def fromdict(cls, ingredient_dict: dict):
        return cls(ingredient_dict['_id'], ingredient_dict['category'], ingredient_dict['ingredientName'], ingredient_dict['categoryCN'], ingredient_dict['ingredientNameCN'])

    def todict(self) -> dict:
        return self.__dict__

    def __str__(self) -> str:
        return self.todict().__str__()

    def __repr__(self) -> str:
        return self.__str__()

    def __hash__(self) -> int:
        return hash(self._id)

    def __eq__(self, __value: object) -> bool:
        if not isinstance(__value, Ingredient):
            raise ValueError("Comparing Ingredient with an invalid type")
        return self._id == __value._id  # ObjectId can be compared with '=='
