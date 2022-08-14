import datetime
from typing import Optional

from pydantic import BaseModel


class GamePriceBase(BaseModel):
    price: str
    shop_name: str


class GamePriceCreate(GamePriceBase):
    pass

    class Config:
        orm_mode = True


class GamePrice(GamePriceBase):
    id: Optional[int]
    game_id: Optional[int]

    class Config:
        orm_mode = True


class GameBase(BaseModel):
    id: int
    title: str
    last_update: Optional[datetime.datetime]


class GameCreate(GameBase):
    prices: Optional[list[GamePriceCreate]] = None


class Game(GameBase):
    prices: Optional[list[GamePrice]] = None

    class Config:
        orm_mode = True
