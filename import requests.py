import requests
from bs4 import BeautifulSoup


def get_html(url):
    response = requests.get(url)
    html = response.text
    return html


def main():
    url = input("Enter a URL: ")
    html = get_html(url)
    print(html)


if __name__ == "__main__":
    main()