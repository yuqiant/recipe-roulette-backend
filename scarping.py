
#Python program to scrape website 
#and save quotes from website
import requests
from bs4 import BeautifulSoup
import csv
   

headers={
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'
}
   
res_foods = requests.get('https://www.xiachufang.com/search/?keyword=%E9%B8%A1%E8%9B%8B&cat=1001',headers =headers)
bs_foods = BeautifulSoup(res_foods.text,'html.parser')
list_title =bs_foods.find_all('div',class_='recipe-menus')  #查找所有的包含菜名和url 的标签
list_ingredients =bs_foods.find_all('p',class_='ing ellipsis') #查找所有包含食材的标签
#list_rating = bs_foods.find_all('p', class_= '')
list_graph = bs_foods.find_all('img', class_ = 'recipe-menu-cover')
for x in range(len(list_title)): 
    name = list_title[x].text.strip()
    url = list_title[x].find('a')['href']
    print_url ='http://www.xiachufang.com'+url
    ingredients = list_title[x].text.strip()
    print(name,'\n',print_url,'\n',ingredients)
   