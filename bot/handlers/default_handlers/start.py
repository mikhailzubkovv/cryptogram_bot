from aiogram.filters import Command
from aiogram.types import Message
from aiogram.utils.markdown import hbold
import datetime

import bot.keyboad.inline_kb.kb_main_menu
from bot.handlers.router_create import router

from utils.coinranking_api.get_coin_info.create_coins_db import create_coins_db


@router.message(Command('start'))
async def command_start_handler(message: Message) -> None:
    """
    This handler receives messages with `/start` command
    """
    await message.answer(text=f"Hello, {hbold(message.from_user.full_name)}! "
                              f"What do you like to do? Just choose below and follow the hints ⏬",
                         reply_markup=bot.keyboad.inline_kb.kb_main_menu.menu)
    today = datetime.date.today()
    day = int(today.strftime('%d'))
    if day in (1, 5, 10, 15, 20, 25, 30):
        create_coins_db()
