import asyncio
import datetime

from aiogram.types import ReplyKeyboardRemove, FSInputFile
from aiogram import Bot

from database.users_tasks_db import select_data
from utils.coinranking_api.get_coin_info.coin_info import coin_info_output
from utils.coinranking_api.path_n_clean import clean_tmp
from project_config.config import BOT_TOKEN


bot = Bot(BOT_TOKEN)


async def send_by_task() -> None:
    """
    Function uses to send info about coin to user at certain time

    :return: None
    """

    marker = {
        datetime.date.today().strftime('%d-%m-%y'): {}
    }
    while True:
        today = datetime.date.today().strftime('%d-%m-%y')
        if today not in marker:
            marker[today] = {}
        try:
            tasks = select_data()
            if tasks == {}:
                await asyncio.sleep(5)
            else:
                for task, value in tasks.items():
                    for user, sub_value in value.items():
                        repeat_time = sub_value['repeat_time']
                        coin_name = sub_value['coin_name']
                        time_period = sub_value['time_period']
                        cur_time = datetime.datetime.now().time()
                        time_format = cur_time.strftime('%H-%M')
                        if time_format == repeat_time and task not in marker[today]:
                            text, picture = coin_info_output(coin_name=coin_name.lower(), time_period=time_period)
                            picture = FSInputFile(picture)
                            await bot.send_photo(
                                chat_id=user,
                                photo=picture,
                                caption=f'You got this message because set task to bot\n'
                                        f'{text}',
                                reply_markup=ReplyKeyboardRemove()
                            )
                            clean_tmp()
                            marker[today][task] = True
                            await asyncio.sleep(1)
                    await asyncio.sleep(1)
        except Exception:
            await asyncio.sleep(1)


async def on_startup() -> None:
    """
    Create coroutine to start with bot

    :return: None
    """

    asyncio.create_task(coro=send_by_task())
