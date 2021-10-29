import json

from readJson import readJSON

def addToJSON(name: str, price: float, image_url: str) -> bool:
    items = readJSON()

    if any(item for item in items if item['nom'] == name):
        return False

    items.append({
        "nom": name,
        "prix": price,
        "image": image_url
    })

    with open('./items.json', 'w', encoding='utf-8') as file:
        json.dump(items, file)
    
    return True