import uvicorn
from fastapi import FastAPI

import routers.game
from database import Base, engine
from .config import config

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(routers.game.router)

if __name__ == "__main__":
    uvicorn.run(
        "app.main:app", host=config.APP.ADDRESS, port=config.APP.PORT, reload=True
    )
