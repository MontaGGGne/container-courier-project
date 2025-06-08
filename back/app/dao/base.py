from fastapi import HTTPException
from sqlalchemy import delete, insert, select, update

from app.database import async_session_maker


class BaseDAO:
    model = None

    @classmethod
    async def create(cls, data):
        async with async_session_maker() as session:
            values = data.dict(exclude_unset=True)
            try:
                stmt = insert(cls.model).values(**values).returning(cls.model.id)
                result = await session.execute(stmt)
                created_id = result.scalar_one()
                await session.commit()
                return created_id
            except:
                raise HTTPException(status_code=400, detail="Ошибка добавления")

    @classmethod
    async def find_all(cls):
        async with async_session_maker() as session:
            query = select(cls.model)
            result = await session.execute(query)
            return result.scalars().all()

    @classmethod
    async def find_one_or_none(cls, **filter_by):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(**filter_by)
            result = await session.execute(query)
            return result.scalar_one_or_none()

    @classmethod
    async def find_by_email(cls, email: str):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(email=email)
            result = await session.execute(query)
            return result.scalar_one_or_none()

    @classmethod
    async def delete(cls, id: int):
        async with async_session_maker() as session:
            stmt = delete(cls.model).where(cls.model.id == id)
            await session.execute(stmt)
            await session.commit()

    @classmethod
    async def update(cls, data):
        async with async_session_maker() as session:
            values = data.dict(exclude_unset=True)
            try:
                stmt = update(cls.model).where(cls.model.id == data.id).values(**values)
                await session.execute(stmt)
                await session.commit()
            except:
                raise HTTPException(status_code=400, detail="Ошибка обновления данных")
