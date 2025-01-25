from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app import crud, schemas
from app.database import SessionLocal
from app.auth import get_current_user

router = APIRouter()

# Создание привычки для текущего пользователя
@router.post("/create", response_model=schemas.Habit)
def create_habit(habit: schemas.HabitCreate, db: Session = Depends(SessionLocal), user_id: int = Depends(get_current_user)):
    """
    Создает новую привычку для текущего пользователя.
    """
    return crud.create_habit(db=db, habit=habit, user_id=user_id)

# Получение списка привычек для текущего пользователя
@router.get("/list", response_model=List[schemas.Habit])
def get_habits(db: Session = Depends(SessionLocal), user_id: int = Depends(get_current_user)):
    """
    Получить список привычек для текущего пользователя.
    """
    return crud.get_habits(db=db, user_id=user_id)
