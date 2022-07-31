from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from database import Base


class GamePrice(Base):
    __tablename__ = "game_price"
    id = Column(Integer, primary_key=True, index=True)
    price = Column(String)
    shop_name = Column(String)
    game_id = Column(Integer, ForeignKey("game.id"))
    game = relationship("Game", back_populates="prices")
