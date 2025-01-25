# app/routes/tweets.py

from fastapi import APIRouter, HTTPException
from typing import List
from app.models import Tweet
from app.database import SessionLocal
from pydantic import BaseModel

router = APIRouter()

class TweetCreate(BaseModel):
    content: str
    user_id: int

class TweetResponse(TweetCreate):
    id: int

    class Config:
        orm_mode = True

@router.post("/tweets/", response_model=TweetResponse)
async def create_tweet(tweet: TweetCreate):
    db = SessionLocal()
    db_tweet = Tweet(content=tweet.content, user_id=tweet.user_id)
    db.add(db_tweet)
    db.commit()
    db.refresh(db_tweet)
    return db_tweet

@router.get("/tweets/", response_model=List[TweetResponse])
async def get_tweets():
    db = SessionLocal()
    tweets = db.query(Tweet).all()
    return tweets

@router.get("/tweets/{tweet_id}", response_model=TweetResponse)
async def get_tweet(tweet_id: int):
    db = SessionLocal()
    tweet = db.query(Tweet).filter(Tweet.id == tweet_id).first()
    if tweet is None:
        raise HTTPException(status_code=404, detail="Tweet not found")
    return tweet

@router.put("/tweets/{tweet_id}", response_model=TweetResponse)
async def update_tweet(tweet_id: int, tweet: TweetCreate):
    db = SessionLocal()
    db_tweet = db.query(Tweet).filter(Tweet.id == tweet_id).first()
    if db_tweet is None:
        raise HTTPException(status_code=404, detail="Tweet not found")
    db_tweet.content = tweet.content
    db_tweet.user_id = tweet.user_id
    db.commit()
    db.refresh(db_tweet)
    return db_tweet

@router.delete("/tweets/{tweet_id}", response_model=TweetResponse)
async def delete_tweet(tweet_id: int):
    db = SessionLocal()
    db_tweet = db.query(Tweet).filter(Tweet.id == tweet_id).first()
    if db_tweet is None:
        raise HTTPException(status_code=404, detail="Tweet not found")
    db.delete(db_tweet)
    db.commit()
    return db_tweet
