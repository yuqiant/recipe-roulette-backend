from dao import DBManager
from model import Ingredient
from bson.objectid import ObjectId


class IngredientRoute:
    def __init__(self, db_manager: DBManager):
        self.collection = db_manager.get_collection("ingredients")
        self.db_manager = db_manager

    def handle_get_all(self) -> list[Ingredient]:
        return [Ingredient.fromdict(x) for x in self.collection.find({})]

    def handle_get_by_id(self, id: ObjectId) -> Ingredient | None:
        doc = self.collection.find_one({"_id": id})
        return Ingredient.fromdict(doc) if doc else None

    def handle_get_by_ids(self, ids: list[ObjectId]) -> list[Ingredient]:
        return [Ingredient.fromdict(x) for x in self.collection.find({"_id": {"$in": ids}})]
