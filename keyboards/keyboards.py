from aiogram import Dispatcher
from aiogram.types import (KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove)
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
from aiogram.filters.callback_data import CallbackData


class ButtonsCallbackFactory(CallbackData, prefix='any'):
    status: str

menu_btn = InlineKeyboardButton(text='Выйти в главное менью',
                                    callback_data=ButtonsCallbackFactory(status='menu').pack())

kb_builderStart = ReplyKeyboardBuilder()
kb_builderReg = InlineKeyboardBuilder()
kb_builderSet = InlineKeyboardBuilder()
kb_builderMode = InlineKeyboardBuilder()

register_btn = InlineKeyboardButton(text='Зарегистрироваться',
                                    callback_data=ButtonsCallbackFactory(status='register').pack())

kb_builderReg.row(register_btn, width=2)
#клавиатура регистрации
register_keyboard: InlineKeyboardMarkup = kb_builderReg.as_markup(
    resize_keyboard=True,
    one_time_keyboard=True
)

start_btn1 = KeyboardButton(text='Давай')
start_btn2 = KeyboardButton(text='Не стоит')
start_btn3 = KeyboardButton(text='Настройки')
start_btn4 = KeyboardButton(text='Режим администратора')

kb_builderStart.row(start_btn1, start_btn2, width=2)
kb_builderStart.row(start_btn3, start_btn4, width=2)
#начальная клавиатура
start_keyboard: ReplyKeyboardMarkup = kb_builderStart.as_markup(
    resize_keyboard=True,
    one_time_keyboard=True
)

setting_btn1 = InlineKeyboardButton(text='Выбрать режим',
                                    callback_data=ButtonsCallbackFactory(status='change mode').pack())
setting_btn2 = InlineKeyboardButton(text='Задать модель поведения',
                                    callback_data=ButtonsCallbackFactory(status='give role').pack())


kb_builderSet.row(setting_btn1, setting_btn2, menu_btn, width=2)

#Клавиатура настроек
setting_keyboard: InlineKeyboardMarkup = kb_builderSet.as_markup(
    resize_keyboard=True,
    one_time_keyboard=True
)

choose_mode1 = InlineKeyboardButton(text='Анализ',
                                    callback_data=ButtonsCallbackFactory(status='analyze').pack())
choose_mode2 = InlineKeyboardButton(text='Генерация идей',
                                    callback_data=ButtonsCallbackFactory(status='genIdeas').pack())
choose_mode3 = InlineKeyboardButton(text='Мозговой штурм',
                                    callback_data=ButtonsCallbackFactory(status='brainStorm').pack())
choose_mode4 = InlineKeyboardButton(text='Просто чат',
                                    callback_data=ButtonsCallbackFactory(status='chat').pack())

kb_builderMode.row(choose_mode1, choose_mode2, width=2)
kb_builderMode.row(choose_mode3, choose_mode4,  width=2)
kb_builderMode.row(menu_btn,  width=1)
#Клавиатура выбора режима
choose_mode_keyboard: InlineKeyboardMarkup = kb_builderMode.as_markup(
    register_keyboard=True,
    one_time_keyboard=True
)

stop_btn = KeyboardButton(text='Прекратить')
stop_keyboard = ReplyKeyboardMarkup(
    keyboard=[[stop_btn]],
    resize_keyboard=True
)
