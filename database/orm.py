import asyncio
import logging

from sqlalchemy import select, delete, update, values

from database.db import async_session_factory, engine, Base
from database.models import UsersOrm

logger = logging.getLogger(__name__)
sf = async_session_factory


async def create_tables():  # Очищает и создает все таблицы из ядра
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
        logging.info("Таблицы созданы успешно.")


async def insert_data(user_id, username):  # Внести пользователя в базу данных
    user = UsersOrm(id=user_id, username=username, banned=False, admin=False)
    async with sf() as session:
        session.add(user)
        await session.commit()
    logging.info("Пользователь записан.")


async def check_user(user_id):  # Проверка, существует ли этот пользователь
    async with sf() as session:
        print(user_id)
        query = select(UsersOrm).where(UsersOrm.id == user_id)
        try:
            (await session.execute(query)).scalars().all()[0].id
        except IndexError:
            logging.info("Пользователя нет в базе.")
            return False
        logging.info("Пользователь есть в базе.")
        return True


async def select_user(user_id):  # Выбор пользователя по ID
    async with sf() as session:
        query = select(UsersOrm).where(UsersOrm.id == user_id)
        res = await session.execute(query)
        user = res.scalars().all()[0]
        logging.info("Пользователь найден")
        return user


async def check_user_ban(user_id):  # Проверка, забанен ли пользователь
    async with sf() as session:
        query = select(UsersOrm).where(UsersOrm.id == user_id)
        res = (await session.execute(query)).scalars().all()
        if len(res) == 1:
            return res[0].banned
        else:
            return False


async def check_user_admin(user_id):  # Проверка, админ ли пользователь
    async with sf() as session:
        query = select(UsersOrm).where(UsersOrm.id == user_id)
        res = (await session.execute(query)).scalars().all()
        if len(res) == 1:
            return res[0].admin
        else:
            return False


async def ban_user(user_id):  # Сделать пользователя админом
    async with sf() as session:
        query = update(UsersOrm).where(UsersOrm.id == user_id).values(banned=True)
        await session.execute(query)
        await session.commit()


async def unban_user(user_id):  # Сделать пользователя админом
    async with sf() as session:
        query = update(UsersOrm).where(UsersOrm.id == user_id).values(banned=False)
        await session.execute(query)
        await session.commit()


async def make_admin(user_id):  # Сделать пользователя админом
    async with sf() as session:
        query = update(UsersOrm).where(UsersOrm.id == user_id).values(admin=True)
        await session.execute(query)
        await session.commit()

