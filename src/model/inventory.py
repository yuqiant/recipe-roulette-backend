from .ingredient import Ingredient
from bson.objectid import ObjectId
from typing import Iterable


class Inventory(set):
    '''
        Inventory of users that stores ingredients.
        To reduce database size, the actual contents stored are the ingredient ObjectIds, which can be used to fetch the actual ingredients.
    '''

    def __init__(self, __iterable: Iterable[ObjectId] = []):
        super().__init__(__iterable)

    @classmethod
    def fromarray(cls, inventory_dict):
        '''
            Create a new Inventory from a dict.
            The dict should not contain the actual ingredients,
            instead it shoud contain the ingredient ObjectIds.
        '''
        return cls(ObjectId(ingredient_id)
                   for ingredient_id in inventory_dict.get('ingredients', []))

    def add(self, ingredient: ObjectId | Ingredient) -> None:
        if isinstance(ingredient, Ingredient):
            super().add(ingredient._id)
        else:
            super().add(ingredient)

    def remove(self, ingredient: ObjectId | Ingredient) -> None:
        if isinstance(ingredient, Ingredient):
            super().remove(ingredient._id)
        else:
            super().remove(ingredient)

    def get_all(self) -> set[ObjectId]:
        return [ingredient for ingredient in self]

    def __contains__(self, __o: object) -> bool:
        if isinstance(__o, Ingredient):
            return super().__contains__(__o._id)
        elif isinstance(__o, ObjectId):
            return super().__contains__(__o)
        else:
            return False

    def __str__(self) -> str:
        return super().__str__()

    def __repr__(self) -> str:
        return super().__repr__()
