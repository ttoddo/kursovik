import asyncio
import logging
from aiogram import Bot, Dispatcher

from config_data.config import load_config, config
from database.orm import create_tables
from dialogs import payment_dialog
from handlers import user_handlers, settings, bot_mode, bot_role, admin
from middlewares.middleware import BanCheckMiddleware


async def main() -> None:
    logging.basicConfig(
        level=logging.DEBUG,
        format='[%(asctime)s] #%(levelname)-8s %(filename)s:'
               '%(lineno)d - %(name)s - %(message)s'
    )

    logger = logging.getLogger(__name__)

    logger.debug('Лог уровня DEBUG')

    # Инициализируем бот и диспетчер
    bot = Bot(token=config.tg_bot.token)
    dp = Dispatcher()

    # Регистриуем роутеры в диспетчере
    dp.include_router(user_handlers.router)
    dp.message.outer_middleware(BanCheckMiddleware())
    dp.include_router(admin.router)
    dp.include_router(settings.router)
    dp.include_router(bot_mode.router)
    dp.include_router(payment_dialog.router)

    clear_database = False  # ОЧИСТКА И СОЗДАНИЕ БД
    if clear_database:
        await create_tables()
        logger.info("Таблицы сделаны.")

    # Пропускаем накопившиеся апдейты и запускаем polling
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


asyncio.run(main())
