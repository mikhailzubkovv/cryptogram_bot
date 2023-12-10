import datetime

import bot.keyboad.inline_kb.kb_main_menu
from aiogram.types import CallbackQuery, Message
from aiogram import F

from bot.handlers.router_create import router
from database.user_history_db import select_data, add_to_db


@router.callback_query(F.data == 'history')
async def history(callback: CallbackQuery) -> None:
    """
    Handler for inline button with user history.

    :param callback: object CallbackQuery
    :return: None
    """

    data = select_data(user_name=callback.from_user.id)
    await callback.message.answer(text=data)
    await callback.answer()

    await callback.message.answer(text=f"What do you like to do next?",
                                  reply_markup=bot.keyboad.inline_kb.kb_main_menu.menu)
