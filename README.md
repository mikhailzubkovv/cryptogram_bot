A Telegram bot for check an information about coin through Coinranking API
*for correct app working, you need to use Postgresql 

U need to use the next keys to work with bot (file ".env.template"):
    _TOKENS_:
    - BOT_TOKEN - your personal token for Telegram bot
    - RAPID_API_KEY - your personal token for RAPID-API.
    U can get it at https://rapidapi.com/Coinranking/api/coinranking1/

    _Work with database_ (WARNING!!! all variables shouldn't be empty):
    - username_db - your username in PSQL system.
    - password_db - password for user in PSQL system
    - host_db - host to connect to PSQL Server where is your database located (local 127.0.0.1)
    - port_db - port for your host (local 5432)
    - db_name - name of your database, should exist beefore connect to it
