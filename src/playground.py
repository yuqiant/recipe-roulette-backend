from dao import DBManager
from model import Ingredient, Inventory, User
from bson.objectid import ObjectId
from routes import UserRoute, IngredientRoute, InventoryRoute

# create a dbmanager
db_manager = DBManager("ingredients")

# create routes
user_route = UserRoute(db_manager)
ingredient_route = IngredientRoute(db_manager)
inventory_route = InventoryRoute(db_manager)

# get an ingredient by user_id
user_id = ObjectId("6463e5c66a39ed73a98958cc")
user = user_route.handle_get_user(user_id)
print(user)

# get an ingredient by id
ingredient_id = ObjectId("6463e5c66a39ed73a98958cc")
ingredient = ingredient_route.handle_get_by_id(ingredient_id)
print(ingredient)

# get user inventory by user id
inventory = inventory_route.handle_get_user_inventory(user_id)
print(inventory)

# add an ingredient to user inventory
ingredient_id_to_add = ObjectId("6463e5c66a39ed73a98958cc")
result = inventory_route.handle_update_user_inventory(user_id, ingredient_id_to_add, "add")
print(f"Add ingredient result: {result}")

# remove an ingredient from user inventory
ingredient_id_to_remove = ObjectId("6463e5c66a39ed73a98958cc")
result = inventory_route.handle_update_user_inventory(user_id, ingredient_id_to_remove, "remove")
print(f"Remove ingredient result: {result}")
