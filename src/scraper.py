from pathlib import Path

import requests
from bs4 import BeautifulSoup
from urllib.parse import quote_plus

from src.database.models.game_price_data import GamePriceData
from src.database.models.shop_price import ShopPrice

GG_DEALS_GAME_LINK = "https://gg.deals/game/{}/"


def get_soup(link, headers):
    response = requests.get(link, headers=headers)
    response.raise_for_status()
    return BeautifulSoup(response.content, "html.parser")


def get_game_price(title):
    link = GG_DEALS_GAME_LINK.format(quote_plus(title.replace(" ", "-")))
    headers = {"X-Requested-With": "XMLHttpRequest"}
    soup = get_soup(link, headers=headers)
    game_name = soup.find("a", {"class": "game-price-anchor-link"})
    found_title = game_name.find("h1").text
    assert title.lower() in found_title.lower(), f"Title mismatch, found text header: {found_title}, requested: {title}"
    game_header = soup.find("div", {"class" : "game-header-box"})
    game_id = game_header.attrs['data-container-game-id']
    shops = soup.findAll("div", {"class": "game-deals-item"})
    game_price_data = GamePriceData(
        game_id=int(game_id),
        game_title=title,
        prices=[]
    )
    for shop in shops:
        shop_name = shop.find_all_next("img")[0]['alt']
        price_entry = shop.find("span", {"class" : "game-price-current"}).text.strip()
        price, currency = price_entry.split(" ")
        approximate = "~" in price
        price = price.replace("~", "")
        game_price_data.prices.append(ShopPrice(
            name=shop_name,
            price=price,
            currency=currency,
            approximate=approximate
        ))

    print(
        game_price_data
    )
    Path("out.json").write_text(game_price_data.json(indent=4), encoding='utf-8')


get_game_price("Elden Ring")
