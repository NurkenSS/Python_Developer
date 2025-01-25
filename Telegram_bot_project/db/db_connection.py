from peewee import PostgresqlDatabase
import os
from dotenv import load_dotenv
from urllib.parse import urlparse

load_dotenv()

DATABASE_URL = os.getenv('DATABASE_URL')

url = urlparse(DATABASE_URL)
DATABASE_NAME = url.path[1:]
DATABASE_USER = url.username
DATABASE_PASSWORD = url.password
DATABASE_HOST = url.hostname
DATABASE_PORT = url.port

db = PostgresqlDatabase(DATABASE_NAME, user=DATABASE_USER, password=DATABASE_PASSWORD, host=DATABASE_HOST, port=DATABASE_PORT)

def initialize_db():
    try:
        print("Подключаемся к базе данных...")
        if not db.is_closed():
            db.close()
        db.connect()
        print("Подключение успешно.")
    except Exception as e:
        print(f"Ошибка при подключении к базе данных: {e}")

initialize_db()
