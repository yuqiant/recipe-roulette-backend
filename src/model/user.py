from .ingredient import Ingredient
from .inventory import Inventory


class User:

    def __init__(self, _id: str, inventory: Inventory = Inventory(), settings: dict = {}) -> None:
        if not isinstance(inventory, Inventory):
            raise TypeError("inventory must be of type Inventory")
        self._id = _id
        self.inventory = inventory
        self.settings = settings

    @classmethod
    def fromdict(cls, user_dict: dict):
        # process inventory
        inventory = Inventory(user_dict['inventory'])
        return cls(user_dict['_id'], inventory,
                   user_dict['settings'])

    def todict(self) -> dict:
        return {
            "_id": self._id,
            "inventory": list(self.inventory),
            "settings": self.settings
        }

    def __str__(self) -> str:
        return {
            "_id": self._id,
            "inventory": self.inventory,
            "settings": self.settings
        }.__str__()

    def __repr__(self) -> str:
        return self.__str__()
