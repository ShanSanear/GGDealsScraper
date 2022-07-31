# import pydantic
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.models.shop_price import ShopPrice
from ..database import Base

# class GamePriceData(Base):
#     __tablename__ = 'game_price_data'
#     game_id = Column(Integer, primary_key=True, index=True)
#     game_title = Column(String)
#     prices = relationship("ShopPrice", back_populates='game_price')
#     # prices: list[ShopPrice]
#
