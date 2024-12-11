from aiogram import Dispatcher
from aiogram.types import (KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove)
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
from aiogram.filters.callback_data import CallbackData


class ButtonsCallbackFactory(CallbackData, prefix='any'):
    status: str


kb_builderRep = ReplyKeyboardBuilder()
kb_builderInl = InlineKeyboardBuilder()

register_btn = InlineKeyboardButton(text='Зарегистрироваться', callback_data=ButtonsCallbackFactory(status='register').pack())

kb_builderInl.row(register_btn, width=2)
#клавиатура регистрации
register_keyboard: InlineKeyboardMarkup = kb_builderInl.as_markup(
    resize_keyboard=True,
    one_time_keyboard=True
)

start_btn1 = KeyboardButton(text='Давай')
start_btn2 = KeyboardButton(text='Не стоит')
start_btn3 = KeyboardButton(text='Настройки')
start_btn4 = KeyboardButton(text='Режим администратора')

kb_builderRep.row(start_btn1, start_btn2, width=2)
kb_builderRep.row(start_btn3, start_btn4, width=2)
#начальная клавиатура
start_keyboard: ReplyKeyboardMarkup = kb_builderRep.as_markup(
    resize_keyboard=True,
    one_time_keyboard=True
)

setting_btn1 = InlineKeyboardButton(text='Выбрать режим', callback_data='change mode of prompts')
setting_btn2 = InlineKeyboardButton(text='Задать модель поведения', callback_data='give a role model')
setting_btn3 = InlineKeyboardButton(text='')

kb_builderInl.row(setting_btn1, setting_btn2, setting_btn3, width=2)

#Клавиатура настроек
setting_keyboard = InlineKeyboardButton = kb_builderInl.as_markup(
    resize_keyboard=True,
    one_time_keyboard=True
)

choose_mode1 = KeyboardButton(text='Анализ', callback_data='analyze')
choose_mode2 = KeyboardButton(text='Генерация идей', callback_data='genIdeas')
choose_mode3 = KeyboardButton(text='Мозговой штурм', callback_data='brainStorm')
choose_mode4 = KeyboardButton(text='Просто чат', callback_data='chat')

kb_builderRep.row(choose_mode1, choose_mode2, width=2)
kb_builderRep.row(choose_mode3, choose_mode4, width=2)
#Клавиатура выбора режима
choose_mode_keyboard = ReplyKeyboardMarkup = kb_builderRep.as_markup(
    register_keyboard=True,
    one_time_keyboard=True
)

stop_btn = KeyboardButton(text='Прекратить')
stop_keyboard = ReplyKeyboardMarkup(
    keyboard=[[stop_btn]],
    resize_keyboard=True
)
