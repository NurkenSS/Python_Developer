from fastapi import APIRouter, HTTPException
from typing import List

router = APIRouter()

likes_db = []  
@router.post("/like/{tweet_id}")
async def like_tweet(tweet_id: int):
    """Добавить лайк для твита по его ID"""
    if tweet_id in likes_db:
        raise HTTPException(status_code=400, detail="Tweet already liked")
    
    likes_db.append(tweet_id)
    return {"message": f"Tweet {tweet_id} liked!"}

@router.get("/likes/")
async def get_likes() -> List[int]:
    """Возвращает все лайкнутые твиты"""
    return likes_db