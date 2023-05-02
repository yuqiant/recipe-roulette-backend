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


def main():
    print("hello")
