import json
from dao import DBManager
from routes import UserRoute
# from inventory.inventory import Inventory

# router = Router()
# router.get('/ingredient', ingredients_handler.handle_get_all(query_string))
# router.get('/ingredient?id=some_id', ingredients_handler.handle_get_by_id(query_string))


def handler(event, context):
    print(event)

    # main entry point for lambda
    # return scrape.handler({"keyword": "egg"}, None)
    # return json.dumps({"message": "To be implemented"})
    # db_manager = DBManager(db_name="recipe-roulette")
    # create a router to handle routing to the correct handler
    # inventory = Inventory(db_manager)
    # return inventory.handler(event, context)


if __name__ == '__main__':
    # from dao import DBManager
    from bson.objectid import ObjectId
    # db = DBManager("recipe-roulette").get_collection("ingredients")
    # res = db.find_one({})
    # id = ObjectId(res.get("_id"))
    # print(id)

    db_manager = DBManager("recipe-roulette")
    user_route = UserRoute(db_manager)
    user = user_route.handle_get_user("124")
    user.inventory.add(ObjectId("5c2d5d0f2b8d9f1b0f9f8c5e"))
    result = user_route.handle_update_user("124", user.todict())
    print(result)

    # event = {"userId": "20394", "ingredient": "egg", "action": "add"}
    # print(handler(event, None))
    # handler(None, None)
