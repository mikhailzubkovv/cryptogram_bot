from aiogram.fsm.state import StatesGroup, State


class TopExpensive(StatesGroup):
    """
    States for Top Expensive handler

    Attributes
        period: str - state gets period of analyze
        amount: str - sate gets amount of output
    """
    period = State()
    amount = State()


class TopCheap(StatesGroup):
    """
    States for Top Cheap handler

    Attributes
        period: str - state gets period of analyze
        amount: str - sate gets amount of output
    """
    period = State()
    amount = State()


class CoinInfo(StatesGroup):
    """
    States for Coin Info handler

    Attributes
        coin_name - state gets coin name
        period - state gets period of analyze
    """
    coin_name = State()
    period = State()


class ManageTasks(StatesGroup):
    """
    States for Manage Tasks handler

    Attributes
        task - state for set task
        coin_name - state gets coin name
        period - state gets period of analyze
        task_to_drop - state to determine task to drop
    """
    task = State()
    coin_name = State()
    period = State()
    task_to_drop = State()
