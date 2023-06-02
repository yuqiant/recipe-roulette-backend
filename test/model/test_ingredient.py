from src.model import Ingredient
from bson.objectid import ObjectId
import unittest


class TestIngredient(unittest.TestCase):

    def test_ingredient_creation(self):
        ingredient = Ingredient(
            ObjectId("645eabb31408d7bd1e4c4921"), "Meat", "pork", "肉类", "猪肉")
        self.assertEqual(ingredient._id, ObjectId("645eabb31408d7bd1e4c4921"))
        self.assertEqual(ingredient.categoryEN, "Meat")
        self.assertEqual(ingredient.nameEN, "pork")
        self.assertEqual(ingredient.categoryZH, "肉类")
        self.assertEqual(ingredient.nameZH, "猪肉")

    def test_ingredient_creation_fromdict(self):
        src_dict = {'_id': ObjectId(
            '645eabb31408d7bd1e4c4921'), 'categoryEN': 'Meat', 'nameEN': 'pork', 'categoryZH': '肉类', 'nameZH': '猪肉'}
        ingredient = Ingredient.fromdict(src_dict)
        self.assertEqual(ingredient._id, ObjectId("645eabb31408d7bd1e4c4921"))
        self.assertEqual(ingredient.categoryEN, "Meat")
        self.assertEqual(ingredient.nameEN, "pork")
        self.assertEqual(ingredient.categoryZH, "肉类")
        self.assertEqual(ingredient.nameZH, "猪肉")

    def test_ingredient_todict(self):
        src_dict = {'_id': ObjectId(
            '645eabb31408d7bd1e4c4921'), 'categoryEN': 'Meat', 'nameEN': 'pork', 'categoryZH': '肉类', 'nameZH': '猪肉'}
        ingredient = Ingredient.fromdict(src_dict)
        self.assertEqual(ingredient.todict(), src_dict)

    def test_ingredient_tostring(self):
        src_dict = {'_id': ObjectId(
            '645eabb31408d7bd1e4c4921'), 'categoryEN': 'Meat', 'nameEN': 'pork', 'categoryZH': '肉类', 'nameZH': '猪肉'}
        ingredient = Ingredient.fromdict(src_dict)
        self.assertEqual(str(ingredient),
                         "{'_id': ObjectId('645eabb31408d7bd1e4c4921'), 'categoryEN': 'Meat', 'nameEN': 'pork', 'categoryZH': '肉类', 'nameZH': '猪肉'}")
