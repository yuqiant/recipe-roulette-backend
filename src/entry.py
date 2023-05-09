import json
from doa.db_manager import DBManager
from inventory.inventory import Inventory

def handler(event, context):
    # main entry point for lambda
    # return scrape.handler({"keyword": "egg"}, None)
    # return json.dumps({"message": "To be implemented"})
    db_manager = DBManager(local=True, local_inventory="test.json")
    inventory = Inventory(db_manager)
    return inventory.handler(event, context)


if __name__ == '__main__':
    event = {
    "userId": "20394",
    "ingredient" : "egg",
    "action": "add"}
    print(handler(event, None))





