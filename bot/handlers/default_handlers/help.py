from aiogram.types import CallbackQuery
from aiogram import F

from bot.handlers.router_create import router


@router.callback_query(F.data == 'help')
async def help_handler(callback: CallbackQuery) -> None:
    """

    """
    await callback.message.answer('Help is HERE')
    await callback.answer()
