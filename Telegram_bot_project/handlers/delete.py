from services.database import clear_history

async def delete_history(update, context):
    clear_history()
    await update.message.reply_text("История поиска очищена.")
