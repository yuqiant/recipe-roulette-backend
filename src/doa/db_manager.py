from doa.local_db import JSONDB


class DBManager:

    def __init__(self, local=False, local_inventory=None, local_user=None):
        if not local:
            raise NotImplementedError("Remote DB not yet implemented")
        else:
            self.__inventory_db = JSONDB(local_inventory)
            self.__user_db = JSONDB(local_user)

    def inventory(self):
        return self.__inventory_db

    def user(self):
        return self.__user_db

    def update_inventory(self, user_id, ingredient_name, action):
        # get inventory from db
        user_inventory = self.__inventory_db.read(user_id)
        if user_inventory is None:
            user_inventory = []

        # type of input error check
        if action == "add":
            if ingredient_name in user_inventory:
                raise ValueError(f"{ingredient_name} already exists in user {user_id}'s inventory.")
            user_inventory.append(ingredient_name)
        elif action == "remove":
            if ingredient_name not in user_inventory:
                raise ValueError(f"{ingredient_name} does not exist in user {user_id}'s inventory.")
            user_inventory.remove(ingredient_name)
        else:
            raise ValueError(f"Invalid action: {action}")
        self.__inventory_db.update(user_id, user_inventory)

    def create_user(self, user_id):
        if self.__user_db.read(user_id) is not None:
            raise ValueError(f"User {user_id} already exists.")
        self.__user_db.create(user_id, [])

    def delete_user(self, user_id):
        self.__user_db.destory(user_id)


def main():
    print("hello")
