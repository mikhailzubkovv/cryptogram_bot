from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove

menu = [
    [InlineKeyboardButton(text='🔝 Топ 10 самых дорогих токенов', callback_data='top')],
    [InlineKeyboardButton(text='🆘 Помощь', callback_data='help')]
]

menu = InlineKeyboardMarkup(inline_keyboard=menu)
