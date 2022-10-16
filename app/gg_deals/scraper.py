import random

import requests
from bs4 import BeautifulSoup
from urllib.parse import quote_plus

import schemas

GG_DEALS_LANGUAGE = "pl"
GG_DEALS_GAME_LINK = f"https://gg.deals/{GG_DEALS_LANGUAGE}/game/{{}}/"


def get_soup(link, headers):
    response = requests.get(link, headers=headers)

    response.raise_for_status()
    return BeautifulSoup(response.content, "html.parser")


def get_game_prices(title) -> schemas.GameCreate:
    simplified_title = (
        title.replace(" ", "-")
        .replace(":", "-")
        .replace("--", "-")
        .replace("!", "")
        .replace("'", "")
        .replace("™", "")
        .replace("®", "")
        .replace("--", "-")
    )
    print(f"Trying to find game with title: {simplified_title}")
    link = GG_DEALS_GAME_LINK.format(quote_plus(simplified_title))
    headers = {"X-Requested-With": "XMLHttpRequest"}
    try:
        soup = get_soup(link, headers=headers)
    except requests.exceptions.HTTPError as err:
        print(f"Couldn't find the game: {title}")
        raise
    game_name = soup.find("a", {"class": "game-price-anchor-link"})
    found_title = game_name.find("h1").text
    if not title.lower() in found_title.lower():
        print(
            f"Title mismatch, found text header: {found_title}, requested: {title}. Double check if it correct"
        )
    game_header = soup.find("div", {"class": "game-header-box"})
    game_id = game_header.attrs["data-container-game-id"]
    shops = soup.findAll("div", {"class": "game-deals-item"})
    prices = []
    for shop in shops:
        shop_name = shop.find_all_next("img")[0]["alt"]
        price_entry = shop.find("span", {"class": "game-price-current"}).text.strip()
        price, currency = price_entry.split(" ")
        approximate = "~" in price
        price = price.replace("~", "")
        prices.append(schemas.GamePriceCreate(price=price, shop_name=shop_name))
    return schemas.GameCreate(id=int(game_id), title=title, prices=prices)
