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
        keyword = body.get('keyword', '')
        if not keyword:
            return {'error': 'No keyword provided.'}

        result = scrapeNew.scrape(keyword)
        return result