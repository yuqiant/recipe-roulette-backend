import json
from src.doa.db_manager import DBManager
from src.inventory.inventory import Inventory

def handler(event, context):
    # main entry point for lambda
    # return scrape.handler({"keyword": "egg"}, None)
    # return json.dumps({"message": "To be implemented"})
    db_manager = DBManager()
    inventory = Inventory(db_manager)
    return inventory.handler(event, context)


if __name__ == '__main__':
    print(handler({"key": "value"}, None))





