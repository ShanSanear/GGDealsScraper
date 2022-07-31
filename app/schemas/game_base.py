from typing import Optional

from pydantic import BaseModel


class GamePriceBase(BaseModel):
    price: str


class GamePriceCreate(GamePriceBase):
    pass


class GamePrice(GamePriceBase):
    id: int
    game_id: int
    shop_name: str

    class Config:
        orm_mode = True


class GameBase(BaseModel):
    title: str


class GameCreate(GameBase):
    pass


class Game(GameBase):
    id: int
    prices: Optional[list[GamePrice]] = None

    class Config:
        orm_mode = True
