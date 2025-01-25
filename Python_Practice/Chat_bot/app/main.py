from fastapi import FastAPI
from app.api.v1 import user, habit

app = FastAPI()

app.include_router(user.router, prefix="/api/v1/user", tags=["User"])
app.include_router(habit.router, prefix="/api/v1/jwt/habit", tags=["Habit"])
