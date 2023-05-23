from dao import DBManager
from model import User, UserSettings
from pymongo.results import UpdateResult, InsertOneResult
from typing import Any


class UserRoute:

    def __init__(self, db_manager: DBManager):
        self.db_manager = db_manager

    # POST /user
    # body {userId: some-id}
    def handle_create_user(self, _: dict, body: dict) -> Any:
        user_id = body.get("userId")
        user_language = body.get("language")
        user = User(user_id)
        user.settings = UserSettings(language=user_language)
        result = self.db_manager.get_collection(
            "users").insert_one(user.todict())
        return result.inserted_id

    def handle_get_user(self, user_id) -> dict:
        user = User.fromdict(self.db_manager.get_collection(
            "users").find_one({"_id": user_id}))
        return user.todict()

    # GET user's settings
    # GET /user/settings?userId=some-id
    def handle_get_user_settings(self, query_params: dict, _: dict) -> dict:
        user_id = query_params.get("userId")[0]
        user = User.fromdict(self.db_manager.get_collection(
            "users").find_one({"_id": user_id}))
        return user.settings.todict()

    # POST /user/settings
    # body {userId: some-id, settings: {...}}
    def handle_update_user_settings(self, _: dict, body: dict) -> Any:
        user_id = body.get("userId")
        user = User.fromdict(self.db_manager.get_collection(
            "users").find_one({"_id": user_id}))
        user.settings = UserSettings.fromdict(body)
        result = self.db_manager.get_collection("users").update_one(
            filter={"_id": user_id}, update={"$set": user.todict()})
        return result.upserted_id
