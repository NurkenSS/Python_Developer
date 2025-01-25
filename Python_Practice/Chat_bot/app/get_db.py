from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from Chat_bot.app.routers.habit import get_db
from app.models import User

def get_current_user(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    user = db.query(User).filter(User.token == token).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user
