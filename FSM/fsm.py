from aiogram.fsm.state import StatesGroup, State


class MessageState(StatesGroup):
    idle = State()
    chatting = State()


class AnalyzeState(StatesGroup):
    idle = State()
    chatting = State()


class GenerateState(StatesGroup):
    idle = State()
    chatting = State()


class BrainStormState(StatesGroup):
    idle = State()
    chatting = State()
