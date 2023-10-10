from aiogram.types import Message, CallbackQuery
from aiogram import F

from bot.handlers.router_create import router


@router.callback_query(F.data == 'help')
async def help_handler(clbck: CallbackQuery) -> None:
    """

    """
    await clbck.message.answer('Help is HERE')
