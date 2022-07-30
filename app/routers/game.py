from fastapi import APIRouter

from app.gg_deals.scraper import get_game_price

router = APIRouter()


@router.get("/game/{title}")
async def get_price(title: str):
    return get_game_price(title)
