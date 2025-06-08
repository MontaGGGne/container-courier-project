from sqlalchemy import asc, desc, func, select, update

from app.dao.base import BaseDAO
from app.database import async_session_maker
from app.models import Orders


class LogicDAO(BaseDAO):
    model = Orders

    @classmethod
    async def all_active_orders(cls):
        async with async_session_maker() as session:
            stmt = (
                select(Orders)
                .where(Orders.user_id == None)
                .order_by(desc(Orders.time_create))
            )
            result = await session.execute(stmt)
            result = result.scalars().all()
            return [
                {
                    "numorder": res.id,
                    "timecreate": res.time_create.strftime("%H:%M:%S")
                    if res.time_create
                    else "",
                    "shop": res.address_start,
                    "address": res.address_end,
                    "tmst": 1 if res.time_start else 0,
                    "tmend": 1 if res.time_end else 0,
                    "typepay": res.type_payment,
                    "sumpay": round(res.price * (1 - res.discount), 1)
                    if res.discount is not None
                    else res.price,
                }
                for res in result
            ]

    @classmethod
    async def all_in_orders(cls, user):
        async with async_session_maker() as session:
            stmt = (
                select(Orders)
                .where(Orders.user_id == user.id)
                .order_by(desc(Orders.time_start))
            )
            result = await session.execute(stmt)
            result = result.scalars().all()
            return [
                {
                    "numorder": res.id,
                    "timecreate": res.time_create.strftime("%H:%M:%S")
                    if res.time_create
                    else "",
                    "shop": res.address_start,
                    "address": res.address_end,
                    "tmst": 1 if res.time_start else 0,
                    "tmend": 1 if res.time_end else 0,
                    "typepay": res.type_payment,
                    "sumpay": round(res.price * (1 - res.discount), 1)
                    if res.discount is not None
                    else res.price,
                }
                for res in result
            ]

    @classmethod
    async def take_orders(cls, id, user):
        async with async_session_maker() as session:
            time_now = func.now()
            stmt = (
                update(Orders)
                .where(Orders.id == id)
                .values(user_id=user.id, time_start=time_now)
            )
            await session.execute(stmt)
            await session.commit()

    @classmethod
    async def close_orders(cls, id, user):
        async with async_session_maker() as session:
            time_now = func.now()
            stmt = (
                update(Orders)
                .where(Orders.id == id)
                .values(user_id=user.id, time_end=time_now)
            )
            await session.execute(stmt)
            await session.commit()

    @classmethod
    async def get_all_inf(cls, id):
        async with async_session_maker() as session:
            stmt = select(Orders).where(Orders.id == id)
            result = await session.execute(stmt)
            result = result.scalars().all()
            if result:
                result = {
                    "numorder": result.id,
                    "timecreate": result.time_create,
                    "shop": result.address_start,
                    "address": result.address_end,
                    "typepay": result.type_payment,
                    "sumpay": round(result.price * (1 - result.discount), 1)
                    if not result.discount
                    else result.price,
                }
            return result

    @classmethod
    async def get_prm_inf(cls, id):
        async with async_session_maker() as session:
            stmt = select(Orders).where(Orders.id == id)
            result = await session.execute(stmt)
            result = result.scalars().all()
            result = result[0]
            if result:
                result = {
                    "numorder": result.id,  #
                    "timestart": result.time_start.strftime("%H:%M"),  #
                    "shop": result.address_start,  #
                    "address": result.address_end,  #
                    "typepay": result.type_payment,  #
                    "price": result.price,  #
                    "discont": 0
                    if result.discount is None
                    else round(result.discount * result.price, 1),  #
                    "sumpay": result.price
                    if result.discount is None
                    else round(result.price * (1 - result.discount), 1),
                    "comment": result.comment,
                    "client": " ".join(result.client.split(" ")[:1]),  #
                    "clientNumber": result.client_number,  #
                    "shopName": result.shop_name,
                }
            return result

    @classmethod
    async def history_orders(cls, user):
        async with async_session_maker() as session:
            stmt = select(Orders).where(Orders.user_id == user.id)
            result = await session.execute(stmt)
            print(result.fetchall())

            return [
                {
                    "numorder": res.id,
                    "timecreate": res.time_create,
                    "shop": res.address_start,
                    "address": res.address_end,
                    "typepay": res.type_payment,
                    "sumpay": round(res.price * (1 - res.discount), 1)
                    if not res.discount
                    else res.price,
                }
                for res in result.fetchall()
            ]
