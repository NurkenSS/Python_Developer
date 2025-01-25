from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import crud, schemas, dependencies

router = APIRouter()

@router.post("/tweets/", response_model=schemas.Tweet)
def create_tweet(tweet: schemas.TweetCreate, db: Session = Depends(dependencies.get_db)):
    return crud.create_tweet(db=db, tweet=tweet, user_id=1)
