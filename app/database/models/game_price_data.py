import pydantic

from app.database.models.shop_price import ShopPrice


class GamePriceData(pydantic.BaseModel):
    game_id: int
    game_title: str
    prices: list[ShopPrice]
