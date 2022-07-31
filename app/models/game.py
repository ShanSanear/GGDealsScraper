from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from database import Base


class Game(Base):
    __tablename__ = "game"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    prices = relationship("GamePrice", back_populates="game")


class GamePrice(Base):
    __tablename__ = "game_price"
    id = Column(Integer, primary_key=True, index=True)
    price = Column(String)
    game_id = Column(Integer, ForeignKey("game.id"))
    game = relationship("Game", back_populates="prices")

