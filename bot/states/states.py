from aiogram.fsm.state import StatesGroup, State


class TopExpensive(StatesGroup):
    period = State()
    amount = State()


class TopCheap(StatesGroup):
    period = State()
    amount = State()


class CoinInfo(StatesGroup):
    coin_name = State()
    period = State()
