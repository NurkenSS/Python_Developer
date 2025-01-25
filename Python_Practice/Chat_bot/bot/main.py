import os
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import ParseMode
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.utils import executor

API_TOKEN = os.getenv("BOT_API_TOKEN")

logging.basicConfig(level=logging.INFO)

bot = Bot(token="7678163374:AAHy-xfKIXgZYqzzydzkearFYbq5Xzi9kO4")
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())

async def add_habit(message: types.Message):
    await message.answer("Добавьте свою привычку:")

async def edit_habit(message: types.Message):
    await message.answer("Редактируйте свою привычку:")

async def view_habits(message: types.Message):
    await message.answer("Вот все ваши привычки:")

dp.register_message_handler(add_habit, commands="add_habit")
dp.register_message_handler(edit_habit, commands="edit_habit")
dp.register_message_handler(view_habits, commands="view_habits")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
