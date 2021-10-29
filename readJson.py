import json

def readJSON():
    try:
        with open('./items.json', 'r', encoding='utf-8') as file:
            return json.load(file)
    except:
        return []