from src.model import Ingredient, Inventory
from bson.objectid import ObjectId
import unittest


class TestInventory(unittest.TestCase):

    def test_inventory_creation(self):
        inventory = Inventory([ObjectId("645eabb31408d7bd1e4c4921"), ObjectId(
            "645eabb31408d7bd1e4c4922"), ObjectId("645eabb31408d7bd1e4c4923")])
        assert len(inventory) == 3

    def test_inventory_add_ingredient(self):
        inventory = Inventory()

        # adding using ObjectId
        inventory.add_ingredient(ObjectId("645eabb31408d7bd1e4c4924"))
        assert len(inventory) == 1

        # adding using full Ingredient (Ingredient content does not matter in our case)
        inventory.add_ingredient(Ingredient(id=ObjectId(
            "645eabb31408d7bd1e4c4926"), category="test", name="test", categoryZH="test", nameZH="test"))
        assert len(inventory) == 2

    def test_inventory_remove_ingredient(self):
        inventory = Inventory([ObjectId("645eabb31408d7bd1e4c4924"), ObjectId(
            "645eabb31408d7bd1e4c4925"), ObjectId("645eabb31408d7bd1e4c4926")])

        # removing using ObjectId
        inventory.remove_ingredient(ObjectId("645eabb31408d7bd1e4c4925"))
        assert len(inventory) == 2

        # removing using full Ingredient (Ingredient content does not matter in our case)
        inventory.remove_ingredient(Ingredient(id=ObjectId(
            "645eabb31408d7bd1e4c4926"), category="test", name="test", categoryZH="test", nameZH="test"))
        assert len(inventory) == 1

    def test_inventory_has_ingredient(self):
        inventory = Inventory([ObjectId("645eabb31408d7bd1e4c4924"), ObjectId(
            "645eabb31408d7bd1e4c4925"), ObjectId("645eabb31408d7bd1e4c4926")])

        # check using ObjectId
        assert inventory.has_ingredient(ObjectId("645eabb31408d7bd1e4c4925"))

        # check using full Ingredient (Ingredient content does not matter in our case)
        assert inventory.has_ingredient(Ingredient(id=ObjectId(
            "645eabb31408d7bd1e4c4926"), category="test", name="test", categoryZH="test", nameZH="test"))
