from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import crud, schemas, dependencies

router = APIRouter()

@router.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(dependencies.get_db)):
    return crud.create_user(db=db, user=user)
