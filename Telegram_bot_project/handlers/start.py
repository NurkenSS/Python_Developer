async def start(update, context):
    await update.message.reply_text(
        "Привет! Я бот для поиска фильмов. Доступные команды:\n"
        "/search - Найти фильм\n"
        "/search_year - Найти фильм по году\n"
        "/history - Посмотреть историю поиска\n"
        "/delete - Очистить историю поиска"
    )
