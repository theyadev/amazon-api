import json

from readJson import readJSON


def getIndex(list: list, key: str, expectedValue):
    return next((index for (index, d) in enumerate(list) if d[key] == expectedValue), None)

def addToJSON(name: str, price: float, image_url: str, category: str = None) -> bool:
    items = readJSON()

    index = getIndex(list=items, key="nom", expectedValue=name)

    if index is not None:
        if items[index]['prix'] == price:
            return False

        items.pop(index)

    items.append({
        "nom": name,
        "prix": price,
        "image": image_url,
        "category": category
    })

    with open('./items.json', 'w', encoding='utf-8') as file:
        json.dump(items, file)

    print(name)
    print(price)
    print(image_url)

    return True
