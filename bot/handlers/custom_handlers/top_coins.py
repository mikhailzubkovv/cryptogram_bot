from aiogram.types import CallbackQuery
from aiogram import F

from bot.handlers.router_create import router
from utils.coinranking_api.get_all_coins.get_all_coins import print_to_user_top


@router.callback_query(F.data == 'top')
async def help_handler(callback: CallbackQuery) -> None:
    """

    """
    await callback.message.answer(print_to_user_top(user_top=5))
    await callback.answer()
