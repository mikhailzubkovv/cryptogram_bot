from aiogram import Bot, Dispatcher, Router
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.utils.chat_action import ChatActionMiddleware

from bot.handlers.default_handlers import start, help, echo
from bot.handlers.custom_handlers import (
    top_coins_cheap,
    top_coins_expensive,
    coin_info,
    history,
    manage_tasks,
)
from utils.coinranking_api.users_task_reminder.users_task_reminder import on_startup

router = Router()


async def start_bot(TOKEN: str) -> None:
    """
    Initialize Bot instance with a default parse mode which will be passed to all API calls

    :param TOKEN: token to get access to Telegram
    :return: None
    """
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    dp = Dispatcher(storage=MemoryStorage())
    dp.include_routers(
        router,
        start.router,
        help.router,
        # echo.router,
        coin_info.router,
        history.router,
        top_coins_expensive.router,
        top_coins_cheap.router,
        manage_tasks.router,
    )

    dp.startup.register(callback=on_startup)
    dp.message.middleware(ChatActionMiddleware())
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == "__main__":
    pass
