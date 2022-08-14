from datetime import datetime

import sqlalchemy
from sqlalchemy.orm import Session

import models, schemas
import models.game_price
from gg_deals import scraper


def get_game(db: Session, game_id: int):
    return db.query(models.Game).filter(models.Game.id == game_id).first()


def get_game_by_title(db: Session, game_title: str):
    query = db.query(models.Game)
    filtered = query.filter(
        sqlalchemy.func.lower(models.Game.title) == sqlalchemy.func.lower(game_title)
    )
    return filtered.first()


def create_game(db: Session, game: schemas.GameCreate):
    db_game = models.Game(title=game.title)
    db.add(db_game)
    db.commit()
    db.refresh(db_game)
    return db_game


def create_game_price(db: Session, game_price: schemas.GamePriceCreate, game_id: int):
    db_item = models.game_price.GamePrice(**game_price.dict(), game_id=game_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def update_game_by_title(db: Session, game_title: str) -> models.Game:
    game_db_item = get_game_by_title(db, game_title)
    scrapped_info = scraper.get_game_prices(game_title)
    prices = [
        models.GamePrice(**price_info.dict()) for price_info in scrapped_info.prices
    ]
    game_db_item.prices = prices
    game_db_item.last_update = datetime.now()
    db.add(game_db_item)
    db.commit()
    db.refresh(game_db_item)
    return game_db_item


def create_game_by_title(db: Session, game_title: str) -> models.Game:
    scrapped_info = scraper.get_game_prices(game_title)
    db_item = models.Game(
        title=scrapped_info.title,
        id=scrapped_info.id,
        prices=[
            models.GamePrice(**price_info.dict()) for price_info in scrapped_info.prices
        ],
    )
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
