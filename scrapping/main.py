from bs4 import BeautifulSoup
from selenium import webdriver
import time
import json

url = 'https://www.amazon.fr/s?k=montre'

driver = webdriver.Chrome('./chromedriver')
driver.get(url)

time.sleep(1)

soup = BeautifulSoup(driver.page_source, features="html.parser")

a = soup.find(class_='s-matching-dir')
b = a.find(class_="sg-col-inner")
c = b.find_all("span")[2]
d = c.findChildren(recursive=False)[1]
e = d.find_all(class_="s-result-item")


def readJSON():
    try:
        with open('../amazon.json', 'r', encoding='utf-8') as file:
            return json.load(file)
    except:
        return []


for test in e:
    try:
        nom = test.find("h2").text
        image_url = test.find("img")['src']
        prix_str = test.find(class_='a-offscreen').text

        amazon = readJSON()

        amazon.append({
            "nom": nom.strip(),
            "prix": float(prix_str.replace('€', "").replace("\u00a0", "").replace('\u202f', "").replace(",", ".")),
            "image": image_url
        })

        print(nom)
        print(image_url)
        print(prix_str)

        with open('../amazon.json', 'w', encoding='utf-8') as file:
            json.dump(amazon, file)
    except:
        pass
