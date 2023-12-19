from aiogram.fsm.state import StatesGroup, State


class TopExpensive(StatesGroup):
    """
    States for Top Expensive handler
    """
    period = State()
    amount = State()


class TopCheap(StatesGroup):
    """
    States for Top Cheap handler
    """
    period = State()
    amount = State()


class CoinInfo(StatesGroup):
    """
    States for Coin Info handler
    """
    coin_name = State()
    period = State()
