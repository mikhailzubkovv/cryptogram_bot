from aiogram.types import CallbackQuery, ReplyKeyboardRemove, Message, FSInputFile
from aiogram import F
from aiogram.fsm.context import FSMContext

import datetime
from bot.keyboad.inline_kb.kb_main_menu import menu_keybord
from bot.handlers.router_create import router
from bot.keyboad.replay_kb.kb_period import period_keyboard
from utils.coinranking_api.get_coin_info.coin_info import coin_info_output
from bot.states.states import CoinInfo
from database.user_history_db import add_to_db


@router.callback_query(F.data == 'coin_info')
async def coin_info_start(callback: CallbackQuery, state: FSMContext) -> None:
    """
    Handler for inline button with coin info.

    :param callback: object CallbackQuery
    :param state: state for bot to determinate current position
    :return: None
    """
    await state.set_state(CoinInfo.coin_name)
    await callback.message.answer(text='Type coin name (ex: "btc", "bitcoin")')
    await callback.answer()


@router.message(CoinInfo.coin_name)
async def coin_info_period(message: Message, state: FSMContext) -> None:
    """
    Handler for Reply keyboard to determine time period.

    :param message: object Message
    :param state: state for bot to determinate current position
    :return: None
    """
    await state.update_data(name=message.text)
    await state.set_state(CoinInfo.period)
    await message.answer(text='Choose time period to output', reply_markup=period_keyboard())


@router.message(
    CoinInfo.period,
    F.text.in_(['1h', '3h', '12h', '24h', '7d', '30d', '3m', '1y', '3y', '5y'])
)
async def coin_info(message: Message, state: FSMContext) -> None:
    """
    Handler for Reply keyboard to determine output info.

    :param message: object Message
    :param state: state for bot to determinate current position
    :return: None
    """
    await state.update_data(period=message.text)
    data = await state.get_data()

    add_to_db(
        user_name=message.from_user.id,
        module='coin_info',
        coin_name=data['name'],
        time_period=data['period'],
        amount_output='EMPTY',
        update_date=str(datetime.datetime.now().strftime('%Y-%b-%d %H:%M:%S'))
    )

    text, picture = coin_info_output(coin_name=data['name'].lower(), time_period=message.text)
    picture = FSInputFile(picture)
    await message.answer_photo(
        photo=picture,
        caption=text,
        reply_markup=ReplyKeyboardRemove()
    )
    await message.answer(text=f"What do you like to do next?",
                         reply_markup=menu_keybord())

    await state.clear()
