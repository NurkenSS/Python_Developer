import requests
import os
from dotenv import load_dotenv

# Загружаем переменные окружения
load_dotenv()
OMDB_API_KEY = os.getenv("OMDB_API_KEY")
BASE_URL = os.getenv("BASE_URL")

def search_movie(query, year=None):
    try:
        params = {"s": query, "apikey": OMDB_API_KEY}
        if year:
            params["y"] = year

        response = requests.get(BASE_URL, params=params)
        response.raise_for_status() 

        print(f"Response from OMDB: {response.text}")  

        data = response.json()

        if data.get("Response") == "True":
            return data["Search"]
        else:
            print("No films found or invalid query.")
            return []  
        
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при запросе к OMDB: {e}")
        return []
