from aiogram.types import CallbackQuery, FSInputFile
from aiogram import F

from bot.handlers.router_create import router
from database.user_history_db import main_user_history
from bot.keyboad.inline_kb.kb_main_menu import menu_keyboard
from utils.coinranking_api.path_n_clean import clean_tmp


@router.callback_query(F.data == 'history')
async def history(callback: CallbackQuery) -> None:
    """
    Handler for inline button with user history.

    :param callback: object CallbackQuery
    :return: None
    """

    data = main_user_history(user_name=callback.from_user.id)
    picture = FSInputFile(data)
    await callback.message.answer_photo(
        photo=picture,
        caption='Your last 10 requests'
    )
    await callback.answer()

    await callback.message.answer(text=f"What do you like to do next?",
                                  reply_markup=menu_keyboard())
    clean_tmp()
