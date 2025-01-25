import logging
from services.omdb_api import search_movie
from services.database import save_search_history

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def search_command(update, context):
    await update.message.reply_text("Введите название фильма для поиска.")

async def search_year_command(update, context):
    await update.message.reply_text("Введите название фильма и год для поиска (например: The Matrix 1999).")

async def handle_message(update, context):
    user_message = update.message.text.strip()

    query_parts = user_message.split(" ")
    year = None
    if len(query_parts) > 1 and query_parts[-1].isdigit():
        query = " ".join(query_parts[:-1])
        year = query_parts[-1]
    else:
        query = user_message

    movie_data = search_movie(query, year)

    if movie_data:
        sent_posters = set() 
        for movie in movie_data:
            movie_title = movie.get('Title')
            movie_year = movie.get('Year')
            imdb_id = movie.get('imdbID')
            imdb_url = f"https://www.imdb.com/title/{imdb_id}/"
            movie_poster = movie.get('Poster')  
            movie_plot = movie.get('Plot') 

            logger.info(f"Ответ от API для {movie_title}: {movie}")

            movie_reply = f"<b>{movie_title} ({movie_year})</b>\n" 
            movie_reply += f"Ссылка на фильм: <a href='{imdb_url}'>IMDb</a>"

            if movie_plot:
                movie_reply += f"\n<i>Описание:</i> {movie_plot}"
            else:
                movie_reply += "\n<i>Описание недоступно.</i>"

            await update.message.reply_text(movie_reply, parse_mode='HTML')


        save_search_history(query, year)  
    else:
        await update.message.reply_text(f"Фильмы с названием '{query}' не найдены.")