from src.model import User, Ingredient, Inventory
from bson.objectid import ObjectId
import unittest


class TestUser(unittest.TestCase):

    def test_user_creation(self):
        user = User("123", Inventory(), {})
        self.assertEqual(user._id, "123")

    def test_user_creation_with_ingredients(self):
        user = User("XXX", Inventory(
            [ObjectId("645eabb31408d7bd1e4c4921")]), {})
        self.assertEqual(len(user.inventory), 1)
        self.assertTrue(ObjectId("645eabb31408d7bd1e4c4921") in user.inventory)

    def test_user_creation_fromdict(self):
        src_dict = {'_id': '1', 'inventory': [
            ObjectId('645eabb31408d7bd1e4c4921')], 'settings': {}}
        user = User.fromdict(src_dict)
        self.assertEqual(user._id, "1")
        self.assertEqual(len(user.inventory), 1)
        ingredient = Ingredient.fromdict({'_id': ObjectId(
            '645eabb31408d7bd1e4c4921'), 'categoryEN': '1', 'nameEN': 'test', 'categoryZH': 'test', 'nameZH': 'test'})
        self.assertTrue(ingredient in user.inventory)
        user.inventory.remove(ingredient)
        self.assertEqual(len(user.inventory), 0)

    def test_user_todict(self):
        src_dict = {'_id': '1', 'inventory': [
            ObjectId('645eabb31408d7bd1e4c4921'), ObjectId('645eabb31408d7bd1e4c4922')], 'settings': {}}
        user = User.fromdict(src_dict)
        user_dict = user.todict()
        self.assertEqual(user_dict.get('_id'), '1')
        self.assertTrue(isinstance(user_dict.get('inventory'), list))
        self.assertTrue(isinstance(user_dict.get('settings'), dict))
