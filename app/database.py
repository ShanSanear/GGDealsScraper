from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import config


engine = create_engine(
    config.DATABASE.CONNECTION_STRING,
    connect_args={"check_same_thread": False}
    # check same thread : False is only neede for sqlite
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
