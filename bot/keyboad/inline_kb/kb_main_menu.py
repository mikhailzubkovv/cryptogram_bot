from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove

menu = [
    [InlineKeyboardButton(text='🆘 Помощь', callback_data='help')]
]

menu = InlineKeyboardMarkup(inline_keyboard=menu)
