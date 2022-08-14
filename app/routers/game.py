from datetime import datetime, timedelta

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
    elif db_game.last_update is None or (datetime.now() - db_game.last_update) > timedelta(days=7):
        return crud.update_game_by_title(db, game_title)
    return db_game
