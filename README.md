A Telegram bot for check an information about coin through Coinranking API

U need to use the next keys to work with bot (file ".env.template"):
_TOKENS_:
    - BOT_TOKEN - your personal token for Telegram bot
    - RAPID_API_KEY - your personal token for RAPID-API.
    U can get it at https://rapidapi.com/Coinranking/api/coinranking1/
   

_Work with database_ (WARNING!!! all variables shouldn't be empty):
    - POSTGRES_USER - your username in PSQL system.
    - POSTGRES_PASSWORD - password for user in PSQL system
    - POSTGRES_DB - name of your database, should exist beefore connect to it

There is added 2 ways to run BOT:

1. Usual way by RUN command "python main.py" from project directory (directory should have name 
"python_basic_diploma". Also, you need to have installed Postgresql
2. Docker way by run command 'docker compose up -d' from project directory. To stop BOT use 'docker compose down'
