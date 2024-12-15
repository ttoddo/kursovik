from aiogram.fsm.state import StatesGroup, State


class PaymentDialog(StatesGroup):
    start = State()


class Chat_mode(StatesGroup):
    analyze = State()
    brainStorm = State()
    generate = State()
    chat = State()


class Admin(StatesGroup):
    ban = State()
    unban = State()
    idle = State()


class Take_role(StatesGroup):
    take_role = State()


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
