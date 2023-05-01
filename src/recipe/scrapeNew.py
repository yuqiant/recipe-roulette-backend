import requests
from bs4 import BeautifulSoup
import json



def handler(event, context):
    # if statements for the functions
    # union of two functions


    keyword = event['keyword']
    result = scrape(keyword)
    ret = json.dumps(result)
    return ret


def scrape(keyword):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/85.0.4183.102 Safari/537.36'}
    # Send a GET request to the URL
    response = requests.get(f'https://www.lezuocai.com/so/{keyword}/', headers=headers)

    # Parse the HTML content of the response using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all the recipe items on the page
    recipe_items = soup.select('body > section > div.search-list > ul > li')

    # Loop through the recipe items and extract the relevant data
    recipes = []
    for item in recipe_items:
        title = item.find('span', class_='tit').find('a').text.strip()
        link_to_recipe = item.find('a', class_='cover')['href']
        ingredientsURL = requests.get(link_to_recipe)
        ingre_soup = BeautifulSoup(ingredientsURL.text, 'html.parser')
        ingredients_items = ingre_soup.select('body > div.main > div.left > div.recipe-ings > table > tbody > tr')
        ingredients = []
        for item_ingredient in ingredients_items:
            ingredient = item_ingredient.find('td', class_='ings-name').text.strip()
            ingredients.append(ingredient)

        thumbnail_href = item.find('img')['src']
        recipe = {'title': title, 'link_to_recipe': link_to_recipe, 'thumbnail': thumbnail_href,
                  'ingredients': ingredients}
        recipes.append(recipe)

    print(recipes)

    # Create a dictionary containing the recipes and convert it to JSON
    result = {'recipes': recipes}
    print(result)
    return result


if __name__ == '__main__':
    handler(event, None)
