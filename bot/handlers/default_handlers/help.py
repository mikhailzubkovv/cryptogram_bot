from aiogram.types import CallbackQuery
from aiogram import F

from bot.handlers.router_create import router
from bot.keyboad.inline_kb.kb_main_menu import menu


@router.callback_query(F.data == 'help')
async def help_handler(callback: CallbackQuery) -> None:
    """
    Send information about bot to user
    """
    await callback.message.answer(
        f"Hello, {callback.from_user.full_name}!✋\n"
        f"I'm Cryptogram bot. I can provide you an information about crypto.\n"
        f"Start command: /start\n"
        f"\n"
        f"So, you can ask me to do next activity:\n"
        f"  📈 Top expensive tokens - output information about the most expensive tokens\n"
        f"  📉 Top cheap tokens - output information about the cheapest tokens\n"
        f"Choose mode and follow bot's hits to get information\n"
        f"\n"
        f"  🔎 Choose coin - output information about user's inputted token's name\n"
        f"You should input token's name shortly like 'btc' or fully 'bitcoin'\n"
        f"\n"
        f"🔑Abbreviations: h - hour, d - day, m - month, y - year\n"
        f"\n"
        f"  💾 History - output last 10 user's requests\n"
    )
    await callback.message.answer(text=f"What do you like to do next?",
                                  reply_markup=menu)
    await callback.answer()

