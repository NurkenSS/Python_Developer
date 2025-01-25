from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from Chat_bot.app.get_db import SessionLocal
from Chat_bot.app.models.user import Habit

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/habits/")
def create_habit(name: str, description: str, db: Session = Depends(get_db)):
    habit = Habit(name=name, description=description)
    db.add(habit)
    db.commit()
    db.refresh(habit)
    return habit
