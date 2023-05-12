import json


class User:

    def load(user_dict):
        return User(user_dict['userId'], user_dict['inventory'],
                    user_dict['settings'])

    def dump(self):
        return {
            "userId": self.__userId,
            "inventory": self.__inventory,
            "settings": self.__settings
        }

    def __init__(self, userId, inventory=set(), settings={}):
        self.userId = userId
        self.inventory = inventory
        self.settings = settings

    def __str__(self) -> str:
        return json.dumps(self.dump())

    def add_ingredient(self, ingredient):
        # add error handling
        self.inventory.add(ingredient)
        # update db

    def remove_ingredient(self, ingredient):
        # add error handling
        self.inventory.remove(ingredient)
        # update db
