from aiogram.filters import Command
from aiogram.types import Message
from aiogram.utils.markdown import hbold
from aiogram import Router

from bot.keyboad.inline_kb.kb_main_menu import menu_keyboard

from utils.coinranking_api.get_coin_info.create_coins_db import create_coins_db

router = Router()


@router.message(Command("start"))
async def command_start_handler(message: Message) -> None:
    """
    This handler receives messages with `/start` command
    """
    await message.answer(
        text=f"Hello, {hbold(message.from_user.full_name)}! "
        f"What do you like to do? Just choose below and follow the hints ⏬",
        reply_markup=menu_keyboard(),
    )
    create_coins_db()
