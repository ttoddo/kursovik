from aiogram import Dispatcher
from aiogram.types import (KeyboardButton, Message, ReplyKeyboardMarkup,
                           ReplyKeyboardRemove)


btn_1 = KeyboardButton(text='Давай начнем')
btn_2 = KeyboardButton(text='Не стоит')
btn_3 = KeyboardButton(text='Хватит')

start_keyboard = ReplyKeyboardMarkup(
    keyboard=[[btn_1, btn_2]],
    resize_keyboard=True
)

stop_keyboard = ReplyKeyboardMarkup(
    keyboard=[[btn_3]],
    resize_keyboard=True
)
