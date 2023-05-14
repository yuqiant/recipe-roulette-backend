from src.model import Ingredient
from bson.objectid import ObjectId
import unittest


class TestIngredient(unittest.TestCase):

    def test_ingredient_creation(self):
        ingredient = Ingredient(
            ObjectId("645eabb31408d7bd1e4c4921"), "Meat", "pork", "肉类", "猪肉")
        assert ingredient._id == ObjectId("645eabb31408d7bd1e4c4921")
        assert ingredient.category == "Meat"
        assert ingredient.ingredientName == "pork"
        assert ingredient.categoryCN == "肉类"
        assert ingredient.ingredientNameCN == "猪肉"

    def test_ingredient_creation_fromdict(self):
        src_dict = {'_id': ObjectId(
            '645eabb31408d7bd1e4c4921'), 'category': 'Meat', 'ingredientName': 'pork', 'categoryCN': '肉类', 'ingredientNameCN': '猪肉'}
        ingredient = Ingredient.fromdict(src_dict)
        assert ingredient._id == ObjectId("645eabb31408d7bd1e4c4921")
        assert ingredient.category == "Meat"
        assert ingredient.ingredientName == "pork"
        assert ingredient.categoryCN == "肉类"
        assert ingredient.ingredientNameCN == "猪肉"

    def test_ingredient_todict(self):
        src_dict = {'_id': ObjectId(
            '645eabb31408d7bd1e4c4921'), 'category': 'Meat', 'ingredientName': 'pork', 'categoryCN': '肉类', 'ingredientNameCN': '猪肉'}
        ingredient = Ingredient.fromdict(src_dict)
        assert ingredient.todict() == src_dict

    def test_ingredient_tostring(self):
        src_dict = {'_id': ObjectId(
            '645eabb31408d7bd1e4c4921'), 'category': 'Meat', 'ingredientName': 'pork', 'categoryCN': '肉类', 'ingredientNameCN': '猪肉'}
        ingredient = Ingredient.fromdict(src_dict)
        assert str(
            ingredient) == "{'_id': ObjectId('645eabb31408d7bd1e4c4921'), 'category': 'Meat', 'ingredientName': 'pork', 'categoryCN': '肉类', 'ingredientNameCN': '猪肉'}"
