from bson.objectid import ObjectId


class Ingredient:

    def __init__(self,  id: ObjectId, category: str, ingredientName: str, categoryCN: str, ingredientNameCN: str) -> None:
        self._id = id
        self.category = category
        self.ingredientName = ingredientName
        self.categoryCN = categoryCN
        self.ingredientNameCN = ingredientNameCN

    @classmethod
    def fromdict(cls, ingredient_dict: dict):
        return cls(ingredient_dict['_id'], ingredient_dict['category'], ingredient_dict['ingredientName'], ingredient_dict['categoryCN'], ingredient_dict['ingredientNameCN'])

    def todict(self) -> dict:
        return self.__dict__

    def __str__(self) -> str:
        return self.todict().__str__()

    def __hash__(self) -> int:
        return hash(self._id)

    def __eq__(self, __value: object) -> bool:
        if not isinstance(__value, Ingredient):
            raise ValueError("Comparing Ingredient with an invalid type")
        return self._id == __value._id  # ObjectId can be compared with '=='


# if __name__ == "__main__":
#     id = ObjectId("645eabb31408d7bd1e4c4921")
#     ingredient = Ingredient(id,
#                             "蔬菜", "西瓜", "蔬菜", "西瓜")
#     print(ingredient)
#     print(ingredient.todict())
