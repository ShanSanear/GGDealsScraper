from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from ..database import Base

# class ShopPrice(Base):
#     __tablename__ = "shop_price"
#     shop_price_id = Column(Integer, primary_key=True, index=True)
#     name = Column(String)
#     price = Column(String)
#     currency = Column(String)
#     approximate = Column(Boolean)
#     game_price_data_id = Column(Integer, ForeignKey("game_price_data.game_id"))
#     game_price = relationship("GamePriceData", back_populates="prices")
