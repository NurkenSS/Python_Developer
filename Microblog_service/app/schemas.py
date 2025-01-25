from pydantic import BaseModel

class UserBase(BaseModel):
    username: str
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int

    class Config:
        orm_mode = True

class TweetBase(BaseModel):
    content: str

class TweetCreate(TweetBase):
    pass

class Tweet(TweetBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True
