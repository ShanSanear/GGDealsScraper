import uvicorn
from fastapi import FastAPI

import routers.game
from database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(routers.game.router)

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
