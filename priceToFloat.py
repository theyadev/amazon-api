def priceToFloat(price: str) -> float:
    return float(price.replace('€', "").replace("\u00a0", "").replace('\u202f', "").replace(",", "."))
