import os
from dotenv import load_dotenv, find_dotenv

if not find_dotenv():
    exit("Переменные окружения не загружены, т.к отсутствует файл .env")
else:
    load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
RAPID_API_KEY = os.getenv("RAPID_API_KEY")
RAPID_API_URL = "https://coinranking1.p.rapidapi.com/"

username_db = os.getenv("POSTGRES_USER")
password_db = os.getenv("POSTGRES_PASSWORD")
db_name = os.getenv("POSTGRES_DB")
