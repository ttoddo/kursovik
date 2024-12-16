from aiogram import Router, F
from aiogram.filters import CommandStart, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state
from aiogram.types import CallbackQuery, Message
from langchain_core.messages import HumanMessage

from FSM.fsm import Chat_mode, Admin, GenerateState, MessageState, AnalyzeState, BrainStormState
from config_data.config import config
from database.orm import check_user, insert_data, make_admin, select_user, check_user_admin, ban_user, unban_user
from gigachat_data.gigaChat import send_message
from handlers.bot_role import botRole
from keyboards.keyboards import register_keyboard, start_keyboard, ButtonsCallbackFactory, setting_keyboard, \
    admin_keyboard, stop_keyboard

router = Router()


@router.message(lambda message: message.text == 'Давай', StateFilter(Chat_mode.analyze))
async def begin_chatting_command(message: Message, state: FSMContext):
    await message.answer(text='Вы в режиме анализа! Для остановки напишите/нажмите кнопку хватит',
                         reply_markup=stop_keyboard)
    await state.set_state(AnalyzeState.chatting)
    # state.update_data('currState':)


@router.message(lambda message: message.text == 'Давай', StateFilter(Chat_mode.brainStorm))
async def begin_chatting_command(message: Message, state: FSMContext):
    await message.answer(text='Вы в режиме мозгового штурма! Для остановки напишите/нажмите кнопку хватит',
                         reply_markup=stop_keyboard)
    await state.set_state(BrainStormState.chatting)


@router.message(lambda message: message.text == 'Давай', StateFilter(Chat_mode.generate))
async def begin_chatting_command(message: Message, state: FSMContext):
    await message.answer(text='Вы в режиме генерации идей! Для остановки напишите/нажмите кнопку хватит',
                         reply_markup=stop_keyboard)
    await state.set_state(GenerateState.chatting)


@router.message(lambda message: message.text == 'Давай', StateFilter(Chat_mode.chat))
async def begin_chatting_command(message: Message, state: FSMContext):
    await message.answer(text='Вы в режиме общения! Для остановки напишите/нажмите кнопку хватит',
                         reply_markup=stop_keyboard)
    await state.set_state(MessageState.chatting)


@router.message(StateFilter(AnalyzeState.chatting))
async def process_analyze(message: Message, state: FSMContext):
    if message.text == "Прекратить":
        await message.answer(text='Общение остановлено. Возврат в главное меню!', reply_markup=start_keyboard)
        await state.set_state(AnalyzeState.idle)
        return
    answer = await send_message('analyze', botRole)
    await message.answer(text=f"{answer}", reply_markup=stop_keyboard)
    await state.set_state(AnalyzeState.chatting)


@router.message(StateFilter(GenerateState.chatting))
async def process_analyze(message: Message, state: FSMContext):
    if message.text == "Прекратить":
        await message.answer(text='Общение остановлено. Возврат в главное меню!', reply_markup=start_keyboard)
        await state.set_state(GenerateState.idle)
        return
    answer = await send_message('genIdeas', botRole)
    await message.answer(text=f"{answer}", reply_markup=stop_keyboard)
    await state.set_state(GenerateState.chatting)


@router.message(StateFilter(BrainStormState.chatting))
async def process_analyze(message: Message, state: FSMContext):
    if message.text == "Прекратить":
        await message.answer(text='Общение остановлено. Возврат в главное меню!', reply_markup=start_keyboard)
        await state.set_state(BrainStormState.idle)
        return
    answer = await send_message('brainStorm', botRole)
    await message.answer(text=f"{answer}", reply_markup=stop_keyboard)
    await state.set_state(BrainStormState.chatting)


@router.message(StateFilter(MessageState.chatting))
async def process_message_command(message: Message, state: FSMContext):
    if message.text == "Прекратить":
        await message.answer(text='Общение остановлено. Возврат в главное меню!', reply_markup=start_keyboard)
        await state.set_state(MessageState.idle)
        return
    answer = await send_message('chat', botRole, message.text)
    await message.answer(text=f"{answer}", reply_markup=stop_keyboard)
    await state.set_state(MessageState.chatting)
