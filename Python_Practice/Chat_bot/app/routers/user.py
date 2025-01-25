from fastapi import APIRouter, Depends
from requests import Session
from Chat_bot.app.routers.habit import get_db
from app.models import User
from app.schemas import UserCreate, User
from app.database import SessionLocal

router = APIRouter()

@router.post("/users/", response_model=User)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = User(email=user.email, full_name=user.full_name, password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
