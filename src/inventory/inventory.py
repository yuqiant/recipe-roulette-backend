import json

from doa.db_manager import DBManager


def handler(data, context):
    user_id = data["userId"]
    ingredient_name = data["ingredient"]
    action = data["action"]
    result = update_inventory(user_id, ingredient_name, action)
    ret = json.dumps(result)
    return ret


def update_inventory(user_id, ingredient_name, action):
    DBManager(True, "test.json")
    print(user_id, ingredient_name, action)
    return "hi"

# # data as a dictionary
# def update_inventory(user_id, ingredient_name, action):
#     # user_id = data["userId"]
#     # ingredient_name = data["ingredient"]
#     # action = data["action"]
#
#     # load the inventory from the JSON file
#     with open("inventory.json", "r") as file:
#         inventory = json.loads(file)
#
#     # check if the user exists in the inventory
#     if user_id not in inventory:
#         raise ValueError(f"User {user_id} does not exist in the inventory.")  # follow up - register pop up or ??
#
#     # get the current inventory of the users
#     user_inventory = inventory[user_id]
#
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
