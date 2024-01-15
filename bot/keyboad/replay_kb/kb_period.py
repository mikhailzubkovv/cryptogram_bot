from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


def period_keyboard() -> ReplyKeyboardMarkup:
    period = [
        [
            KeyboardButton(text='1h'),
            KeyboardButton(text='3h'),
            KeyboardButton(text='12h'),
            KeyboardButton(text='24h')
        ],

        [
            KeyboardButton(text='7d'),
            KeyboardButton(text='30d'),
            KeyboardButton(text='3m')
        ],

        [
            KeyboardButton(text='1y'),
            KeyboardButton(text='3y'),
            KeyboardButton(text='5y'),
        ]
    ]

    return ReplyKeyboardMarkup(
        keyboard=period,
        resize_keyboard=True,
        input_field_placeholder='Choose the time period to observe'
    )


def data_period() -> dict:
    period = {
        '1h': '1 hour',
        '3h': '3 hours',
        '12h': '12 hours',
        '24h': '24 hours',
        '7d': '7 days',
        '30d': '30 days',
        '3m': '3 months',
        '1y': '1 year',
        '3y': '3 years',
        '5y': '5 years'
    }
    return period
