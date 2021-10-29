import requests
import sys

sys.path.append(r"C:\Users\stagiaire.PORT-20B-11.000\Documents\amazon-api")

from addToJson import addToJSON


def fetchAPI():
    res = requests.get("https://steamspy.com/api.php?request=all")
    return res.json()


def convertToCent(number):
    return '{:,.2f}'.format(number / 100)


def fetchGames():
    games = fetchAPI()
    ids = [id for id in games.keys()]

    data = {}

    res = requests.get(
        f"https://store.steampowered.com/api/appdetails?filters=price_overview&appids={','.join(ids[:500])}")

    data.update(res.json())

    res = requests.get(
        f"https://store.steampowered.com/api/appdetails?filters=price_overview&appids={','.join(ids[501:])}")

    data.update(res.json())

    for id, game in games.items():
        try:
            name = game['name']
            price = float(convertToCent(int(game["price"])))
            image_url = f"https://cdn.akamai.steamstatic.com/steam/apps/{game['appid']}/header.jpg"

            if price == 0:
                continue

            if data[str(game['appid'])]['data'] == []:
                continue

            price = float(data[str(game['appid'])]['data']['price_overview']['final_formatted'].replace(
                '€', "").replace("\u00a0", "").replace('\u202f', "").replace(",", "."))

            res = addToJSON(name, price, image_url)

            if res == True:
                print(name)
                print(price)
                print(image_url)
        except:
            pass


def main():
    fetchGames()


if __name__ == "__main__":
    main()
