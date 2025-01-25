from pydantic_settings import BaseSettings
from fastapi import FastAPI

class Settings(BaseSettings):
    DATABASE_URL: str

    class Config:
        env_file = ".env"

app = FastAPI()
