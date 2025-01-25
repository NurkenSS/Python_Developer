from pydantic import BaseModel

# Схема для входа пользователя (логин)
class User(BaseModel):
    username: str
    password: str

# Схема для токена
class Token(BaseModel):
    access_token: str
    token_type: str

# Схема для привычки
class HabitBase(BaseModel):
    name: str

class HabitCreate(HabitBase):
    pass

class Habit(HabitBase):
    id: int

    class Config:
        orm_mode = True
