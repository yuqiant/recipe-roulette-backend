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

    def add_ingredient(self, ingredient: ObjectId | Ingredient) -> None:
        if isinstance(ingredient, Ingredient):
            self.add(ingredient._id)
        else:
            self.add(ingredient)

    def remove_ingredient(self, ingredient: ObjectId | Ingredient) -> None:
        if isinstance(ingredient, Ingredient):
            self.remove(ingredient._id)
        else:
            self.remove(ingredient)

    def has_ingredient(self, ingredient: ObjectId | Ingredient) -> bool:
        if isinstance(ingredient, Ingredient):
            return ingredient._id in self
        else:
            return ingredient in self

    def get_all(self) -> set[ObjectId]:
        return [ingredient for ingredient in self]

    def __str__(self) -> str:
        return '\n'.join(map(str, self))

    def __repr__(self) -> str:
        return self.__str__()


# if __name__ == '__main__':
    # inv = Inventory()
    # inv.add_ingredient(ObjectId('645eabb31408d7bd1e4c4921'))
    # inv.add_ingredient(ObjectId('645eabb31408d7bd1e4c4922'))
    # inv.add_ingredient(ObjectId('645eabb31408d7bd1e4c4923'))
    # inv.remove_ingredient(Ingredient(
    #     ObjectId('645eabb31408d7bd1e4c4923'), "cat", "name", "catCN", "nameCN"))
    # print(inv.get_all())
