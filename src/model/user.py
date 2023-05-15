from .ingredient import Ingredient
from .inventory import Inventory


class User:

    def __init__(self, userId: str, inventory: Inventory = Inventory(), settings: dict = {}) -> None:
        if not isinstance(inventory, Inventory):
            raise TypeError("inventory must be of type Inventory")
        self.userId = userId
        self.inventory = inventory
        self.settings = settings

    @classmethod
    def fromdict(cls, user_dict: dict):
        # process inventory
        inventory = Inventory(user_dict['inventory'])
        return cls(user_dict['userId'], inventory,
                   user_dict['settings'])

    def todict(self) -> dict:
        return self.__dict__

    def __str__(self) -> str:
        return {
            "userId": self.userId,
            "inventory": self.inventory,
            "settings": self.settings
        }.__str__()

    # def add_ingredient(self, ingredient: Ingredient):
    #     # add error handling
    #     self.inventory.add(ingredient)
    #     # update db

    # def remove_ingredient(self, ingredient: Ingredient):
    #     # add error handling
    #     self.inventory.remove(ingredient)
    #     # update db
