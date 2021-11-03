import requests
import sys


sys.path.append('./')

from addToJson import addToJSON
from priceToFloat import priceToFloat


def fetchGames() -> dict:
    res = requests.get("https://steamspy.com/api.php?request=all")
    return res.json()


def convertToCent(number: int) -> str:
    return '{:,.2f}'.format(number / 100)


def fetchGamesPrice(games: dict) -> dict:
    ids = [id for id in games.keys()]

    data = {}

    res = requests.get(
        f"https://store.steampowered.com/api/appdetails?filters=price_overview&appids={','.join(ids[:500])}")

    data.update(res.json())

    # res = requests.get(
    #     f"https://store.steampowered.com/api/appdetails?filters=price_overview&appids={','.join(ids[501:])}")

    # data.update(res.json())

    return data


def getImageUrl(id: int) -> str:
    return f"https://cdn.akamai.steamstatic.com/steam/apps/{id}/header.jpg"

def updateGamesToJSON():
    games = fetchGames()

    games_prices = fetchGamesPrice(games)

    for game in games.values():
        try:
            name: str = game['name']

            not_updated_price = float(convertToCent(int(game["price"])))

            image_url = getImageUrl(game['appid'])

            if not_updated_price == 0:
                continue

            if games_prices[str(game['appid'])]['data'] == []:
                continue

            price_str: str = games_prices[str(
                game['appid'])]['data']['price_overview']['final_formatted']

            price = priceToFloat(price_str)

            addToJSON(name, price, image_url, "game")
        except:
            continue


def main():
    updateGamesToJSON()


if __name__ == "__main__":
    main()
