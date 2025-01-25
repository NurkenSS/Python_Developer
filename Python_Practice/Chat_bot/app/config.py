import os

class Config:
    TELEGRAM_TOKEN = os.getenv('7678163374:AAHy-xfKIXgZYqzzydzkearFYbq5Xzi9kO4')
    DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://nurken:your_password@localhost/chat_bot_db")
    REMINDER_TIME = os.getenv('REMINDER_TIME', '08:00')  
    LOGGING_DIR = os.getenv('LOGGING_DIR', 'logs')
    GOAL_NOTIFICATION_TIME = os.getenv('GOAL_NOTIFICATION_TIME', '09:00')
    GOAL_PROGRESS_THRESHOLD = os.getenv('GOAL_PROGRESS_THRESHOLD', 50)
    API_KEY = os.getenv('API_KEY', 'your-api-key-here')

from dotenv import load_dotenv
load_dotenv()
