from aiogram import BaseMiddleware
from aiogram.types import Message
from database.orm import check_user, check_user_ban


class BanCheckMiddleware(BaseMiddleware):
    async def __call__(self, handler, message: Message, data):
        if await check_user(user_id=message.from_user.id):
            if await check_user_ban(user_id=message.from_user.id):
                await message.answer('Вы забанены!')
                return
            else:
                return await handler(message, data)
        else:
            return await handler(message, data)
