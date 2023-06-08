from dao import DBManager
from model import Ingredient, Inventory, User
from bson.objectid import ObjectId
from routes import UserRoute, IngredientRoute, InventoryRoute, RecipesRoute

# create a dbmanager
db_manager = DBManager("ingredients")

# create routes
user_route = UserRoute(db_manager)
ingredient_route = IngredientRoute(db_manager)
inventory_route = InventoryRoute(db_manager)
recipes_route = RecipesRoute(db_manager)

# get an ingredient by user_id
user_id = "101010"
user = user_route.handle_get_user(user_id)
print(user)

# get an ingredient by id
ingredient_id = ObjectId("646d2a4804e31f5e664e3441")
ingredient = db_manager.get_collection("ingredients_json").find_one({"name": "pork"})
ingredientObj = Ingredient.fromdict(ingredient)
#ingredient = ingredient_route.handle_get_by_id(ingredient_id)
print(ingredientObj)

# get user inventory by user id
inventory = inventory_route.handle_get_user_inventory(user_id)
print(inventory)

# add an ingredient to user inventory
ingredient_id_to_add = ObjectId("646d2a4804e31f5e664e3441")
result = inventory_route.handle_update_user_inventory(user_id, ingredient_id_to_add, "add")
print(f"Add ingredient result: {result}")

# remove an ingredient from user inventory
ingredient_id_to_remove = ObjectId("646d2a4804e31f5e664e3441")
result = inventory_route.handle_update_user_inventory(user_id, ingredient_id_to_remove, "remove")
print(f"Remove ingredient result: {result}")

body = {"ingredients": ["猪肉", "鸡蛋"]}
result = recipes_route.handle_get_recipes_by_keyword(body)
print(result)


