from pymongo.mongo_client import MongoClient
from dotenv import load_dotenv
import os


class DBManager:

    def __init__(self, db_name):
        load_dotenv()
        # read mongodb_uri_dev from .env file
        env = os.getenv("ENV")
        uri = os.getenv(f"MONGODB_URI_{env}")
        print(f"Connecting to MongoDB in {env}")
        # Create a new client and connect to the server
        self.__client = MongoClient(
            host=uri, maxPoolSize=10, appname="recipe_roulette")
        # self.__client = MongoClient(uri)
        self.__db = self.__client.get_database(db_name)

    def get_db(self):
        return self.__db

    def get_collection(self, collection_name):
        return self.__db.get_collection(collection_name)

    def close(self):
        self.__client.close()

    # def __users_collection(self):
    #     return self.__db.get_collection("user")

    # def __ingredients_collection(self):
    #     return self.__db.get_collection("ingredient")

    # def update_inventory(self, user_id, ingredient_name, action):
    #     # get current user inventory from db
    #     user_inventory = self.__users_collection().find_one({"_id": user_id})
    #     if user_inventory is None:
    #         user_inventory = []

        # user_inventory = self.__inventory_db.read(user_id)
        # if user_inventory is None:
        #     user_inventory = []

        # # type of input error check
        # if action == "add":
        #     if ingredient_name in user_inventory:
        #         raise ValueError(
        #             f"{ingredient_name} already exists in user {user_id}'s inventory.")
        #     user_inventory.append(ingredient_name)
        # elif action == "remove":
        #     if ingredient_name not in user_inventory:
        #         raise ValueError(
        #             f"{ingredient_name} does not exist in user {user_id}'s inventory.")
        #     user_inventory.remove(ingredient_name)
        # else:
        #     raise ValueError(f"Invalid action: {action}")
        # self.__inventory_db.update(user_id, user_inventory)

    # def create_user(self, user_id):
    #     if self.__user_db.read(user_id) is not None:
    #         raise ValueError(f"User {user_id} already exists.")
    #     self.__user_db.create(user_id, [])

    # def delete_user(self, user_id):
    #     self.__user_db.destory(user_id)
