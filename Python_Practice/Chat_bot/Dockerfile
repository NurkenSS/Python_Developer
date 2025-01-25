FROM python:3.10-buster

# Устанавливаем переменные окружения
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Устанавливаем рабочую директорию
WORKDIR /code

# Устанавливаем необходимые пакеты
RUN apt-get update && apt install -y python3-dev
RUN pip install --upgrade pip
RUN pip install poetry

# Копируем файл конфигурации poetry
ADD pyproject.toml .

# Настройки Poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-root --no-interaction --no-ansi

# Открываем порт
EXPOSE 8000

# Копируем все файлы проекта в контейнер
COPY . .
