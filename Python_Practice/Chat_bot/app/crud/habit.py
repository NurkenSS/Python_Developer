from sqlalchemy.orm import Session
from Chat_bot.app.models.user import Habit
from app.schemas.habit import HabitCreate

def create_habit(db: Session, habit: HabitCreate, user_id: int):
    db_habit = Habit(name=habit.name, description=habit.description, user_id=user_id)
    db.add(db_habit)
    db.commit()
    db.refresh(db_habit)
    return db_habit
