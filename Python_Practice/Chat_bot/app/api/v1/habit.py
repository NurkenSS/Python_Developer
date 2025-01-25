from fastapi import APIRouter, Depends
from pydantic import BaseModel
from app.services.auth import get_current_user
from app.models.user import UserResponse  # Добавлен импорт UserResponse

router = APIRouter()

class HabitCreate(BaseModel):
    title: str
    description: str

class HabitResponse(BaseModel):
    id: int
    title: str
    description: str

@router.post("/create", response_model=HabitResponse)
async def create_habit(habit: HabitCreate, current_user: UserResponse = Depends(get_current_user)):
    # Логика для создания привычки
    return {"id": 1, "title": habit.title, "description": habit.description}

@router.patch("/update", response_model=HabitResponse)
async def update_habit(habit_id: int, habit: HabitCreate, current_user: UserResponse = Depends(get_current_user)):
    # Логика для частичного обновления привычки
    return {"id": habit_id, "title": habit.title, "description": habit.description}

@router.delete("/delete")
async def delete_habit(habit_id: int, current_user: UserResponse = Depends(get_current_user)):
    # Логика для удаления привычки
    return {"message": "Habit deleted successfully"}

@router.get("/user/me/habits")
async def get_user_habits(current_user: UserResponse = Depends(get_current_user)):
    # Логика для получения всех привычек текущего пользователя
    return [{"id": 1, "title": "Drink water", "description": "Drink 2 liters of water daily"}]

@router.get("/user/me/habit")
async def get_habit_by_id(habit_id: int, current_user: UserResponse = Depends(get_current_user)):
    # Логика для получения привычки по habit_id
    return {"id": habit_id, "title": "Drink water", "description": "Drink 2 liters of water daily"}
