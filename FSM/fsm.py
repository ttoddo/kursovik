from aiogram.fsm.state import StatesGroup, State


class MessageState(StatesGroup):
    idle = State()
    chatting = State()
