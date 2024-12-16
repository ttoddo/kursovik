from aiogram import Router
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from FSM.fsm import Take_role, Chat_mode
from keyboards.keyboards import start_keyboard
router = Router()
botRole = ''


@router.message(StateFilter(Take_role.take_role))
async def take_role(message: Message, state: FSMContext):
    global botRole
    botRole = message.text
    await message.answer("Роль успешно задана, возвращаемся в меню!", reply_markup=start_keyboard)
    await state.set_state(Chat_mode.chat)
    await message.answer(text='Чат-мод сброшен на режим общения, задайте его в настройках, если хотите изменить')