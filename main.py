import logging
import asyncio
import sys

# There is an import handlers for messages here. Main code uses them despite being marked 'unused import'
from bot.handlers.default_handlers import start, help
from bot.handlers.custom_handlers import top_coins_cheap, top_coins_expensive, coin_info, history

from bot.loader.loader import start_bot
from project_config.config import BOT_TOKEN
from utils.coinranking_api.path_n_clean import create_tmp_folder


if __name__ == '__main__':
    create_tmp_folder()
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(start_bot(TOKEN=BOT_TOKEN))
    create_tmp_folder()
