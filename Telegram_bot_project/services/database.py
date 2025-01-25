from peewee import PostgresqlDatabase, Model, CharField, IntegerField, DateTimeField
from datetime import datetime
import os
from urllib.parse import urlparse
from dotenv import load_dotenv


load_dotenv()

# Настройка подключения к базе данных
DATABASE_URL = os.getenv("DATABASE_URL")
db_url = urlparse(DATABASE_URL)

db = PostgresqlDatabase(
    database=db_url.path[1:],
    user=db_url.username,
    password=db_url.password,
    host=db_url.hostname,
    port=db_url.port
)

# Модель таблицы истории поисков
class MovieSearchHistory(Model):
    query = CharField()
    year = IntegerField(null=True)
    search_date = DateTimeField(default=datetime.now)

    class Meta:
        database = db

# Функция для создания таблиц
def create_tables():
    with db:
        db.create_tables([MovieSearchHistory])

# Сохранение поискового запроса
def save_search_history(query, year=None):
    try:
        MovieSearchHistory.create(query=query, year=year)
    except Exception as e:
        print(f"Ошибка при сохранении запроса: {e}")

# Очистка истории запросов
def clear_history():
    try:
        MovieSearchHistory.delete().execute()
    except Exception as e:
        print(f"Ошибка при очистке истории: {e}")

# Получение истории запросов
def get_search_history(limit=10):
    """
    Возвращает последние `limit` записей из базы данных в виде списка словарей.
    """
    history = (
        MovieSearchHistory.select()
        .order_by(MovieSearchHistory.search_date.desc())
        .limit(limit)
    )
    return [
        {
            "query": record.query,
            "year": record.year,  # NULL в базе данных будет возвращён как None
            "search_date": record.search_date,
        }
        for record in history
    ]