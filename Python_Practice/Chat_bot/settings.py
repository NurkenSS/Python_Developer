import os
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_TOKEN = os.getenv("7678163374:AAHy-xfKIXgZYqzzydzkearFYbq5Xzi9kO4")

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///db.sqlite3")

DEBUG = os.getenv("DEBUG", "True").lower() == "true"

if DATABASE_URL.startswith("postgres"):
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.path.basename(DATABASE_URL),
            'USER': 'user',
            'PASSWORD': 'password',
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
