import os

from dotenv import load_dotenv

load_dotenv()

DEBUG = 10

API_TOKEN = str(os.environ.get("API_TOKEN"))
GPT_TOKEN = str(os.environ.get("GPT_TOKEN"))
IP = str(os.getenv('IP'))
POSTGRES_USER = str(os.getenv('POSTGRES_USER'))
POSTGRES_PASSWORD = str(os.getenv('POSTGRES_PASSWORD'))
DATABASE = str(os.getenv('DATABASE'))
POSTGRES_URL = f'postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{IP}/{DATABASE}'

ADMINS = [
    int(os.getenv('MY_TELEGRAM_ID'))
]
