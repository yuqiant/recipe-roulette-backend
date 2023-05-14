from src.model import User, Ingredient
from bson.objectid import ObjectId
import unittest


class TestUser(unittest.TestCase):

    def test_user_creation(self):
        user = User("123", set(), {})
        assert user.userId == "123"

    def test_user_creation_with_ingredients(self):
        user = User("XXX", set([ObjectId("645eabb31408d7bd1e4c4921")]), {})
        assert len(user.inventory) == 1
        assert ObjectId("645eabb31408d7bd1e4c4921") in user.inventory

    def test_user_creation_fromdict(self):
        src_dict = {'userId': '1', 'inventory': [{'_id': ObjectId(
            '645eabb31408d7bd1e4c4921'), 'category': '1', 'ingredientName': 'test', 'categoryCN': 'test', 'ingredientNameCN': 'test'}], 'settings': {}}
        user = User.fromdict(src_dict)
        assert user.userId == "1"
        assert len(user.inventory) == 1
        ingredient = Ingredient.fromdict({'_id': ObjectId(
            '645eabb31408d7bd1e4c4921'), 'category': '1', 'ingredientName': 'test', 'categoryCN': 'test', 'ingredientNameCN': 'test'})
        assert ingredient in user.inventory
        user.inventory.remove(ingredient)
        assert len(user.inventory) == 0

    def test_user_todict(self):
        src_dict = {'userId': '1', 'inventory': [{'_id': ObjectId(
            '645eabb31408d7bd1e4c4921'), 'category': '1', 'ingredientName': 'test', 'categoryCN': 'test', 'ingredientNameCN': 'test'}], 'settings': {}}
        user = User.fromdict(src_dict)
        user_dict = user.todict()
        assert user_dict.get('userId') == '1'
        assert isinstance(user_dict.get('inventory'), set)
        assert isinstance(user_dict.get('settings'), dict)


if __name__ == "__main__":
    unittest.main()
