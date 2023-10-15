from aiogram.filters import Command
from aiogram.types import Message
from aiogram.utils.markdown import hbold

import bot.keyboad.inline_kb.kb_main_menu
from bot.handlers.router_create import router


@router.message(Command('start'))
async def command_start_handler(message: Message) -> None:
    """
    This handler receives messages with `/start` command
    """
    await message.answer(f"Hello, {hbold(message.from_user.full_name)}!", reply_markup=bot.keyboad.inline_kb.kb_main_menu.menu)
