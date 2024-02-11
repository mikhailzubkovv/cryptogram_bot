import datetime

from aiogram.types import CallbackQuery, ReplyKeyboardRemove, Message
from aiogram import F, html, Router
from aiogram.fsm.context import FSMContext

from bot.keyboad.replay_kb.kb_period import period_keyboard, data_period
from bot.keyboad.replay_kb.kb_amount import amount_keyboard
from bot.keyboad.inline_kb.kb_main_menu import menu_keyboard
from utils.coinranking_api.get_all_coins.get_all_coins import get_coins
from bot.states.states import TopCheap
from database.user_history_db import add_to_db

router = Router()


@router.callback_query(F.data == 'top_cheap')
async def top_coins_start(callback: CallbackQuery, state: FSMContext) -> None:
    """
    Handler for inline button with top tokens.

    :param callback: object CallbackQuery
    :param state: state for bot to determinate current position
    :return: None
    """
    await state.set_state(TopCheap.period)
    await callback.message.answer(text='Choose time period', reply_markup=period_keyboard())
    await callback.answer()


@router.message(
    TopCheap.period,
    F.text.in_(['1h', '3h', '12h', '24h', '7d', '30d', '3m', '1y', '3y', '5y'])
)
async def top_coins_period(message: Message, state: FSMContext) -> None:
    """
    Handler for Reply keyboard to determine time period.

    :param message: object Message
    :param state: state for bot to determinate current position
    :return: None
    """
    await state.update_data(period=message.text)
    await state.set_state(TopCheap.amount)
    await message.answer(text='Choose amount of output', reply_markup=amount_keyboard())


@router.message(
    TopCheap.amount,
    F.text.in_(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'])
)
async def top_coins_output(message: Message, state: FSMContext) -> None:
    """
    Handler for Reply keyboard to determine output amount.

    :param message: object Message
    :param state: state for bot to determinate current position
    :return: None
    """
    data = await state.get_data()
    add_to_db(
        user_name=message.from_user.id,
        module='top_coins_cheap',
        coin_name='EMPTY',
        time_period=data['period'],
        amount_output=message.text,
        update_date=str(datetime.datetime.now().strftime('%Y-%b-%d %H:%M:%S'))
    )

    await message.answer(
        text=f"⏳ Period: {html.bold(data_period()[data['period']])} "
             f"⚡Top: {html.bold(message.text)}\n"
             f"{get_coins(timePeriod=data['period'], orderDirection='asc', limit='10', user_top=int(message.text))}",
        parse_mode='HTML',
        reply_markup=ReplyKeyboardRemove()
    )

    await message.answer(text=f"What do you like to do next?",
                         reply_markup=menu_keyboard())

    await state.clear()
