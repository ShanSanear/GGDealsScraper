import pydantic


class ShopPrice(pydantic.BaseModel):
    name: str
    price: str
    currency: str
    approximate: bool
