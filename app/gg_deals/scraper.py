import random

import requests
from bs4 import BeautifulSoup
from urllib.parse import quote_plus

import schemas

GG_DEALS_GAME_LINK = "https://gg.deals/game/{}/"


def get_soup(link, headers):
    response = requests.get(link, headers=headers)
    response.raise_for_status()
    return BeautifulSoup(response.content, "html.parser")


def get_game_prices(title) -> schemas.Game:
    link = GG_DEALS_GAME_LINK.format(quote_plus(title.replace(" ", "-")))
    headers = {"X-Requested-With": "XMLHttpRequest"}
    soup = get_soup(link, headers=headers)
    game_name = soup.find("a", {"class": "game-price-anchor-link"})
    found_title = game_name.find("h1").text
    assert title.lower() in found_title.lower(), f"Title mismatch, found text header: {found_title}, requested: {title}"
    game_header = soup.find("div", {"class": "game-header-box"})
    game_id = game_header.attrs['data-container-game-id']
    shops = soup.findAll("div", {"class": "game-deals-item"})
    prices = []
    for shop in shops:
        shop_name = shop.find_all_next("img")[0]['alt']
        price_entry = shop.find("span", {"class": "game-price-current"}).text.strip()
        price, currency = price_entry.split(" ")
        approximate = "~" in price
        price = price.replace("~", "")
        prices.append(schemas.GamePrice(
            id=random.randint(0, 12312431234), # TODO - remove this randomness lol
            game_id=int(game_id),
            price=price,
        ))
    return schemas.Game(
        id=int(game_id),
        title=title,
        prices=prices
    )
