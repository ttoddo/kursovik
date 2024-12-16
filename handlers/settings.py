from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from FSM.fsm import Chat_mode, Take_role
from keyboards.keyboards import start_keyboard, ButtonsCallbackFactory, choose_mode_keyboard

router = Router()


@router.callback_query(ButtonsCallbackFactory.filter(F.status == 'change mode'))
async def mode_menu(query: CallbackQuery):
    await query.message.answer(text='Выберите режим, в котором будет работать бот: ', reply_markup=choose_mode_keyboard)
    await query.message.delete()


@router.callback_query(ButtonsCallbackFactory.filter(F.status == 'give role'))
async def set_role(query: CallbackQuery, state: FSMContext):
    await query.message.answer(text='Задайте роль боту(пишите развернуто иначе нейросеть не захочет её принимать): ',
                               reply_markup=start_keyboard)
    await query.message.delete()
    await state.set_state(Take_role.take_role)


@router.callback_query(ButtonsCallbackFactory.filter(F.status == 'analyze'))
async def analyze_mode(query: CallbackQuery, state: FSMContext):
    await state.set_state(Chat_mode.analyze)
    await query.message.answer(text='Выбран режим анализа! Возврат в меню ', reply_markup=start_keyboard)
    await query.message.delete()


@router.callback_query(ButtonsCallbackFactory.filter(F.status == 'brainStorm'))
async def analyze_mode(query: CallbackQuery, state: FSMContext):
    await state.set_state(Chat_mode.brainStorm)
    await query.message.answer(text='Выбран режим мозгового штурма! Возврат в меню ', reply_markup=start_keyboard)
    await query.message.delete()


@router.callback_query(ButtonsCallbackFactory.filter(F.status == 'genIdeas'))
async def analyze_mode(query: CallbackQuery, state: FSMContext):
    await state.set_state(Chat_mode.generate)
    await query.message.answer(text='Выбран режим генерации идей! Возврат в меню ', reply_markup=start_keyboard)
    await query.message.delete()


@router.callback_query(ButtonsCallbackFactory.filter(F.status == 'chat'))
async def chat_mode(query: CallbackQuery, state: FSMContext):
    await state.set_state(Chat_mode.chat)
    await query.message.answer(text='Выбран режим общения! Возврат в меню ', reply_markup=start_keyboard)
    await query.message.delete()
