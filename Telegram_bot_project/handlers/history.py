from services.database import get_search_history

async def view_history(update, context):
    """
    Отображает историю запросов из базы данных. Если год отсутствует, он не отображается.
    """
    history = get_search_history()

    if history:
        response = "\n".join([
            f"{idx + 1}. {item['query']}{(' (' + str(item['year']) + ')') if item['year'] else ''} - "
            f"{item['search_date'].strftime('%Y-%m-%d %H:%M:%S')}"
            for idx, item in enumerate(history)
        ])
    else:
        response = "История запросов пуста."

    await update.message.reply_text(response)
    