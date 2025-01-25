from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from app import crud, models, schemas
from app.database import SessionLocal
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from typing import Optional

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

SECRET_KEY = "your_secret_key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def verify_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(SessionLocal)):
    try:
        payload = verify_token(token)
        user = crud.get_user(db, user_id=payload["sub"])  # 'sub' - это поле, где хранится ID пользователя в токене
        if user is None:
            raise HTTPException(status_code=401, detail="User not found")
        return user
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")
    