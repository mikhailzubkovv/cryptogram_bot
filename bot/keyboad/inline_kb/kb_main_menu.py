from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

menu = [
    [
        InlineKeyboardButton(text='📈 Top expensive tokens', callback_data='top_expensive'),
        InlineKeyboardButton(text='📉 Top cheap tokens', callback_data='top_cheap')
    ],

    [InlineKeyboardButton(text='🆘 Help', callback_data='help')]
]

menu = InlineKeyboardMarkup(inline_keyboard=menu)
