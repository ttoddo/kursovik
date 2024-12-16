from aiogram import Router
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from FSM.fsm import Chat_mode,  GenerateState, MessageState, AnalyzeState, BrainStormState, Take_role
from gigachat_data.gigaChat import send_message
from keyboards.keyboards import start_keyboard, stop_keyboard
botRole = ''
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
    answer = await send_message('analyze', botRole, message)
    await message.answer(text=f"{answer}", reply_markup=stop_keyboard)
    await state.set_state(AnalyzeState.chatting)


@router.message(StateFilter(GenerateState.chatting))
async def process_analyze(message: Message, state: FSMContext):
    if message.text == "Прекратить":
        await message.answer(text='Общение остановлено. Возврат в главное меню!', reply_markup=start_keyboard)
        await state.set_state(GenerateState.idle)
        return
    answer = await send_message('genIdeas', botRole, message)
    await message.answer(text=f"{answer}", reply_markup=stop_keyboard)
    await state.set_state(GenerateState.chatting)


@router.message(StateFilter(BrainStormState.chatting))
async def process_analyze(message: Message, state: FSMContext):
    if message.text == "Прекратить":
        await message.answer(text='Общение остановлено. Возврат в главное меню!', reply_markup=start_keyboard)
        await state.set_state(BrainStormState.idle)
        return
    answer = await send_message('brainStorm', botRole, message)
    await message.answer(text=f"{answer}", reply_markup=stop_keyboard)
    await state.set_state(BrainStormState.chatting)


@router.message(StateFilter(MessageState.chatting))
async def process_message_command(message: Message, state: FSMContext):
    if message.text == "Прекратить":
        await message.answer(text='Общение остановлено. Возврат в главное меню!', reply_markup=start_keyboard)
        await state.set_state(MessageState.idle)
        return
    print(botRole)
    answer = await send_message('chat', botRole, message.text)
    await message.answer(text=f"{answer}", reply_markup=stop_keyboard)
    await state.set_state(MessageState.chatting)


@router.message(StateFilter(Take_role.take_role))
async def take_role(message: Message, state: FSMContext):
    global botRole
    botRole = message.text
    await message.answer("Роль успешно задана, возвращаемся в меню!", reply_markup=start_keyboard)
    await state.set_state(Chat_mode.chat)
    await message.answer(text='Чат-мод сброшен на режим общения, задайте его в настройках, если хотите изменить')
