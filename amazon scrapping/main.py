from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import sys

sys.path.append('./')

from addToJson import addToJSON
from priceToFloat import priceToFloat


def fetchFromAmazon(query):
    url = f'https://www.amazon.fr/s?k={query}'

    driver = None

    chrome_options = Options()
    chrome_options.add_argument("--headless")

    try:
        driver = webdriver.Chrome('./chromedriver', options=chrome_options)
    except:
        driver = webdriver.Chrome(
            './amazon scrapping/chromedriver', options=chrome_options)

    driver.get(url)

    soup = BeautifulSoup(driver.page_source, features="html.parser")

    catalog_div = soup.find_all(class_="s-result-item")

    for product_div in catalog_div:
        try:
            price_str = product_div.find(class_='a-offscreen').text
            price = priceToFloat(price_str)

            name = product_div.find("h2").text.strip()

            image_url = product_div.find("img")['src']

            addToJSON(name, price, image_url, "amazon")
        except:
            pass

    driver.quit()


if __name__ == "__main__":
    query = input("Que voulez vous ajouter comme articles ? ")

    fetchFromAmazon(query)
