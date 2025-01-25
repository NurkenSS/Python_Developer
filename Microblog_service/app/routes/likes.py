from fastapi import APIRouter, HTTPException

router = APIRouter()

fake_likes = []

@router.post("/like/{tweet_id}")
async def like_tweet(tweet_id: int):
    if tweet_id in fake_likes:
        raise HTTPException(status_code=400, detail="Tweet already liked")
    fake_likes.append(tweet_id)
    return {"message": f"Liked tweet {tweet_id}"}

@router.get("/likes/")
async def get_likes():
    return {"liked_tweet_ids": fake_likes}
