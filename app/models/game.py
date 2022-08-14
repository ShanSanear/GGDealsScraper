import sqlalchemy
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship

from database import Base


class Game(Base):
    __tablename__ = "game"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    prices = relationship("GamePrice", back_populates="game")
    last_update = Column(DateTime, server_default=sqlalchemy.func.now(), onupdate=sqlalchemy.func.now())