import os
from dotenv import load_dotenv, find_dotenv

if not find_dotenv():
    exit("Переменные окружения не загружены, т.к отсутствует файл .env")
else:
    load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
RAPID_API_KEY = os.getenv("RAPID_API_KEY")
RAPID_API_URL = 'https://coinranking1.p.rapidapi.com/'

username_db = os.getenv("username_db")
password_db = os.getenv("password_db")
host_db = os.getenv("host_db")
port_db = os.getenv('port_db')
db_name = os.getenv('db_name')