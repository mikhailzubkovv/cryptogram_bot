from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def menu_keybord() -> InlineKeyboardMarkup:
    menu = [
        [
            InlineKeyboardButton(text='📈 Top expensive tokens', callback_data='top_expensive'),
            InlineKeyboardButton(text='📉 Top cheap tokens', callback_data='top_cheap')
        ],

        [InlineKeyboardButton(text='🔎 Choose coin', callback_data='coin_info')],

        [
            InlineKeyboardButton(text='💾 History', callback_data='history'),
            InlineKeyboardButton(text='🆘 Help', callback_data='help'),
        ]
    ]
    return InlineKeyboardMarkup(inline_keyboard=menu)
