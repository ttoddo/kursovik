from aiogram import Router, F
from aiogram.filters import Command, CommandStart, StateFilter
from aiogram.filters.callback_data import CallbackData
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state
from aiogram.types import CallbackQuery
from FSM.fsm import *
from keyboards.keyboards import *
from gigachat_data.gigaChat import *

router = Router()


@router.message(CommandStart(), StateFilter(default_state))
async def process_start_command(message: Message):
    await message.answer(text=f'Hello! User, {message.from_user.username}', reply_markup=register_keyboard)


@router.callback_query(ButtonsCallbackFactory.filter(F.status == 'register'))
async def main_menu(query: CallbackQuery):
    await query.message.answer(text='Вы успешно зарегистрировались!')
    await query.message.answer(text='Давайте начнем', reply_markup=start_keyboard)


@router.message(lambda message: message.text == 'Давай')
async def begin_chatting_command(message: Message, state: FSMContext):
    await message.answer(text='Вы в режиме общения! Для остановки напишите/нажмите кнопку хватит',
                         reply_markup=stop_keyboard)
    await state.set_state(currentState.chatting)


@router.message(lambda message: message.text == 'Не стоит')
async def begin_chatting_command(message: Message, state: FSMContext):
    await message.answer(text='Если передумаете, можете просто нажать кнопочку',
                         reply_markup=start_keyboard)


@router.message(StateFilter(AnalyzeState.chatting))
async def process_analyze(message: Message, state: FSMContext):
    if message.text == "Прекратить":
        await message.answer(text='Общение остановлено. Возврат в главное меню!', reply_markup=start_keyboard)
        await state.set_state(MessageState.idle)
        return
    answer = await send_message('analyze')
    await message.answer(text=f"{answer}", reply_markup=stop_keyboard)
    await state.set_state(AnalyzeState.chatting)


@router.message(StateFilter(GenerateState.chatting))
async def process_analyze(message: Message, state: FSMContext):
    if message.text == "Прекратить":
        await message.answer(text='Общение остановлено. Возврат в главное меню!', reply_markup=start_keyboard)
        await state.set_state(MessageState.idle)
        return
    answer = await send_message('genIdeas')
    await message.answer(text=f"{answer}", reply_markup=stop_keyboard)
    await state.set_state(AnalyzeState.chatting)


@router.message(StateFilter(BrainStormState.chatting))
async def process_analyze(message: Message, state: FSMContext):
    if message.text == "Прекратить":
        await message.answer(text='Общение остановлено. Возврат в главное меню!', reply_markup=start_keyboard)
        await state.set_state(MessageState.idle)
        return
    answer = await send_message('brainStorm')
    await message.answer(text=f"{answer}", reply_markup=stop_keyboard)
    await state.set_state(AnalyzeState.chatting)


@router.message(StateFilter(MessageState.chatting))
async def process_message_command(message: Message, state: FSMContext):
    if message.text == "Прекратить":
        await message.answer(text='Общение остановлено. Возврат в главное меню!', reply_markup=start_keyboard)
        await state.set_state(MessageState.idle)
        return

    # messages.append(HumanMessage(content=message.text))
    # res = model.invoke(messages)
    # messages.append(res)
    answer = await send_message('chat')
    await message.answer(text=f"{answer}", reply_markup=stop_keyboard)
    await state.set_state(MessageState.chatting)
