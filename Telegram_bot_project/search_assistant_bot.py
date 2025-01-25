import logging
from telegram.ext import Application, CommandHandler, MessageHandler, filters
from handlers.start import start
from handlers.search import search_command, search_year_command, handle_message 
from handlers.delete import delete_history
from handlers.history import view_history
from services.database import create_tables
from dotenv import load_dotenv
import os

load_dotenv()

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)

BOT_TOKEN = os.getenv("BOT_TOKEN")

def main():
    create_tables()

    application = Application.builder().token(BOT_TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("search", search_command))
    application.add_handler(CommandHandler("search_year", search_year_command))
    application.add_handler(CommandHandler("delete", delete_history))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    application.add_handler(CommandHandler("history", view_history))

    logger.info("Бот запущен...")
    application.run_polling()

if __name__ == "__main__":
    main()
