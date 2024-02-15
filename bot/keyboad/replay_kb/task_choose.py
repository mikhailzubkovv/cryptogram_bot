from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


def task_decision_keyboard() -> ReplyKeyboardMarkup:
    decision = [
        [KeyboardButton(text="Add a task"), KeyboardButton(text="Drop a task")],
        [KeyboardButton(text="Show all tasks")],
    ]

    return ReplyKeyboardMarkup(
        keyboard=decision,
        resize_keyboard=True,
        input_field_placeholder="What would you like to do with tasks?",
    )
