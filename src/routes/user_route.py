from dao import DBManager
from model import User


class UserRoute():

    def __init__(self, db_manager: DBManager):
        self.db_manager = db_manager

    def handle_create_default_user(self, user_id):
        user = User(user_id)
        result = self.db_manager.get_collection(
            "users").insert_one(user.todict())
        return result

    def handle_get_user(self, user_id):
        user = User.fromdict(self.db_manager.get_collection(
            "users").find_one({"_id": user_id}))
        return user

    def handle_update_user(self, user_id, user_data):
        result = self.db_manager.get_collection("users").update_one(
            filter={"_id": user_id}, update={"$set": user_data})
        return result

    # GET user's settings
    # GET /user/settings?userId=some-id
    def handle_get_user_settings(self, user_id):
        pass

    # POST /user/settings?userId=some-id
    def handle_update_user_settings(self, user_id, user_settings):
        pass
