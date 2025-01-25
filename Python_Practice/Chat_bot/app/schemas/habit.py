from app import schemas
from fastapi import APIRouter

router = APIRouter()

@router.post("/create", response_model=schemas.Habit)
async def create_habit(habit: schemas.Habit):
    return habit
