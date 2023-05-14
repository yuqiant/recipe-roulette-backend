from .ingredient import Ingredient


class User:

    def __init__(self, userId: str, inventory: set = set(), settings: dict = {}) -> None:
        self.userId = userId
        # perhaps consider creating an inventory class?
        self.inventory = inventory
        self.settings = settings

    @classmethod
    def fromdict(cls, user_dict: dict):
        # process inventory
        inventory = set()
        for ingredient in user_dict['inventory']:
            inventory.add(Ingredient.fromdict(ingredient))
        return cls(user_dict['userId'], inventory,
                   user_dict['settings'])

    def todict(self) -> dict:
        return self.__dict__

    def __str__(self) -> str:
        return {
            "userId": self.userId,
            "inventory": [ingredient.todict() for ingredient in self.inventory],
            "settings": self.settings
        }.__str__()

    def add_ingredient(self, ingredient: Ingredient):
        # add error handling
        self.inventory.add(ingredient)
        # update db

    def remove_ingredient(self, ingredient: Ingredient):
        # add error handling
        self.inventory.remove(ingredient)
        # update db
