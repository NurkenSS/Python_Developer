from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

async def login(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    await update.message.reply_text(f'Привет, {user.first_name}! Ты успешно авторизован.')

def get_application(token: str) -> Application:
    return Application.builder().token(token).build()
