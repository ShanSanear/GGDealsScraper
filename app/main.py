import uvicorn
from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

import crud
from database import Base, SessionLocal, engine
import schemas

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
        return crud.create_game_by_title(db, game_title)
    return db_game


if __name__ == '__main__':
    uvicorn.run("app.main:app", host='0.0.0.0', port=8000, reload=True)
