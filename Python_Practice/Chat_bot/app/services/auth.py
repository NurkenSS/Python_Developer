from fastapi import Depends, HTTPException, Security
from fastapi.security import OAuth2PasswordBearer  # Импортируем OAuth2PasswordBearer
from datetime import datetime, timedelta
from typing import Union
from jose import JWTError, jwt
from app.models import User  # Убедитесь, что это ваша модель пользователя
from passlib.context import CryptContext
from app.database import SessionLocal

# Секретный ключ для создания токенов
SECRET_KEY = "YOUR_SECRET_KEY"  # Замените на свой секретный ключ
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Для хеширования паролей
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Создаём объект oauth2_scheme
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="jwt/token")

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_user_from_db(username: str):
    # Здесь должна быть логика получения пользователя из базы данных
    db = SessionLocal()
    user = db.query(User).filter(User.username == username).first()
    db.close()
    return user

def create_access_token(data: dict, expires_delta: Union[timedelta, None] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def get_current_user(token: str = Depends(oauth2_scheme)):  # Теперь oauth2_scheme используется правильно
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Invalid token")
        return {"sub": username}  # Вернуть данные пользователя (например, "sub" - это username)
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")
    