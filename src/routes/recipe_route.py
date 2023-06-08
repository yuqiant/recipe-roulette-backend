from dao import DBManager
from recipe import scrape

class RecipesRoute:
    def __init__(self, db_manager: DBManager):
        self.db_manager = db_manager

    # POST /recipes
    # get a list of recipes based on the ingredients in the request body
    # body: {
    #   ingredients: [string]
    # }
    # body = {"ingredients": ["鸡蛋", "猪肉"]}
    #
    def handle_get_recipes_by_keyword(self, body: dict)->dict:

        #keyword = body.get('ingredients', '')
        # keyword = body['ingredients']
        # #print(keyword)
        #
        # keyword = body.get('keyword', '')
        #
        # if not keyword:
        #     return {'error': 'No keyword provided.'}
        #
        # result = scrapeNew.scrape(keyword)
        # return result
        # keyword = body['ingredients']
        # ingredient = self.db_manager.get_collection("ingredients_json").find_one({"name": keyword})
        # if ingredient is not None and 'nameZH' in ingredient:
        #     keywordZH = ingredient['nameZH']
        # else:
        #     return {'error': 'No keyword provided.'}
        #
        # result = scrapeNew.scrape(keywordZH)
        # return result

        ingredients = body.get('ingredients', [])

        if not ingredients:
            return {'error': 'No ingredients provided.'}

        results = []
        for ingredient in ingredients:
            result = scrape.scrape(ingredient)
            results.append(result)

        return {'results': results}






