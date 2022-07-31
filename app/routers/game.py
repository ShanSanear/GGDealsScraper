from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

import crud
import schemas
from dependencies import get_db

router = APIRouter()


@router.get("/game/{game_title}", response_model=schemas.Game)
def read_game(game_title: str, db: Session = Depends(get_db)):
    db_game = crud.get_game_by_title(db, game_title=game_title)
    if db_game is None:
        return crud.create_game_by_title(db, game_title)
    return db_game
