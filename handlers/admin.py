from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message

from FSM.fsm import Chat_mode, Admin
from database.orm import check_user, check_user_admin, ban_user, unban_user
from keyboards.keyboards import ButtonsCallbackFactory, admin_keyboard


router = Router()


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

