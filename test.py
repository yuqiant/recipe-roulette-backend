import requests
from bs4 import BeautifulSoup
import json


def handler(event, context):
    keyword = event['keyword']
    result = scrape(keyword)
    ret = json.dumps(result)
    return ret




def scrape(keyword):

    headers={
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'
    }
    # Send a GET request to the URL
    response = requests.get(f'https://www.xiachufang.com/search/?keyword={keyword}&cat=1001',headers= headers)

    # Parse the HTML content of the response using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all the recipe items on the page
    recipe_items = soup.select('body > div.page-outer > div > div > div.pure-u-2-3.main-panel > div.white-bg.block > div > div.pure-u-3-4.search-result-list > div.normal-recipe-list > ul > li > div')


    # Loop through the recipe items and extract the relevant data
    recipes = []
    for item in recipe_items:
        title = item.find('p', class_='name').find('a').text.strip()
        ingredients = item.find('p',class_='ing ellipsis').text.strip().split('、')
        try:
            rating = float(item.find('span',class_='score bold green-font').text.strip())
        except AttributeError:
            rating = 0
        link_to_recipe = item.find('a')['href']
        thumbnail_href = item.find('img')['data-src']
        recipe = {'title': title, 'ingredients': ingredients, 'rating': rating, 'link_to_recipe': link_to_recipe, 'thumbnail':thumbnail_href}
        recipes.append(recipe)
    print(recipes)

    # Create a dictionary containing the recipes and convert it to JSON
    result = {'recipes': recipes}
    print(result)
    return result


if __name__ == '__main__':
    scrape('keyword')

