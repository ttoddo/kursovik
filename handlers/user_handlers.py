from aiogram import Router, F
from aiogram.filters import CommandStart, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state
from aiogram.types import CallbackQuery, Message

from FSM.fsm import Chat_mode, Admin
from config_data.config import config
from database.orm import check_user, insert_data, make_admin, select_user, check_user_admin, ban_user, unban_user
from keyboards.keyboards import register_keyboard, start_keyboard, ButtonsCallbackFactory, setting_keyboard, \
    admin_keyboard
from middlewares.middleware import BanCheckMiddleware

router = Router()
router.message.middleware(BanCheckMiddleware())


@router.message(CommandStart())
async def process_start_command(message: Message, state: FSMContext):
    if await check_user(message.from_user.id):
        await message.answer(text=f'Hello! User, {message.from_user.username}, с возвращением',
                             reply_markup=start_keyboard)
        if config.tg_bot.admin_id == message.from_user.id:
            await make_admin(message.from_user.id)
            await select_user(message.from_user.id)
            await message.answer(text='Вы админ! Привет владельцу')
    else:
        await message.answer(text=f'Привет, {message.from_user.username}, зарегистрируйтесь',
                             reply_markup=register_keyboard)
    await state.set_state(Chat_mode.chat)


@router.message(lambda message: message.text == 'Зарегистрироваться')
async def main_menu(message: Message):
    await insert_data(message.from_user.id, message.from_user.username)
    await message.answer(text='Вы успешно зарегистрировались!')
    await message.answer(text='Давайте начнем', reply_markup=start_keyboard)
    if message.from_user.id == 780374592:
        await make_admin(message.from_user.id)
        await message.answer(text='Вы админ! Привет владельцу')
    else: print('net')


@router.message(lambda message: message.text == 'Режим администратора')
async def admin_panel(message: Message):
    if await check_user(user_id=message.from_user.id):
        if await check_user_admin(user_id=message.from_user.id):
            await message.answer(text='Вы в панели администратора! Выберите действие', reply_markup=admin_keyboard)
            return
        else:
            await message.answer('Вы не админ!')
    else:
        await message.answer('Вас нет в базе!')


@router.callback_query(ButtonsCallbackFactory.filter(F.status == 'ban'))
async def main_menu(query: CallbackQuery, state: FSMContext):
    await query.message.answer(text='Введите id пользователя, которого хотите забанить', reply_markup=None)
    await state.set_state(Admin.ban)
    await query.message.delete()


@router.message(Admin.ban)
async def user_ban(message: Message, state: FSMContext):
    await ban_user(int(message.text))
    await message.answer(text='Пользователь успешно забанен')
    await state.set_state(Chat_mode.chat)



@router.callback_query(ButtonsCallbackFactory.filter(F.status == 'unban'))
async def main_menu(query: CallbackQuery, state: FSMContext):
    await query.message.answer(text='Введите id пользователя, которого хотите разбанить', reply_markup=None)
    await state.set_state(Admin.unban)
    await query.message.delete()


@router.message(Admin.unban)
async def user_unban(message: Message, state: FSMContext):
    await unban_user(int(message.text))
    await message.answer(text='Пользователь успешно разбанен')
    await state.set_state(Chat_mode.chat)


@router.callback_query(ButtonsCallbackFactory.filter(F.status == 'menu'))
async def main_menu(query: CallbackQuery):
    await query.message.answer(text='Возврат в меню', reply_markup=start_keyboard)
    await query.message.delete()


@router.message(lambda message: message.text == 'Не стоит')
async def begin_stop_command(message: Message):
    await message.answer(text='Если передумаете, можете просто нажать кнопочку',
                         reply_markup=start_keyboard)


@router.message(lambda message: message.text == 'Настройки')
async def begin_sett_command(message: Message):
    await message.answer(text='Вы перешли в настройки, выберите пункт: ',
                         reply_markup=setting_keyboard)

