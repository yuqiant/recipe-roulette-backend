from dao import DBManager
from model import Inventory
from bson.objectid import ObjectId

class InventoryRoute:
    def __init__(self, db_manager: DBManager):
        self.db_manager = db_manager

    # GET /user/inventory?userId=some-id
    # get the user's inventory
    def handle_get_user_inventory(self, user_id: ObjectId):
        #user = User(user_id)
        result = self.db_manager.get_collection("inventory").find_one({"user_id": user_id})
        return Inventory.fromarray(result) if result else None


    # POST /user/inventory?userId=some-id
    # updates the user's inventory
    # body: {
    #   ingredientName: string,
    #   action: string "ADD" or "REMOVE"
    # }
    def handle_update_user_inventory(self,  user_id: ObjectId, ingredient_id: ObjectId, action: str):
        # get the inventory's document as a dict
        inventory_doc = self.db_manager.get_collection("inventory").find_one({"user_id": user_id})
        if inventory_doc:
            inventory = Inventory.fromarray(inventory_doc)
            if action == "add":
                inventory.add(ingredient_id)
            elif action == "remove":
                inventory.remove(ingredient_id)
            else:
                return False
            result = self.db_manager.get_collection("inventory").update_one(
                {"user_id": user_id},
                {"$set": {"ingredients": list(inventory.get_all())}}
            )
            return result.modified_count > 0
        return False







