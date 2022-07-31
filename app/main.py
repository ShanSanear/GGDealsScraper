#
# from .routers import game
#
# app.include_router(game.router)
#
# @app.get("/")
# async def root():
#     return {"message": "Hello Bigger Applications!"}
#
import uvicorn
from fastapi import Depends, HTTPException, FastAPI
from sqlalchemy.orm import Session

import crud
from database import Base, SessionLocal, engine
import schemas
from gg_deals import scraper

app = FastAPI()
Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/game/{game_title}", response_model=schemas.Game)
def read_game(game_title: str, db: Session = Depends(get_db)):
    db_game = crud.get_game_by_title(db, game_title=game_title)
    if db_game is None:
        print("Generating")
        return crud.create_game_by_title(db, game_title)
        # db_game = scraper.get_game_prices(game_title)
        # db.add(db_game)
        # db.commit()
        # db.refresh(db_game)
        pass
        # raise HTTPException(status_code=404, detail="Game not found")
    print("Found!")
    return db_game

if __name__ == '__main__':
    uvicorn.run("app.main:app", host='0.0.0.0', port=8000, reload=True)