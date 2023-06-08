import json
from dao import DBManager
from routes import UserRoute
from router import Router
# from inventory.inventory import Inventory

router = Router()
db_manager = DBManager("recipe-roulette")
user_route = UserRoute(db_manager)
# router.get('/ingredient', ingredients_handler.handle_get_all(query_string))
router.post('/user', user_route.handle_create_user)
router.get('/user/settings', user_route.handle_get_user_settings)
router.post('/user/settings', user_route.handle_update_user_settings)


def handler(event, _):
    print(event)
    return router.handle(event)


# if __name__ == '__main__':
    # from bson.objectid import ObjectId
    # from bson import json_util
    # db = DBManager("recipe-roulette").get_collection("ingredients")
    # res = db.find_one({})
    # id = ObjectId(res.get("_id"))
    # print(id)

    # db_manager = DBManager("recipe-roulette")
    # user_route = UserRoute(db_manager)

    # settings = user_route.handle_get_user_settings({"userId": "124"})
    # out = json_util.dumps(settings.todict())
    # print(out)

    # user = user_route.handle_get_user("124")
    # print(user)
    # out = json_util.dumps(user.todict())
    # print(out)

    # user.inventory.add(ObjectId("5c2d5d0f2b8d9f1b0f9f8c5e"))
    # result = user_route.handle_update_user("124", user.todict())
    # print(result)

    # event = {"userId": "20394", "ingredient": "egg", "action": "add"}
    # print(handler(event, None))
    # handler(None, None)
