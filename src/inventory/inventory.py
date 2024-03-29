import json
from dao.db_manager import DBManager
from model.ingredient import Ingredient


# parse input and call dbmanager
class Inventory:
    def __init__(self, db_manager: DBManager):
        self.collection = db_manager.get_collection("ingredients")
        self.db_manager = db_manager

    def handler(self, event, context):
        '''
            example of how we can perform queries on the collection
        '''
        ingredient = Ingredient.load(self.collection.find_one(
            {"ingredientName": "chicken leg"}))

        print(ingredient)
        # example output
        # {"_id": "ObjectId(645eabb31408d7bd1e4c4935)", "category": "Meat", "ingredientName": "chicken leg", "categoryCN": "\u8089\u7c7b", "ingredientNameCN": "\u9e21\u817f"}

        # ================================
        #   Nothing changed below
        # ================================

        # user_id = event["userId"]
        # ingredient_name = event["ingredient"]
        # action = event["action"]

        # if action not in ["add", "remove"]:
        #     raise ValueError(f"Invalid action: {action}")
        # if not isinstance(ingredient_name, str):
        #     raise ValueError(f"Invalid ingredient_name: {ingredient_name}")

        # if action == "add" or action == "remove":
        #     self.db_manager.update_inventory(user_id, ingredient_name, action)

        # result = self.db_manager.inventory().read(user_id)
        # ret = json.dumps(result)
        # return ret

# def handler(event, context):
#     user_id = event["userId"]
#     ingredient_name = event["ingredient"]
#     action = event["action"]
#     result = update_inventory(user_id, ingredient_name, action)
#     ret = json.dumps(result)
#     return ret


# data as a dictionary
# def update_inventory(user_id, ingredient_name, action):
#     #user_id = data["userId"]
#     #ingredient_name = data["ingredient"]
#     #action = data["action"]
#
#     # load the inventory from the JSON file
#     with open("inventory.json", "r") as file:
#         inventory = json.loads(file)
#
#     # check if the user exists in the inventory
#     if user_id not in inventory:
#         raise ValueError(f"User {user_id} does not exist in the inventory.")
#         # follow up - register pop up or ??
#
#     # get the current inventory of the users
#     user_inventory = inventory[user_id]
#
#     # type of input error check
#     if action == "add" and ingredient_name in user_inventory:
#         raise ValueError(f"{ingredient_name} already exists in user {user_id}'s inventory.")
#     elif action == "remove" and ingredient_name not in user_inventory:
#         raise ValueError(f"{ingredient_name} does not exist in user {user_id}'s inventory.")
#
#     # update the inventory
#     if action == "add":
#         user_inventory.append(ingredient_name)
#     elif action == "remove":
#         user_inventory.remove(ingredient_name)
#
#     inventory[user_id] = user_inventory
#
#     # write the updated inventory dictionary with the new inventory
#     with open("inventory.json", "w") as file:
#         json.dump(inventory, file)
#
#     return inventory
