import requests
import sys

sys.path.append(r"C:\Users\stagiaire.PORT-20B-11.000\Documents\amazon-api")

from addToJson import addToJSON


def fetchAPI():
    res = requests.get("https://steamspy.com/api.php?request=all")
    return res.json()

def convertToCent(number):
    return '{:,.2f}'.format(number/100)

def fetchGames():
    games = fetchAPI()
    for id, game in games.items():
        try:
            name = game['name']
            price = float(convertToCent(int(game["price"])))
            image_url = f"https://cdn.akamai.steamstatic.com/steam/apps/{game['appid']}/header.jpg"

            print(name)
            print(price)
            print(image_url)

            if price == 0:
                continue

            addToJSON(name, price, image_url)   
        except:
            pass

def main():
    fetchGames()

if __name__ == "__main__":
    main()