from fastapi import APIRouter, Depends, HTTPException
from app.schemas import User, Token
from app.services.auth import create_access_token
from app.auth import get_current_user, get_user_from_db, verify_password

router = APIRouter()

# Эндпоинт для получения токена
@router.post("/jwt/token", response_model=Token)
async def login_for_access_token(user: User):
    # Получаем пользователя из базы данных
    db_user = get_user_from_db(user.username)
    if db_user and verify_password(user.password, db_user.password):  # Проверка пароля
        access_token = create_access_token(data={"sub": user.username})
        return {"access_token": access_token, "token_type": "bearer"}
    raise HTTPException(status_code=401, detail="Invalid credentials")

# Пример защищённого эндпоинта, где используется get_current_user
@router.get("/protected")
async def read_protected_data(current_user: dict = Depends(get_current_user)):
    return {"message": f"Welcome, {current_user['sub']}!"}
