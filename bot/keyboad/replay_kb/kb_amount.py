from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


def amount_keyboard() -> ReplyKeyboardMarkup:
    amount = [
        [
            KeyboardButton(text="1"),
            KeyboardButton(text="2"),
            KeyboardButton(text="3"),
        ],
        [
            KeyboardButton(text="4"),
            KeyboardButton(text="5"),
            KeyboardButton(text="6")
        ],
        [
            KeyboardButton(text="7"),
            KeyboardButton(text="8"),
            KeyboardButton(text="9"),
        ],
        [KeyboardButton(text="10")],
    ]

    return ReplyKeyboardMarkup(
        keyboard=amount,
        resize_keyboard=True,
        input_field_placeholder="Choose amount tokens to output",
    )
