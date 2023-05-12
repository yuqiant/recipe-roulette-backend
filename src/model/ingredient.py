import json


class Ingredient:

    def load(ingredient_dict):
        return Ingredient(ingredient_dict['_id'], ingredient_dict['category'], ingredient_dict['ingredientName'], ingredient_dict['categoryCN'], ingredient_dict['ingredientNameCN'])

    def dump(self):
        return {
            "_id": self.id,
            "category": self.category,
            "ingredientName": self.ingredientName,
            "categoryCN": self.categoryCN,
            "ingredientNameCN": self.ingredientNameCN
        }

    def __init__(self, id, category, ingredientName, categoryCN, ingredientNameCN):
        self.id = id
        self.category = category
        self.ingredientName = ingredientName
        self.categoryCN = categoryCN
        self.ingredientNameCN = ingredientNameCN

    def __str__(self) -> str:
        return json.dumps(
            {
                "_id": f"ObjectId({self.id.__str__()})",
                "category": self.category,
                "ingredientName": self.ingredientName,
                "categoryCN": self.categoryCN,
                "ingredientNameCN": self.ingredientNameCN
            }
        )
