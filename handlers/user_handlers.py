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
botRole = ''


@router.message(CommandStart(), StateFilter(default_state))
async def process_start_command(message: Message, state: FSMContext):
    await message.answer(text=f'Hello! User, {message.from_user.username}', reply_markup=register_keyboard)
    await state.set_state(Chat_mode.chat)


@router.callback_query(ButtonsCallbackFactory.filter(F.status == 'register'))
async def main_menu(query: CallbackQuery):
    await query.message.answer(text='Вы успешно зарегистрировались!')
    await query.message.answer(text='Давайте начнем', reply_markup=start_keyboard)


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


@router.message(lambda message: message.text == 'Не стоит')
async def begin_stop_command(message: Message, state: FSMContext):
    await message.answer(text='Если передумаете, можете просто нажать кнопочку',
                         reply_markup=start_keyboard)


@router.message(lambda message: message.text == 'Настройки')
async def begin_sett_command(message: Message):
    await message.answer(text='Вы перешли в настройки, выберите пункт: ',
                         reply_markup=setting_keyboard)


@router.callback_query(ButtonsCallbackFactory.filter(F.status == 'give role'))
async def set_role(query: CallbackQuery, state: FSMContext):

    await query.message.answer(text='Задайте роль боту: ', reply_markup=start_keyboard)
    await state.set_state(Take_role.take_role)


@router.message(StateFilter(Take_role.take_role))
async def take_role(message: Message, state: FSMContext):
    global botRole
    botRole = message.text
    await message.answer("Роль успешно задана, возвращаемся в меню!", reply_markup=start_keyboard)
    await state.set_state(Chat_mode.chat)
    await message.answer(text='Чат-мод сброшен на режим общения, задайте его в настройках, если хотите изменить')


@router.callback_query(ButtonsCallbackFactory.filter(F.status == 'change mode'))
async def mode_menu(query: CallbackQuery):
    await query.message.answer(text='Выберите режим, в котором будет работать бот: ', reply_markup=choose_mode_keyboard)


@router.callback_query(ButtonsCallbackFactory.filter(F.status == 'analyze'))
async def analyze_mode(query: CallbackQuery, state: FSMContext):
    await state.set_state(Chat_mode.analyze)
    await query.message.answer(text='Выбран режим анализа! Возврат в меню ', reply_markup=start_keyboard)


@router.callback_query(ButtonsCallbackFactory.filter(F.status == 'brainStorm'))
async def analyze_mode(query: CallbackQuery, state: FSMContext):
    await state.set_state(Chat_mode.brainStorm)
    await query.message.answer(text='Выбран режим мозгового штурма! Возврат в меню ', reply_markup=start_keyboard)


@router.callback_query(ButtonsCallbackFactory.filter(F.status == 'genIdeas'))
async def analyze_mode(query: CallbackQuery, state: FSMContext):
    await state.set_state(Chat_mode.generate)
    await query.message.answer(text='Выбран режим генерации идей! Возврат в меню ', reply_markup=start_keyboard)


@router.callback_query(ButtonsCallbackFactory.filter(F.status == 'chat'))
async def chat_mode(query: CallbackQuery, state: FSMContext):
    await state.set_state(Chat_mode.chat)
    await query.message.answer(text='Выбран режим общения! Возврат в меню ', reply_markup=start_keyboard)


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

    # messages.append(HumanMessage(content=message.text))
    # res = model.invoke(messages)
    # messages.append(res)
    answer = await send_message('chat', botRole)
    await message.answer(text=f"{answer}", reply_markup=stop_keyboard)
    await state.set_state(MessageState.chatting)
