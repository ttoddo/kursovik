import asyncio
import logging

from sqlalchemy import Table, Column, Integer, String, BOOLEAN, MetaData, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database.db import Base, engine


class UsersOrm(Base):  # Таблица пользователей
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str]
    admin: Mapped[bool | None]
    banned: Mapped[bool]


