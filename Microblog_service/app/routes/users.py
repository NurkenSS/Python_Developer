from fastapi import APIRouter, HTTPException
from typing import List
from pydantic import BaseModel

router = APIRouter()

class User(BaseModel):
    id: int
    username: str
    email: str

fake_users = []

@router.post("/users/", response_model=User)
async def create_user(user: User):
    fake_users.append(user)
    return user

@router.get("/users/", response_model=List[User])
async def get_users():
    return fake_users

@router.get("/users/{user_id}", response_model=User)
async def get_user(user_id: int):
    if user_id >= len(fake_users):
        raise HTTPException(status_code=404, detail="User not found")
    return fake_users[user_id]

@router.put("/users/{user_id}", response_model=User)
async def update_user(user_id: int, user: User):
    if user_id >= len(fake_users):
        raise HTTPException(status_code=404, detail="User not found")
    fake_users[user_id] = user
    return user

@router.delete("/users/{user_id}", response_model=User)
async def delete_user(user_id: int):
    if user_id >= len(fake_users):
        raise HTTPException(status_code=404, detail="User not found")
    deleted_user = fake_users.pop(user_id)
    return deleted_user
