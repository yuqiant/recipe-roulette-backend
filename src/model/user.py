<<<<<<< HEAD
from .inventory import Inventory
from .user_settings import UserSettings
=======
from .ingredient import Ingredient
>>>>>>> 89713ee (add unittest for models)


class User:

    def __init__(self, _id: str, inventory: Inventory = Inventory(), settings: UserSettings = UserSettings()) -> None:
        if not isinstance(inventory, Inventory):
            raise TypeError("inventory must be of type Inventory")
        self._id = _id
        self.inventory = inventory
        self.settings = settings

    @classmethod
    def fromdict(cls, user_dict: dict):
        # process inventory
        inventory = Inventory(user_dict['inventory'])
        settings = UserSettings.fromdict(user_dict['settings'])
        return cls(user_dict['_id'], inventory,
                   settings)

    def todict(self) -> dict:
        return {
            "_id": self._id,
            "inventory": list(self.inventory),
            "settings": self.settings.todict()
        }

    def __str__(self) -> str:
        return {
            "_id": self._id,
            "inventory": self.inventory,
            "settings": self.settings
        }.__str__()

<<<<<<< HEAD
    def __repr__(self) -> str:
        return self.__str__()
=======
    def add_ingredient(self, ingredient: Ingredient):
        # add error handling
        self.inventory.add(ingredient)
        # update db

    def remove_ingredient(self, ingredient: Ingredient):
        # add error handling
        self.inventory.remove(ingredient)
        # update db
>>>>>>> 89713ee (add unittest for models)
