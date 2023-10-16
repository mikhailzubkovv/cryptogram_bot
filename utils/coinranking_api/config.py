import os
from dotenv import load_dotenv, find_dotenv

if not find_dotenv():
    exit("Переменные окружения не загружены, т.к отсутствует файл .env")
else:
    load_dotenv()

RAPID_API_KEY = os.getenv("RAPID_API_KEY")
RAPID_API_URL = 'https://coinranking1.p.rapidapi.com/'
