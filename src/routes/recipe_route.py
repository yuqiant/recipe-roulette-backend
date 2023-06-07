from dao import DBManager
from recipe import scrapeNew

class RecipesRoute:
    def __init__(self, db_manager: DBManager):
        self.db_manager = db_manager

    # POST /recipes
    # get a list of recipes based on the ingredients in the request body
    # body: {
    #   ingredients: [string]
    # }
    def handle_get_recipes_by_keyword(self, body: dict)->dict:
<<<<<<< HEAD
        #keyword = body.get('ingredients', '')
        keyword = body['ingredients']
        #print(keyword)
=======
        keyword = body.get('keyword', '')
>>>>>>> 593c3ed25b0e1d898973cd275cacd2d8c71ce39a
        if not keyword:
            return {'error': 'No keyword provided.'}

        result = scrapeNew.scrape(keyword)
<<<<<<< HEAD
        print(result)
        return result
        # keyword = body['ingredients']
        # ingredient = self.db_manager.get_collection("ingredients_json").find_one({"name": keyword})
        # if ingredient is not None and 'nameZH' in ingredient:
        #     keywordZH = ingredient['nameZH']
        # else:
        #     return {'error': 'No keyword provided.'}
        #
        # result = scrapeNew.scrape(keywordZH)
        # return result



=======
        return result
>>>>>>> 593c3ed25b0e1d898973cd275cacd2d8c71ce39a
