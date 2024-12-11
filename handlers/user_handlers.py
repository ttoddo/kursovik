from aiogram import Router, F
from aiogram.filters import Command, CommandStart
from aiogram.fsm.context import FSMContext
from FSM.fsm import *
from keyboards.keyboards import *
from gigachat_data.gigaChat import *

router = Router()


@router.message(CommandStart())
async def process_start_command(message: Message, state: FSMContext):
    await message.answer(text='/start', reply_markup=start_keyboard)
    await state.set_state(MessageState.chatting)


@router.message(MessageState.chatting)
async def process_message_command(message: Message, state: FSMContext):
    if message.text == "Хватит":
        await state.set_state(MessageState.idle)
        return

    #messages.append(HumanMessage(content=message.text))
    #res = model.invoke(messages)
    #messages.append(res)
    await message.answer(text="Привет, я гигачат", reply_markup=stop_keyboard)
    await state.set_state(MessageState.chatting)

