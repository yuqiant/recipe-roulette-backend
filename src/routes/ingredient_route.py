from dao import DBManager
from model import Ingredient
from bson.objectid import ObjectId


class IngredientRoute:
    def __init__(self, db_manager: DBManager):
        self.db_manager = db_manager

    # GET /ingredients
    def handle_get_all(self) -> list[Ingredient]:
        return [Ingredient.fromdict(x) for x in self.db_manager.get_collection("ingredients").find({})]

    # GET /ingredients?id=some_id
    def handle_get_by_id(self, id: ObjectId) -> Ingredient | None:
        doc = self.db_manager.get_collection("ingredients").find_one({"_id": id})
        return Ingredient.fromdict(doc) if doc else None

    # GET /
    def handle_get_by_ids(self, ids: list[ObjectId]) -> list[Ingredient]:
        return [Ingredient.fromdict(x) for x in self.db_manager.get_collection("ingredients").find({"_id": {"$in": ids}})]

