from aiogram.types import CallbackQuery, ReplyKeyboardRemove, Message
from aiogram import F
from aiogram.fsm.context import FSMContext


from bot.keyboad.inline_kb.kb_main_menu import menu_keyboard
from bot.handlers.router_create import router
from bot.keyboad.replay_kb.kb_period import period_keyboard
from bot.keyboad.replay_kb.task_choose import task_decision_keyboard
from bot.states.states import ManageTasks
from database.users_tasks_db import add_to_db, drop_from_db, select_data


@router.callback_query(F.data == 'manage_tasks')
async def manage_tasks_start(callback: CallbackQuery, state: FSMContext) -> None:
    """
    Handler for inline button with manage your tasks.

    :param callback: object CallbackQuery
    :param state: state for bot to determinate current position
    :return: None
    """
    await state.set_state(ManageTasks.task)
    await callback.message.answer(text='Choose action', reply_markup=task_decision_keyboard())
    await callback.answer()


# BLOCK ADD TASK TO DATABASE
@router.message(ManageTasks.task, F.text.in_(['Add a task']))
async def add_task_name(message: Message, state: FSMContext) -> None:
    """
    Handler for Reply keyboard to determine time period.

    :param message: object Message
    :param state: state for bot to determinate current position
    :return: None
    """
    await state.set_state(ManageTasks.coin_name)
    await message.answer(text='Type coin name (ex: "btc", "bitcoin")')


@router.message(ManageTasks.coin_name)
async def add_task_period(message: Message, state: FSMContext) -> None:
    """
    Handler for Reply keyboard to determine time period.

    :param message: object Message
    :param state: state for bot to determinate current position
    :return: None
    """
    await state.update_data(name=message.text)
    await state.set_state(ManageTasks.period)
    await message.answer(text='Choose time period to output', reply_markup=period_keyboard())


@router.message(
    ManageTasks.period,
    F.text.in_(['1h', '3h', '12h', '24h', '7d', '30d', '3m', '1y', '3y', '5y'])
)
async def add_task_handler(message: Message, state: FSMContext) -> None:
    """
    Handler for Reply keyboard to add task to DB.

    :param message: object Message
    :param state: state for bot to determinate current position
    :return: None
    """
    await state.update_data(period=message.text)
    data = await state.get_data()

    add_to_db(
        user_name=message.from_user.id,
        coin_name=data['name'],
        time_period=data['period'],
        repeat_time="12:00"
    )

    await message.answer(text=f"You've set the task!\nWhat do you like to do next?",
                         reply_markup=menu_keyboard())

    await state.clear()


# SHOW ALL TASKS IN DATABASE
@router.message(ManageTasks.task, F.text.in_(['Show all tasks']))
async def drop_task_handler(message: Message, state: FSMContext) -> None:
    """
    Handler for Reply keyboard to show all user's tasks.

    :param message: object Message
    :param state: state for bot to determinate current position
    :return: None
    """
    tasks = select_data(user_name=message.from_user.id)

    text = ''
    for task in tasks:
        text += (f'Task {task}:\n'
                 f"Get info about changes in {tasks[task]['coin_name'].upper()} for period {tasks[task]['time_period']}"
                 f" every {tasks[task]['repeat_time']}\n"
                 f"<--->\n")

    await message.answer(text=text, reply_markup=ReplyKeyboardRemove())
    await message.answer(text=f"What do you like to do next?",
                         reply_markup=menu_keyboard())
    await state.clear()


# DROP TASK IN DATABASE
@router.message(ManageTasks.task, F.text.in_(['Drop a task']))
async def drop_task_start(message: Message, state: FSMContext) -> None:
    """
    Handler for Reply keyboard to drop user's task: request ID position to drop.

    :param message: object Message
    :param state: state for bot to determinate current position
    :return: None
    """
    await state.set_state(ManageTasks.task_to_drop)
    await message.answer(text='Type task to drop (ex: 0 or 1 - U can see it by command "Show all tasks")')


@router.message(ManageTasks.task_to_drop)
async def drop_task_handler(message: Message, state: FSMContext) -> None:
    """
    Handler for Reply keyboard to drop user's task.

    :param message: object Message
    :param state: state for bot to determinate current position
    :return: None
    """

    drop_from_db(id_position=int(message.text), user_name=message.from_user.id)

    await message.answer(text=f"You dropped task {message.text}!\nWhat do you like to do next?",
                         reply_markup=menu_keyboard())
    await state.clear()
