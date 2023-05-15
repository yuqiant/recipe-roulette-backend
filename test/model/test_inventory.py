from src.model import Ingredient, Inventory
from bson.objectid import ObjectId
import unittest


class TestInventory(unittest.TestCase):

    def test_inventory_creation(self):
        inventory = Inventory([ObjectId("645eabb31408d7bd1e4c4921"), ObjectId(
            "645eabb31408d7bd1e4c4922"), ObjectId("645eabb31408d7bd1e4c4923")])
        self.assertEqual(len(inventory), 3)

    def test_inventory_add_ingredient(self):
        inventory = Inventory()

        # adding using ObjectId
        inventory.add(ObjectId("645eabb31408d7bd1e4c4924"))
        self.assertEqual(len(inventory), 1)

        # adding using full Ingredient (Ingredient content does not matter in our case)
        inventory.add(Ingredient(id=ObjectId(
            "645eabb31408d7bd1e4c4926"), category="test", name="test", categoryZH="test", nameZH="test"))
        self.assertEqual(len(inventory), 2)

    def test_inventory_remove_ingredient(self):
        inventory = Inventory([ObjectId("645eabb31408d7bd1e4c4924"), ObjectId(
            "645eabb31408d7bd1e4c4925"), ObjectId("645eabb31408d7bd1e4c4926")])

        # removing using ObjectId
        inventory.remove(ObjectId("645eabb31408d7bd1e4c4925"))
        self.assertEqual(len(inventory), 2)

        # removing using full Ingredient (Ingredient content does not matter in our case)
        inventory.remove(Ingredient(id=ObjectId(
            "645eabb31408d7bd1e4c4926"), category="test", name="test", categoryZH="test", nameZH="test"))
        self.assertEqual(len(inventory), 1)

    def test_inventory_has_ingredient(self):
        inventory = Inventory([ObjectId("645eabb31408d7bd1e4c4924"), ObjectId(
            "645eabb31408d7bd1e4c4925"), ObjectId("645eabb31408d7bd1e4c4926")])

        # check using ObjectId
        self.assertTrue(ObjectId("645eabb31408d7bd1e4c4925") in inventory)

        # check using full Ingredient (Ingredient content does not matter in our case)
        self.assertTrue(Ingredient(id=ObjectId(
            "645eabb31408d7bd1e4c4926"), category="test", name="test", categoryZH="test", nameZH="test") in inventory)
