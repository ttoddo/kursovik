import uuid

from aiogram import Router, F
from aiogram.filters.callback_data import CallbackData
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import Message, CallbackQuery, LabeledPrice, PreCheckoutQuery
from aiogram_dialog import DialogManager, Window, Dialog, setup_dialogs, StartMode
from aiogram_dialog.widgets.kbd import Button
from aiogram_dialog.widgets.text import Const

from FSM.fsm import PaymentDialog
from config_data.config import config


async def buy_sub(callback: CallbackQuery, button: Button, dialog: DialogManager):
    payment_id = str(uuid.uuid4())  # Идентификатор для платежа
    await callback.message.answer_invoice(
        title='Поддержка создателя',
        description='Поддержка создателя',
        payload=payment_id,
        #provider_token=,
        currency='RUB',
        prices=[LabeledPrice(label='Оплата услуг', amount=50)])
    await callback.message.answer(text='Номер тест-карты: 4000 0000 0000 0408, cvv=000, date=01/01')


payment_window = Window(
    Const("Буду рад поддержке ^_^"),
    Button(Const("Закинуть монетку"), id='pay', on_click=buy_sub),
    state=PaymentDialog.start,
)

storagePay = MemoryStorage()
router = Router()
dialog = Dialog(payment_window)
router.include_router(dialog)
setup_dialogs(router)


@router.message(lambda message: message.text == 'Поддержать разработчика')
async def payment_dialog_start(message: Message, dialog_manager: DialogManager):
    await dialog_manager.start(PaymentDialog.start, mode=StartMode.RESET_STACK)


@router.pre_checkout_query()
async def process_pre_checkout_query(query: PreCheckoutQuery):
    await query.bot.answer_pre_checkout_query(pre_checkout_query_id=query.id, ok=True)


@router.message(F.successful_payment)
async def success_payment_handler(message: Message):
    await message.answer(text='Спасибо за  поддержку!🤗\nРазработчик стал счастливее!')
