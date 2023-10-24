import logging
import asyncio
import sys

# There is an import handlers for messages here. Main code uses them despite being marked 'unused import'
from bot.handlers.default_handlers import start, help
from bot.handlers.custom_handlers import top_coins_cheap, top_coins_expensive

from bot.loader.loader import start_bot
from bot.config_data.config import BOT_TOKEN


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(start_bot(TOKEN=BOT_TOKEN))
