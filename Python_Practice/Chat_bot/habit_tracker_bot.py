import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

logging.basicConfig(level=logging.INFO)

TELEGRAM_TOKEN = "7678163374:AAHy-xfKIXgZYqzzydzkearFYbq5Xzi9kO4"

user_goals = {}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logging.info("Start command received")
    await update.message.reply_text(
        "Привет! Я ваш бот для отслеживания привычек. Введите команду для начала.\n"
        "/setgoal - Установить цель\n"
        "/remind - Напомнить о задаче\n"
        "/status - Показать текущий статус\n"
        "/help - Показать список команд"
    )

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logging.info("Received /help command")
    await update.message.reply_text(
        "Вот список доступных команд:\n"
        "/start - Начать работу с ботом\n"
        "/setgoal - Установить цель\n"
        "/remind - Напомнить о задаче\n"
        "/status - Показать текущий статус\n"
        "/reset - Сбросить цель\n"
        "/remove - Удалить цель\n"
        "/help - Показать список команд"
    )

async def set_goal(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logging.info(f"Received /setgoal command from user {update.message.chat_id}")

    await update.message.reply_text("Пожалуйста, укажите вашу цель:")

    context.user_data['awaiting_goal'] = True

async def receive_goal(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if context.user_data.get('awaiting_goal'):
        goal = update.message.text
        user_goals[update.message.chat_id] = goal
        context.user_data['awaiting_goal'] = False
        await update.message.reply_text(f"Ваша цель установлена: {goal}")
    else:
        await update.message.reply_text("Для установки цели используйте команду /setgoal.")

async def remind(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logging.info("Received /remind command")
    if update.message.chat_id in user_goals:
        goal = user_goals[update.message.chat_id]
        await update.message.reply_text(f"Напоминаю вам о задаче: {goal}")
    else:
        await update.message.reply_text("Цель не установлена. Пожалуйста, установите цель с помощью команды /setgoal.")

async def status(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logging.info("Received /status command")
    if update.message.chat_id in user_goals:
        goal = user_goals[update.message.chat_id]
        await update.message.reply_text(f"Ваш текущий статус: Цель - {goal}")
    else:
        await update.message.reply_text("Ваш текущий статус: Цель не установлена.")

async def reset(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logging.info("Received /reset command")
    if update.message.chat_id in user_goals:
        del user_goals[update.message.chat_id]
        await update.message.reply_text("Ваша цель была сброшена.")
    else:
        await update.message.reply_text("Цель не установлена.")

async def remove_goal(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logging.info("Received /remove command")
    if update.message.chat_id in user_goals:
        del user_goals[update.message.chat_id]
        await update.message.reply_text("Цель была удалена.")
    else:
        await update.message.reply_text("Цель не установлена.")

def main() -> None:
    application = Application.builder().token(TELEGRAM_TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("setgoal", set_goal))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, receive_goal))
    application.add_handler(CommandHandler("remind", remind))
    application.add_handler(CommandHandler("status", status))
    application.add_handler(CommandHandler("help", help))
    application.add_handler(CommandHandler("reset", reset))
    application.add_handler(CommandHandler("remove", remove_goal))

    logging.info("Bot started...")
    application.run_polling()

if __name__ == "__main__":
    main()
