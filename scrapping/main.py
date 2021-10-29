# import requests
# from bs4 import BeautifulSoup 


# mot="dyson"

# url = "https://www.amazon.fr/s?k="+mot

# response = requests.get(url)

# soup = BeautifulSoup(response.text, features="html.parser")
# title = soup.find(".s-result-item")
# print(soup)


##### TEST SITE DYNAMIQUE : PAS DE REQUESTS MAIS SELENIUM

# from bs4 import BeautifulSoup
# from selenium import webdriver
# import time

# url = 'https://www.webscraper.io/test-sites/e-commerce/ajax/computers/laptops'

# # Change argument to the location you installed the chrome driver
# # (see selenium installation instructions, or get the driver for your
# # system from https://sites.google.com/a/chromium.org/chromedriver/downloads)
# driver = webdriver.Chrome('./chromedriver')
# driver.get(url)

# # Give the javascript time to render
# time.sleep(1)

# # Now we have the page, let BeautifulSoup do the rest!
# soup = BeautifulSoup(driver.page_source)

# # The text containing title and price are in a
# # div with class caption.
# for caption in soup.find_all(class_='caption'):
#     product_name = caption.find(class_='title').text
#     price = caption.find(class_='pull-right price').text
#     print(product_name, price)


## AMAZON


from bs4 import BeautifulSoup
from selenium import webdriver
import time
import json

url = 'https://www.amazon.fr/s?k=montre'

# Change argument to the location you installed the chrome driver
# (see selenium installation instructions, or get the driver for your
# system from https://sites.google.com/a/chromium.org/chromedriver/downloads)
driver = webdriver.Chrome('./chromedriver')
driver.get(url)

# Give the javascript time to render
time.sleep(1)

# Now we have the page, let BeautifulSoup do the rest!
soup = BeautifulSoup(driver.page_source, features="html.parser")

# The text containing title and price are in a
# div with class caption.
#for caption in soup.find(class_='s-matching-dir'):
    #product_name = caption.find(class_='title').text
    #price = caption.find(class_='pull-right price').text
    #print(caption)

a=soup.find(class_='s-matching-dir')
b=a.find(class_="sg-col-inner")
c=b.find_all("span")[2]
d=c.findChildren(recursive=False)[1]
e=d.find_all(class_="s-result-item")

def readJSON():
    try:
        with open('../amazon.json', 'r', encoding='utf-8') as file:
            return json.load(file)
    except:
        return []

for test in e:
    try:
        f=test.find("h2").text
        g=test.find("img")['src']
        h=test.find(class_='a-offscreen').text

        amazon = readJSON()

        amazon.append({
            "nom": f.strip(),
            "prix": float(h.replace('€', "").replace("\u00a0", "").replace('\u202f', "").replace(",", ".")),
            "image": g
        })

        print(f)
        print(g)
        print(h)

        with open('../amazon.json', 'w', encoding='utf-8') as file:
            json.dump(amazon, file)


    except:
        pass